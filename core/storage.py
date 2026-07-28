"""Leads and gallery persistence. CSV + JSON on disk — simple and booth-proof."""

import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
GALLERY_DIR = ROOT / "gallery"
LEADS_CSV = DATA_DIR / "leads.csv"
GALLERY_META = GALLERY_DIR / "metadata.json"

LEAD_FIELDS = [
    "timestamp", "ticket", "name", "company", "job_title", "phone", "email",
    "film", "task_id", "status", "video_path", "consent", "email_sent",
    "photo_url", "asset_id", "costar",
]


def ensure_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    GALLERY_DIR.mkdir(exist_ok=True)


def load_leads() -> list[dict]:
    if not LEADS_CSV.exists():
        return []
    with LEADS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def next_ticket() -> str:
    return f"PP-{len(load_leads()) + 1:04d}"


def save_lead(lead: dict) -> None:
    ensure_dirs()
    is_new = not LEADS_CSV.exists()
    row = {k: lead.get(k, "") for k in LEAD_FIELDS}
    row["timestamp"] = row["timestamp"] or datetime.now().isoformat(timespec="seconds")
    with LEADS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LEAD_FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def update_lead(ticket: str, **fields) -> None:
    leads = load_leads()
    for lead in leads:
        if lead["ticket"] == ticket:
            lead.update({k: str(v) for k, v in fields.items()})
    with LEADS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LEAD_FIELDS)
        writer.writeheader()
        writer.writerows(leads)


GUESTS_JSON = DATA_DIR / "guest_photos.json"


def load_guest_photos() -> list[dict]:
    """Saved guest photos, newest first: [{id, label, tos_url, asset_id, created}]."""
    if not GUESTS_JSON.exists():
        return []
    items = json.loads(GUESTS_JSON.read_text(encoding="utf-8"))
    return sorted(items, key=lambda e: e.get("created", ""), reverse=True)


def _write_guests(items: list[dict]) -> None:
    ensure_dirs()
    GUESTS_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


def save_guest_photo(entry: dict) -> None:
    items = load_guest_photos()
    items.append(entry)
    _write_guests(items)


def get_guest_photo(photo_id: str) -> dict | None:
    return next((e for e in load_guest_photos() if e.get("id") == photo_id), None)


def update_guest_photo(photo_id: str, **fields) -> None:
    items = load_guest_photos()
    for e in items:
        if e.get("id") == photo_id:
            e.update({k: str(v) for k, v in fields.items()})
    _write_guests(items)


def delete_guest_photo(photo_id: str) -> None:
    _write_guests([e for e in load_guest_photos() if e.get("id") != photo_id])


def load_gallery() -> list[dict]:
    """Finished films, newest first: [{ticket, name, film, video, created}]."""
    if not GALLERY_META.exists():
        return []
    entries = json.loads(GALLERY_META.read_text(encoding="utf-8"))
    return sorted(entries, key=lambda e: e.get("created", ""), reverse=True)


def add_gallery_entry(entry: dict) -> None:
    ensure_dirs()
    entries = json.loads(GALLERY_META.read_text(encoding="utf-8")) if GALLERY_META.exists() else []
    entries.append(entry)
    GALLERY_META.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
