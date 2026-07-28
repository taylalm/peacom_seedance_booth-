"""The production backlot — background render queue.

A dispatcher thread consumes jobs; each job renders in its own thread,
gated by a semaphore honoring ModelArk's 3-concurrent-task ceiling.
Runs fully off the Streamlit script thread: the visitor never waits.

Mock mode (no ARK credentials): simulates a short render and premieres a
sample clip, so booth dry-runs work without spending tokens.
"""

import logging
import queue
import threading
import time
from datetime import datetime
from pathlib import Path

from core import assets, emailer, films, seedance, storage, tos_store

log = logging.getLogger("premiere.worker")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

MAX_CONCURRENT = 3  # ModelArk per-account concurrent task limit
MOCK_RENDER_SECONDS = 20
MOCK_VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"

_queue: "queue.Queue[dict]" = queue.Queue()
_semaphore = threading.BoundedSemaphore(MAX_CONCURRENT)
_start_lock = threading.Lock()
_started = False
_config: dict = {}


_group_lock = threading.Lock()


def ensure_started(config: dict) -> None:
    """Start the dispatcher once per server process.
    config: api_key, model, smtp, assets (cred dict), tos (cfg dict), group_name."""
    global _started, _config
    with _start_lock:
        _config = config
        if _started:
            return
        threading.Thread(target=_dispatch, name="pp-dispatcher", daemon=True).start()
        _started = True
        log.info("production worker started (%s mode)", _mode())


def _mode() -> str:
    if not (_config.get("api_key") and _config.get("model")):
        return "MOCK"
    if _real_face_ready():
        return "REAL-FACE (asset library)"
    return "INLINE (real faces will be rejected)"


def _real_face_ready() -> bool:
    from core import creds
    return creds.is_complete(_config.get("assets", {})) and tos_store.is_configured(_config.get("tos", {}))


def _asset_group_id() -> str:
    """One shared virtual-avatar asset group for the whole booth, created lazily."""
    if _config.get("group_id"):
        return _config["group_id"]
    with _group_lock:
        if _config.get("group_id"):
            return _config["group_id"]
        name = _config.get("group_name", "seedance-booth")
        gid = assets.create_asset_group(_config["assets"], name, "Seedance booth guests")
        _config["group_id"] = gid
        log.info("created shared asset group %s (%s)", gid, name)
        return gid


def enqueue(job: dict) -> None:
    """job: {ticket, film_key, portrait (jpeg bytes), name, email}"""
    storage.update_lead(job["ticket"], status="queued")
    _queue.put(job)
    log.info("queued %s (%s)", job["ticket"], job["film_key"])


def queue_depth() -> int:
    return _queue.qsize()


def regenerate(ticket: str) -> bool:
    """Re-run a lead's film reusing its saved photo/asset — no re-upload.
    Returns False if the lead has no reusable photo (e.g. old inline capture)."""
    lead = next((x for x in storage.load_leads() if x["ticket"] == ticket), None)
    if not lead or not (lead.get("asset_id") or lead.get("photo_url")):
        return False
    job = {"ticket": ticket, "film_key": lead["film"],
           "name": lead.get("name", ""), "email": lead.get("email", ""),
           "costar": lead.get("costar", "")}
    if lead.get("asset_id"):
        job["asset_id"] = lead["asset_id"]
    if lead.get("photo_url"):
        job["photo_url"] = lead["photo_url"]
    enqueue(job)
    return True


def _dispatch() -> None:
    while True:
        job = _queue.get()
        threading.Thread(target=_process, args=(job,), name=f"pp-{job['ticket']}", daemon=True).start()


def _process(job: dict) -> None:
    ticket = job["ticket"]
    with _semaphore:
        try:
            storage.update_lead(ticket, status="rendering")
            live = bool(_config.get("api_key") and _config.get("model"))
            video_ref = _render_live(job) if live else _render_mock(job)
            storage.add_gallery_entry({
                "ticket": ticket,
                "name": job.get("name", ""),
                "film": job["film_key"],
                "video": video_ref,
                "created": datetime.now().isoformat(timespec="seconds"),
            })
            storage.update_lead(ticket, status="done", video_path=video_ref)
            log.info("premiered %s -> %s", ticket, video_ref)
            _maybe_email(job, video_ref)
        except seedance.RealFaceRejected as exc:
            log.warning("real-face rejected for %s", ticket)
            storage.update_lead(
                ticket, status="rejected_face",
                task_id=job.get("task_id", ""),
                video_path=f"REJECTED: {str(exc)[:200]}",
            )
        except Exception as exc:  # keep the worker alive whatever happens
            log.exception("render failed for %s", ticket)
            storage.update_lead(
                ticket, status="failed",
                task_id=job.get("task_id", ""),
                video_path=f"ERROR: {str(exc)[:200]}",
            )


def _prepare_asset(job: dict) -> str:
    """Real-face path → asset:// URI. Reuse order (cheapest first):
    job asset_id → guest-photo cached asset_id → guest/job TOS url → upload bytes.
    Caches the new asset_id onto the guest photo so regeneration is free."""
    if job.get("asset_id"):
        return assets.asset_uri(job["asset_id"])
    cred = _config["assets"]
    photo_id = job.get("photo_id")
    url = job.get("photo_url")

    if photo_id:
        entry = storage.get_guest_photo(photo_id)
        if entry and entry.get("asset_id"):                # already registered — reuse
            job["asset_id"] = entry["asset_id"]
            storage.update_lead(job["ticket"], asset_id=entry["asset_id"])
            return assets.asset_uri(entry["asset_id"])
        if entry and entry.get("tos_url"):
            url = entry["tos_url"]

    if not url:                                            # fallback: host the raw bytes
        _, url = tos_store.upload_image(
            _config["tos"], job["portrait"],
            prefix=_config.get("event_prefix", "premiere"), cred=cred,
        )
    storage.update_lead(job["ticket"], photo_url=url)

    asset_id = assets.create_asset(cred, _asset_group_id(), url, name=job["ticket"])
    assets.wait_asset_active(cred, asset_id)
    job["asset_id"] = asset_id
    storage.update_lead(job["ticket"], asset_id=asset_id)
    if photo_id:
        storage.update_guest_photo(photo_id, asset_id=asset_id)  # cache for reuse
    log.info("%s asset ready %s", job["ticket"], asset_id)
    return assets.asset_uri(asset_id)


def _run_task(job: dict, prompt: str, *, image_refs, video_ref=None, dest: Path):
    """Submit one 15s generation, wait, download to dest. Returns dest."""
    spec = films.FIXED_SPEC
    task_id = seedance.create_task(
        _config["api_key"], _config["model"], prompt, None,
        image_refs=image_refs, video_ref=video_ref,
        ratio=spec["ratio"], duration=spec["duration"], resolution=spec.get("resolution"),
        generate_audio=True, watermark=False,
    )
    storage.update_lead(job["ticket"], task_id=task_id)
    log.info("%s -> task %s", job["ticket"], task_id)
    result = seedance.wait_for_task(
        _config["api_key"], task_id,
        on_status=lambda s: log.info("%s task %s: %s", job["ticket"], task_id, s),
    )
    seedance.download(seedance.video_url(result), dest)
    return dest


def _render_live(job: dict) -> str:
    asset_uri = _prepare_asset(job) if _real_face_ready() else None
    gender = job.get("costar", "")
    duo = films.duo_prompts(job["film_key"], gender) if gender in ("woman", "man") else None
    if asset_uri and duo:
        return _render_duo(job, asset_uri, duo)
    return _render_solo(job, asset_uri)


def _render_solo(job: dict, asset_uri: str | None) -> str:
    film = films.FILM_BY_KEY[job["film_key"]]
    storage.ensure_dirs()
    dest = storage.GALLERY_DIR / f"{job['ticket']}.mp4"
    if not asset_uri:  # inline fallback path (no asset creds)
        return _run_task_inline(job, film["prompt"], dest)
    _run_task(job, film["prompt"], image_refs=[asset_uri], dest=dest)
    return f"gallery/{dest.name}"


def _run_task_inline(job: dict, prompt: str, dest: Path) -> str:
    spec = films.FIXED_SPEC
    task_id = seedance.create_task(
        _config["api_key"], _config["model"], prompt, job.get("portrait"),
        ratio=spec["ratio"], duration=spec["duration"], resolution=spec.get("resolution"),
        generate_audio=True, watermark=False,
    )
    storage.update_lead(job["ticket"], task_id=task_id)
    result = seedance.wait_for_task(_config["api_key"], task_id,
                                    on_status=lambda s: log.info("%s %s", job["ticket"], s))
    seedance.download(seedance.video_url(result), dest)
    return f"gallery/{dest.name}"


def _render_duo(job: dict, visitor_uri: str, duo) -> str:
    """30s render: visitor (Image 1) + an AI companion described in the prompt.
    Seq A introduces both; seq B is generated FROM seq A's video (extend) so the
    companion and setting stay consistent; then the two 15s halves are stitched."""
    from core import stitch
    seq_a_prompt, seq_b_prompt = duo
    refs = [visitor_uri]
    storage.ensure_dirs()
    tmp_a = storage.GALLERY_DIR / f"{job['ticket']}_a.mp4"
    tmp_b = storage.GALLERY_DIR / f"{job['ticket']}_b.mp4"
    final = storage.GALLERY_DIR / f"{job['ticket']}.mp4"

    log.info("%s duo seq A", job["ticket"])
    _run_task(job, seq_a_prompt, image_refs=refs, dest=tmp_a)
    # host seq A so seq B can extend from it (reference_video)
    _, seq_a_url = tos_store.upload_video(
        _config["tos"], tmp_a.read_bytes(),
        prefix=_config.get("event_prefix", "premiere"), cred=_config["assets"],
    )
    log.info("%s duo seq B (extends seq A)", job["ticket"])
    _run_task(job, seq_b_prompt, image_refs=refs, video_ref=seq_a_url, dest=tmp_b)

    stitch.concat([tmp_a, tmp_b], final)
    tmp_a.unlink(missing_ok=True)
    tmp_b.unlink(missing_ok=True)
    log.info("%s duo stitched -> %s", job["ticket"], final.name)
    return f"gallery/{final.name}"


def _render_mock(job: dict) -> str:
    log.info("MOCK render for %s (no ARK credentials)", job["ticket"])
    time.sleep(MOCK_RENDER_SECONDS)
    return MOCK_VIDEO_URL


def _email_video_ref(video_ref: str) -> str:
    """Prefer a public TOS URL for the email (a link is reliable behind the
    proxy and dodges attachment-size limits). Falls back to the local path."""
    if video_ref.startswith("http") or not tos_store.is_configured(_config.get("tos", {})):
        return video_ref
    try:
        path = storage.GALLERY_DIR / Path(video_ref).name
        _, url = tos_store.upload_video(_config["tos"], path.read_bytes(), cred=_config["assets"])
        return url
    except Exception:
        log.exception("video TOS upload failed; emailing local attachment instead")
        return video_ref


def _maybe_email(job: dict, video_ref: str) -> None:
    if not job.get("email"):
        return
    try:
        sent = emailer.send_premiere(
            _config.get("smtp", {}),
            name=job.get("name", ""),
            email=job["email"],
            film_key=job["film_key"],
            ticket=job["ticket"],
            video_ref=_email_video_ref(video_ref),
        )
        storage.update_lead(job["ticket"], email_sent="yes" if sent else "mock")
    except Exception:
        log.exception("email failed for %s", job["ticket"])
        storage.update_lead(job["ticket"], email_sent="failed")
