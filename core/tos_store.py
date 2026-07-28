"""BytePlus TOS object storage — hosts each captured photo at a public URL.

CreateAsset requires a public HTTP(S) URL (base64/data-URI is rejected), so we
upload the booth photo here and hand the URL to the asset library. Objects are
namespaced by event prefix so one bucket can serve multiple event apps.
"""

import datetime as dt
import os
import uuid

import tos

from core import creds


def _client(tos_cfg: dict, cred: dict):
    kwargs = dict(
        ak=cred["ak"], sk=cred["sk"],
        endpoint=tos_cfg["endpoint"], region=tos_cfg["region"],
        security_token=cred.get("session_token") or None,
    )
    ca = os.environ.get("REQUESTS_CA_BUNDLE")  # corporate proxy trust (see netfix)
    if ca:
        kwargs["ca_crt"] = ca
    return tos.TosClientV2(**kwargs)


def upload_bytes(tos_cfg: dict, data: bytes, *, prefix: str, ext: str,
                 content_type: str, cred: dict | None = None) -> tuple[str, str]:
    """Upload arbitrary bytes; return (key, public_url).

    tos_cfg: {bucket, region, endpoint}. Creds resolved from env/secrets unless
    passed explicitly. Public URL works only on a public-read bucket; for a
    private bucket, swap this for a pre-signed GET URL."""
    cred = cred or creds.resolve()
    key = f"{prefix}/{dt.date.today().isoformat()}/{uuid.uuid4().hex}.{ext}"
    client = _client(tos_cfg, cred)
    client.put_object(tos_cfg["bucket"], key, content=data, content_type=content_type)
    return key, f"https://{tos_cfg['bucket']}.{tos_cfg['endpoint']}/{key}"


def upload_image(tos_cfg: dict, data: bytes, *, prefix: str = "premiere",
                 ext: str = "jpg", content_type: str = "image/jpeg",
                 cred: dict | None = None) -> tuple[str, str]:
    return upload_bytes(tos_cfg, data, prefix=prefix, ext=ext, content_type=content_type, cred=cred)


def upload_video(tos_cfg: dict, data: bytes, *, prefix: str = "films",
                 cred: dict | None = None) -> tuple[str, str]:
    return upload_bytes(tos_cfg, data, prefix=prefix, ext="mp4", content_type="video/mp4", cred=cred)


def is_configured(tos_cfg: dict) -> bool:
    return bool(tos_cfg.get("bucket") and tos_cfg.get("endpoint"))
