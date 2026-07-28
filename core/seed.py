"""Seed demo content into the stores on startup.

A fresh Streamlit Cloud deploy has empty (ephemeral) galleries. This loads the
committed sample face + sample ad videos (hosted on TOS) so the Guest Gallery
and NOW SHOWING look populated for demos. Idempotent and once-per-process:
only adds entries not already present, so real guest content is never touched.
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
    _seed(SEED_DIR / "gallery.json", storage.load_gallery, storage.add_gallery_entry, "ticket")


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
