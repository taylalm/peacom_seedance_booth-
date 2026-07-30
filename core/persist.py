"""Cloud persistence for booth data — survives Streamlit Cloud container loss.

Streamlit Community Cloud disks are EPHEMERAL: a redeploy, reboot, or overnight
hibernation recycles the container and wipes leads/guests/gallery (this cost us
the TikTok Shop event's lead list). Fix: every write is mirrored to TOS under a
fixed per-app key, and on startup any file missing locally is restored from TOS.

Backups are best-effort and asynchronous — a TOS hiccup (e.g. expired STS
token) never blocks or breaks the booth flow; it just logs.
"""

import logging
import threading
from core import storage, tos_store

log = logging.getLogger("premiere.persist")

_cfg: dict = {}

FILES = {
    "leads.csv": storage.LEADS_CSV,
    "guest_photos.json": storage.GUESTS_JSON,
    "gallery_metadata.json": storage.GALLERY_META,
}


def configure(tos_cfg: dict, cred: dict, prefix: str = "appdata/premiere") -> None:
    _cfg.update(tos=tos_cfg or {}, cred=cred or {}, prefix=prefix)


def enabled() -> bool:
    return bool(_cfg.get("tos")) and tos_store.is_configured(_cfg["tos"])


def _key(name: str) -> str:
    return f"{_cfg['prefix']}/{name}"


def backup(name: str) -> None:
    """Upload one data file to its fixed TOS key (overwrites previous copy)."""
    if not enabled():
        return
    path = FILES[name]
    if not path.exists():
        return
    client = tos_store._client(_cfg["tos"], _cfg["cred"])
    client.put_object(_cfg["tos"]["bucket"], _key(name), content=path.read_bytes())


def backup_async(name: str) -> None:
    threading.Thread(target=_safe_backup, args=(name,), daemon=True).start()


def _safe_backup(name: str) -> None:
    try:
        backup(name)
    except Exception:
        log.exception("cloud backup failed for %s (booth continues)", name)


def restore_all() -> None:
    """On startup: pull any data file that exists in TOS but not on this disk
    (i.e. we are in a fresh container after a recycle)."""
    if not enabled():
        return
    storage.ensure_dirs()
    try:
        client = tos_store._client(_cfg["tos"], _cfg["cred"])
    except Exception:
        log.exception("persist restore skipped (no TOS client)")
        return
    for name, path in FILES.items():
        if path.exists():
            continue
        try:
            resp = client.get_object(_cfg["tos"]["bucket"], _key(name))
            path.write_bytes(resp.read())
            log.info("restored %s from cloud backup", name)
        except Exception:
            pass  # no backup yet — first boot
