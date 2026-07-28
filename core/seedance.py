"""Seedance 2.0 client — BytePlus ModelArk content-generation tasks API.

Plain REST via requests: create task (prompt + reference portrait), poll
until it settles, download the finished MP4 (result URLs are temporary).
"""

import base64
import time

import requests

BASE_URL = "https://ark.ap-southeast.bytepluses.com/api/v3"
TASKS_URL = f"{BASE_URL}/contents/generations/tasks"

TERMINAL_OK = {"succeeded"}
TERMINAL_BAD = {"failed", "cancelled", "expired"}


class SeedanceError(RuntimeError):
    pass


class RealFaceRejected(SeedanceError):
    """ModelArk refused the input as containing a real person (needs the
    real-person entitlement enabled on the account/endpoint)."""


def _headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}


def create_task(
    api_key: str,
    model: str,
    prompt: str,
    portrait_jpeg: bytes | None = None,
    *,
    asset_uri: str | None = None,
    image_refs: list[str] | None = None,
    video_ref: str | None = None,
    ratio: str = "9:16",
    duration: int = 15,
    resolution: str | None = None,
    generate_audio: bool = True,
    watermark: bool = False,
) -> str:
    """Submit a generation task; returns the task id.

    Image references become "Image 1", "Image 2", … in order (reference the
    person in Image N in the prompt):
      - `image_refs`: list of asset:// URIs or public URLs (multi-character)
      - `asset_uri`: single asset:// (back-compat, same as image_refs=[asset_uri])
      - `portrait_jpeg`: inline base64 (rejected for real people)
    `video_ref` adds a reference_video (public URL) — used to continue a story
    across two stitched 15s halves for better continuity."""
    content: list[dict] = [{"type": "text", "text": prompt}]
    refs = list(image_refs) if image_refs else ([asset_uri] if asset_uri else [])
    for ref in refs:
        content.append({
            "type": "image_url",
            "image_url": {"url": ref},
            "role": "reference_image",
        })
    if not refs and portrait_jpeg:
        b64 = base64.b64encode(portrait_jpeg).decode()
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
            "role": "reference_image",
        })
    if video_ref:
        content.append({
            "type": "video_url",
            "video_url": {"url": video_ref},
            "role": "reference_video",
        })
    payload = {
        "model": model,
        "content": content,
        "generate_audio": generate_audio,
        "ratio": ratio,
        "duration": duration,
        "watermark": watermark,
    }
    if resolution:
        payload["resolution"] = resolution

    resp = requests.post(TASKS_URL, json=payload, headers=_headers(api_key), timeout=60)
    if resp.status_code != 200:
        if "SensitiveContentDetected" in resp.text or "may contain real person" in resp.text:
            raise RealFaceRejected(
                "ModelArk rejected the photo as a real person. Enable real-person "
                "generation on the account/endpoint. Detail: " + resp.text[:300]
            )
        raise SeedanceError(f"create_task HTTP {resp.status_code}: {resp.text[:500]}")
    task_id = resp.json().get("id")
    if not task_id:
        raise SeedanceError(f"create_task: no task id in response: {resp.text[:500]}")
    return task_id


# transient network faults that shouldn't abort a 15-minute render — retry through them
_TRANSIENT = (requests.exceptions.ConnectionError, requests.exceptions.Timeout,
              requests.exceptions.ChunkedEncodingError)


def get_task(api_key: str, task_id: str, *, retries: int = 5, backoff: int = 6) -> dict:
    last = None
    for attempt in range(retries):
        try:
            resp = requests.get(f"{TASKS_URL}/{task_id}", headers=_headers(api_key), timeout=30)
            if resp.status_code != 200:
                raise SeedanceError(f"get_task HTTP {resp.status_code}: {resp.text[:500]}")
            return resp.json()
        except _TRANSIENT as exc:  # network blip — wait and retry, don't lose the task
            last = exc
            time.sleep(backoff * (attempt + 1))
    raise SeedanceError(f"get_task {task_id} failed after {retries} retries: {last}")


def wait_for_task(
    api_key: str,
    task_id: str,
    *,
    poll_seconds: int = 10,
    timeout_seconds: int = 1500,
    on_status=None,
) -> dict:
    """Poll until the task settles; returns the final task payload."""
    deadline = time.monotonic() + timeout_seconds
    while True:
        data = get_task(api_key, task_id)
        status = data.get("status", "")
        if on_status:
            on_status(status)
        if status in TERMINAL_OK:
            return data
        if status in TERMINAL_BAD:
            err = data.get("error") or {}
            raise SeedanceError(
                f"task {task_id} {status}: {err.get('code', '')} {err.get('message', '')}".strip()
            )
        if time.monotonic() > deadline:
            raise SeedanceError(f"task {task_id} timed out after {timeout_seconds}s (last status: {status})")
        time.sleep(poll_seconds)


def video_url(task: dict) -> str:
    url = (task.get("content") or {}).get("video_url")
    if not url:
        raise SeedanceError(f"no video_url in task result: {str(task)[:500]}")
    return url


def download(url: str, dest_path, *, retries: int = 4, backoff: int = 5) -> None:
    last = None
    for attempt in range(retries):
        try:
            with requests.get(url, stream=True, timeout=120) as resp:
                resp.raise_for_status()
                with open(dest_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=1 << 16):
                        f.write(chunk)
            return
        except _TRANSIENT as exc:  # blip mid-download — retry the whole fetch
            last = exc
            time.sleep(backoff * (attempt + 1))
    raise SeedanceError(f"download failed after {retries} retries: {last}")
