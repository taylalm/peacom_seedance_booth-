"""Render one SOLO 15s test video per theme using test_face.jpg.

Uses the same pipeline the booth uses: upload face -> virtual-avatar asset ->
generate each theme's solo prompt -> download -> host on TOS -> print watch link.

Run:  .venv/bin/python scripts/render_theme_tests.py [theme_key ...]
"""

import sys
import tomllib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core import netfix, creds, films, assets, seedance, tos_store  # noqa: E402

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

FACE = ROOT / "test_face.jpg"
OUT = ROOT / "scratch_renders"
OUT.mkdir(exist_ok=True)


def prepare_face_asset() -> str:
    """Upload the test face once, register as a virtual-avatar asset, reuse for all."""
    cred = CFG["assets"]
    _, url = tos_store.upload_image(CFG["tos"], FACE.read_bytes(),
                                    prefix=CFG["event_prefix"], cred=cred)
    gid = assets.create_asset_group(cred, CFG["group_name"], "theme test faces")
    aid = assets.create_asset(cred, gid, url, name="theme-test-face")
    assets.wait_asset_active(cred, aid)
    print(f"[face] asset ready {aid}")
    return assets.asset_uri(aid)


def render(film: dict, asset_uri: str) -> tuple[str, str]:
    key = film["key"]
    spec = films.FIXED_SPEC
    task_id = seedance.create_task(
        CFG["api_key"], CFG["model"], film["prompt"], None,
        image_refs=[asset_uri], ratio=spec["ratio"], duration=spec["duration"],
        resolution=spec.get("resolution"), generate_audio=True, watermark=False,
    )
    print(f"[{key}] task {task_id}")
    result = seedance.wait_for_task(CFG["api_key"], task_id,
                                    on_status=lambda s: print(f"[{key}] {s}"))
    dest = OUT / f"{key}.mp4"
    seedance.download(seedance.video_url(result), dest)
    _, url = tos_store.upload_video(CFG["tos"], dest.read_bytes(),
                                    prefix=CFG["event_prefix"], cred=CFG["assets"])
    print(f"[{key}] DONE -> {url}")
    return key, url


def main():
    wanted = sys.argv[1:]
    catalog = [f for f in films.FILMS if not wanted or f["key"] in wanted]
    print("Rendering:", [f["key"] for f in catalog])
    asset_uri = prepare_face_asset()
    results = {}
    # 3 at a time — ModelArk's concurrent-task ceiling
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(render, f, asset_uri): f["key"] for f in catalog}
        for fut in as_completed(futs):
            key = futs[fut]
            try:
                k, url = fut.result()
                results[k] = url
            except Exception as exc:
                results[key] = f"FAILED: {exc}"
                print(f"[{key}] FAILED: {exc}")
    print("\n===== WATCH LINKS =====")
    for f in catalog:
        print(f"{f['no']} {f['title_en']:22} {results.get(f['key'])}")


if __name__ == "__main__":
    main()
