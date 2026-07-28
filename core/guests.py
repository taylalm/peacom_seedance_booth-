"""Guest photo intake — capture once, host on TOS, reuse forever.

Each captured/uploaded photo is uploaded to TOS immediately and saved as a
reusable guest-photo entry (with its public URL). The Seedance asset is created
lazily on first render and cached back onto the entry, so regenerating a film
for the same person needs no re-upload and no re-registration.
"""

import uuid
from datetime import datetime

from core import creds, storage, tos_store, worker


def realface_available() -> bool:
    """True when TOS + asset credentials are configured (real-face mode)."""
    cfg = getattr(worker, "_config", {}) or {}
    return creds.is_complete(cfg.get("assets", {})) and tos_store.is_configured(cfg.get("tos", {}))


def save_capture(photo_bytes: bytes, label: str = "") -> dict:
    """Upload a freshly captured photo to TOS and persist a guest-photo entry.
    Fast (just the upload); the asset is created later by the render worker."""
    cfg = worker._config
    _, url = tos_store.upload_image(
        cfg["tos"], photo_bytes,
        prefix=cfg.get("event_prefix", "premiere"), cred=cfg["assets"],
    )
    entry = {
        "id": uuid.uuid4().hex[:12],
        "label": label or "Guest",
        "tos_url": url,
        "asset_id": "",
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    storage.save_guest_photo(entry)
    return entry
