"""Seed demo content into the stores on startup.

A fresh Streamlit Cloud deploy has empty (ephemeral) galleries. This loads the
committed sample face + sample ad videos (hosted on TOS) so the Guest Gallery
and NOW SHOWING look populated for demos. Idempotent and once-per-process.

The seed files are AUTHORITATIVE for sample content: SAMPLE-* gallery entries
that are no longer in seed/gallery.json get pruned, so removing a clip from
the seed removes it from the deployed gallery too. Real guest content (non
SAMPLE tickets) is never touched.
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
    _prune_stale_samples()


def _prune_stale_samples() -> None:
    """Drop SAMPLE-* gallery entries that the committed seed no longer lists."""
    try:
        path = SEED_DIR / "gallery.json"
        wanted = set()
        if path.exists():
            wanted = {e.get("ticket") for e in json.loads(path.read_text(encoding="utf-8"))}
        for entry in storage.load_gallery():
            ticket = entry.get("ticket", "")
            if ticket.startswith("SAMPLE-") and ticket not in wanted:
                storage.delete_gallery_entry(ticket)
    except Exception:  # pruning must never break app startup
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
