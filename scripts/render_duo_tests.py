"""Render one 30s TWO-CHARACTER test video per theme using test_face.jpg.

Mirrors worker._render_duo: face -> virtual-avatar asset; seq A (visitor + AI
companion); host seq A on TOS; seq B extends from seq A (reference_video) so the
companion + world stay consistent; ffmpeg-concat the two 15s halves -> 30s;
upload final to TOS; print watch link.

Run:  .venv/bin/python scripts/render_duo_tests.py [theme_key ...]
Test face is male, so the AI companion gender is 'woman'.
"""

import sys
import tomllib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core import netfix, creds, films, assets, seedance, tos_store, stitch  # noqa: E402

netfix.ensure_ca_bundle()

SECRETS = tomllib.loads((ROOT / ".streamlit" / "secrets.toml").read_text())
_assets = creds.resolve(SECRETS)
_assets["project"] = SECRETS.get("ARK_PROJECT", "default")
CFG = {
    "api_key": SECRETS.get("ARK_API_KEY", ""),
    "model": SECRETS.get("ARK_MODEL_EP", ""),
    "assets": _assets,
    "tos": dict(SECRETS.get("tos", {})),
    "event_prefix": SECRETS.get("EVENT_PREFIX", "premiere"),
    "group_name": SECRETS.get("ASSET_GROUP_NAME", "seedance-booth"),
}
import os
COSTAR = os.environ.get("TEST_COSTAR", "woman")  # co-star gender (opposite of face)
FACE = Path(os.environ.get("TEST_FACE", str(ROOT / "test_face.jpg")))
OUT = ROOT / "scratch_renders"
OUT.mkdir(exist_ok=True)


def _run(key, prompt, image_refs, video_ref, dest):
    spec = films.FIXED_SPEC
    task_id = seedance.create_task(
        CFG["api_key"], CFG["model"], prompt, None,
        image_refs=image_refs, video_ref=video_ref,
        ratio=spec["ratio"], duration=spec["duration"], resolution=spec.get("resolution"),
        generate_audio=True, watermark=False,
    )
    print(f"[{key}] task {task_id}")
    result = seedance.wait_for_task(CFG["api_key"], task_id,
                                    on_status=lambda s: print(f"[{key}] {s}"))
    seedance.download(seedance.video_url(result), dest)
    return dest


def prepare_face_asset() -> str:
    cred = CFG["assets"]
    _, url = tos_store.upload_image(CFG["tos"], FACE.read_bytes(),
                                    prefix=CFG["event_prefix"], cred=cred)
    gid = assets.create_asset_group(cred, CFG["group_name"], "duo test faces")
    aid = assets.create_asset(cred, gid, url, name="duo-test-face")
    assets.wait_asset_active(cred, aid)
    print(f"[face] asset ready {aid}")
    return assets.asset_uri(aid)


def render_duo(film: dict, asset_uri: str) -> tuple[str, str]:
    key = film["key"]
    seq_a, seq_b = films.duo_prompts(key, COSTAR)
    tmp_a = OUT / f"{key}_a.mp4"
    tmp_b = OUT / f"{key}_b.mp4"
    final = OUT / f"{key}_duo.mp4"

    print(f"[{key}] seq A")
    _run(key, seq_a, [asset_uri], None, tmp_a)
    _, seq_a_url = tos_store.upload_video(CFG["tos"], tmp_a.read_bytes(),
                                          prefix=CFG["event_prefix"], cred=CFG["assets"])
    print(f"[{key}] seq B (extends A)")
    _run(key, seq_b, [asset_uri], seq_a_url, tmp_b)

    stitch.concat([tmp_a, tmp_b], final)
    branded = OUT / f"{key}_duo_branded.mp4"
    stitch.watermark(final, branded)
    branded.replace(final)
    tmp_a.unlink(missing_ok=True)
    tmp_b.unlink(missing_ok=True)
    _, url = tos_store.upload_video(CFG["tos"], final.read_bytes(),
                                    prefix=CFG["event_prefix"], cred=CFG["assets"])
    print(f"[{key}] DONE -> {url}")
    return key, url


def main():
    wanted = sys.argv[1:]
    catalog = [f for f in films.FILMS if not wanted or f["key"] in wanted]
    print("Rendering DUO:", [f["key"] for f in catalog])
    asset_uri = prepare_face_asset()
    results = {}
    # 3 themes at a time; each theme itself runs its 2 seqs sequentially (B extends A)
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(render_duo, f, asset_uri): f["key"] for f in catalog}
        for fut in as_completed(futs):
            key = futs[fut]
            try:
                k, url = fut.result()
                results[k] = url
            except Exception as exc:
                results[key] = f"FAILED: {exc}"
                print(f"[{key}] FAILED: {exc}")
    print("\n===== DUO WATCH LINKS =====")
    for f in catalog:
        print(f"{f['no']} {f['title_en']:22} {results.get(f['key'])}")


if __name__ == "__main__":
    main()
