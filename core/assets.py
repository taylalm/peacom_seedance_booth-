"""BytePlus ModelArk real-human portrait asset library client.

The path that lets real faces through Seedance (inline base64 is always
rejected as a real person). Three stages:

  1. real-person liveness verification  -> Asset Group ID  (per visitor, once)
  2. upload the portrait as an asset     -> asset ID (poll until Active)
  3. reference it in generation as        asset://<asset ID>

Auth here is AK/SK signature signing (via byteplussdkcore universal.do_call),
NOT the Bearer ARK_API_KEY used for generation.
"""

import logging
import os
import time

from byteplussdkcore.api_client import ApiClient
from byteplussdkcore.configuration import Configuration
from byteplussdkcore.universal import UniversalApi, UniversalInfo

log = logging.getLogger("premiere.assets")

SERVICE = "ark"
VERSION = "2024-01-01"


class AssetError(RuntimeError):
    pass


def _api(cfg: dict) -> UniversalApi:
    c = Configuration()
    c.ak = cfg["ak"]
    c.sk = cfg["sk"]
    if cfg.get("session_token"):
        c.session_token = cfg["session_token"]  # required for temporary (STS) creds
    c.region = cfg.get("region", "ap-southeast-1")
    if cfg.get("host"):
        c.host = cfg["host"]
    ca = os.environ.get("REQUESTS_CA_BUNDLE")  # corporate proxy trust (see netfix)
    if ca:
        c.ssl_ca_cert = ca
    return UniversalApi(ApiClient(c))


def _call(cfg: dict, action: str, body: dict) -> dict:
    info = UniversalInfo(
        method="POST", service=SERVICE, version=VERSION,
        action=action, content_type="application/json",
    )
    try:
        resp = _api(cfg).do_call(info, body)
    except Exception as exc:  # noqa: BLE001
        raise AssetError(f"{action} failed: {type(exc).__name__}: {str(exc)[:300]}") from exc
    if isinstance(resp, dict) and "Result" in resp:
        return resp["Result"]
    return resp if isinstance(resp, dict) else {"_raw": resp}


# ---------------------------------------------------------------- step 1

def create_validate_session(cfg: dict, callback_url: str, lang: str = "en") -> dict:
    """Start liveness verification. Returns {BytedToken, H5Link}.
    Show H5Link (as a QR) to the visitor; they complete liveness + authorization."""
    res = _call(cfg, "CreateVisualValidateSession", {
        "CallbackURL": callback_url,
        "ProjectName": cfg.get("project", "default"),
    })
    link = res.get("H5Link", "")
    if link and "lng=" not in link:
        link += ("&" if "?" in link else "?") + f"lng={lang}"
    return {"BytedToken": res.get("BytedToken", ""), "H5Link": link}


def get_validate_result(cfg: dict, byted_token: str) -> str | None:
    """Poll for the Asset Group ID. Returns GroupId once verification passes,
    else None (still pending). BytedToken is valid ~30 min."""
    try:
        res = _call(cfg, "GetVisualValidateResult", {
            "BytedToken": byted_token,
            "ProjectName": cfg.get("project", "default"),
        })
    except AssetError:
        return None  # not ready yet / transient
    return res.get("GroupId") or None


def wait_for_group(cfg: dict, byted_token: str, *, poll_seconds=5, timeout_seconds=1500) -> str:
    deadline = time.monotonic() + timeout_seconds
    while True:
        gid = get_validate_result(cfg, byted_token)
        if gid:
            return gid
        if time.monotonic() > deadline:
            raise AssetError("liveness verification not completed in time")
        time.sleep(poll_seconds)


# ------------------------------------------------- virtual avatar library
# (docs 2333565/2333601 — no liveness; groups are created directly via API.
#  Real faces pass only with Moderation Skip, which needs the content
#  pre-filter turned off in the console — KYC-High entitlement.)

def create_asset_group(cfg: dict, name: str, description: str = "") -> str:
    """Create a virtual-avatar (AIGC) asset group. Returns group Id.
    First-ever call on an account requires signing an authorization letter
    in the ModelArk console."""
    res = _call(cfg, "CreateAssetGroup", {
        "Name": name,
        "Description": description or name,
        "ProjectName": cfg.get("project", "default"),
    })
    group_id = res.get("Id")
    if not group_id:
        raise AssetError(f"CreateAssetGroup returned no Id: {res}")
    return group_id


# ---------------------------------------------------------------- step 2

def create_asset(cfg: dict, group_id: str, image_url: str, *, name: str = "", skip_moderation=False) -> str:
    """Register a hosted portrait image into the person's asset group. Returns asset Id.
    The face must match the liveness reference (same single person)."""
    body = {
        "GroupId": group_id,
        "URL": image_url,
        "AssetType": "Image",
        "ProjectName": cfg.get("project", "default"),
    }
    if name:
        body["Name"] = name
    if skip_moderation:
        body["Moderation"] = {"Strategy": "Skip"}
    res = _call(cfg, "CreateAsset", body)
    asset_id = res.get("Id")
    if not asset_id:
        raise AssetError(f"CreateAsset returned no Id: {res}")
    return asset_id


def get_asset(cfg: dict, asset_id: str) -> dict:
    return _call(cfg, "GetAsset", {"Id": asset_id, "ProjectName": cfg.get("project", "default")})


def wait_asset_active(cfg: dict, asset_id: str, *, poll_seconds=5, timeout_seconds=900) -> dict:
    """Poll GetAsset until Status is Active. Raises on Failed/timeout."""
    deadline = time.monotonic() + timeout_seconds
    while True:
        res = get_asset(cfg, asset_id)
        status = res.get("Status", "")
        if status == "Active":
            return res
        if status == "Failed":
            raise AssetError(f"asset {asset_id} processing failed (face mismatch or moderation)")
        if time.monotonic() > deadline:
            raise AssetError(f"asset {asset_id} not Active in time (last status: {status})")
        time.sleep(poll_seconds)


def asset_uri(asset_id: str) -> str:
    return f"asset://{asset_id}"
