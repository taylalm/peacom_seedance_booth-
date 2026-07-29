"""Seed demo content into the stores on startup.

A fresh Streamlit Cloud deploy has empty (ephemeral) galleries. This loads the
committed sample face + sample ad videos (hosted on TOS) so the Guest Gallery
and NOW SHOWING look populated for demos. Idempotent and once-per-process.

The seed files are AUTHORITATIVE for sample content: SAMPLE-* gallery entries
are fully reconciled against seed/gallery.json — entries removed from the seed
disappear, and entries whose video URL changed get replaced with the new
version. Real guest content (non-SAMPLE tickets) is never touched.
"""

import json
from pathlib import Path

from core import storage

SEED_DIR = Path(__file__).resolve().parent.parent / "seed"
_seeded = False


def seed_demo_content() -> None:
    global _seeded
    if _seeded:
        return
    _seeded = True
    _seed(SEED_DIR / "guests.json", storage.load_guest_photos, storage.save_guest_photo, "id")
    _sync_sample_gallery()


def _sync_sample_gallery() -> None:
    """Make SAMPLE-* gallery entries match seed/gallery.json exactly:
    delete stale/outdated ones, then add whatever is missing."""
    try:
        path = SEED_DIR / "gallery.json"
        seeds = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
        wanted = {e.get("ticket"): e for e in seeds}

        # remove SAMPLE entries that are gone from the seed OR point at an old video
        for entry in storage.load_gallery():
            ticket = entry.get("ticket", "")
            if not ticket.startswith("SAMPLE-"):
                continue  # real guest content — never touched
            want = wanted.get(ticket)
            if want is None or want.get("video") != entry.get("video"):
                storage.delete_gallery_entry(ticket)

        # add any seed entry not currently present
        existing = {e.get("ticket") for e in storage.load_gallery()}
        for entry in seeds:
            if entry.get("ticket") not in existing:
                storage.add_gallery_entry(entry)
    except Exception:  # seeding must never break app startup
        pass


def _seed(path: Path, load, add, key: str) -> None:
    if not path.exists():
        return
    try:
        seeds = json.loads(path.read_text(encoding="utf-8"))
        existing = {e.get(key) for e in load()}
        for entry in seeds:
            if entry.get(key) not in existing:
                add(entry)
    except Exception:  # seeding must never break app startup
        pass
