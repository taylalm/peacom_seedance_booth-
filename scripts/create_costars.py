"""Create the two preset co-star assets (one woman, one man) for 30s duo videos.

Run once, with fresh creds, from the app folder:
    source byteplus_creds.sh && .venv/bin/python scripts/create_costars.py

It uploads two co-star face photos to TOS, registers them in the asset library,
waits until Active, and prints the two asset IDs. Put those into secrets:
    COSTAR_FEMALE_ASSET = "asset-..."
    COSTAR_MALE_ASSET   = "asset-..."
(locally in secrets.toml AND in each app's Streamlit Cloud secrets).

Provide the two source photos as command-line paths, or drop them at
scripts/costar_female.jpg and scripts/costar_male.jpg (clear, front-facing,
>=300px, single face). Use consented / licensed stock photos.
"""
import io
import sys
import tomllib
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP))
from core import netfix; netfix.ensure_ca_bundle()
from core import assets, creds, tos_store
from PIL import Image, ImageOps

secrets = tomllib.loads((APP / ".streamlit/secrets.toml").read_text())
cred = creds.resolve(secrets); cred["project"] = secrets.get("ARK_PROJECT", "default")
tos_cfg = dict(secrets["tos"])

sources = {
    "female": Path(sys.argv[1]) if len(sys.argv) > 1 else APP / "scripts/costar_female.jpg",
    "male": Path(sys.argv[2]) if len(sys.argv) > 2 else APP / "scripts/costar_male.jpg",
}

gid = assets.create_asset_group(cred, "costars", "Preset co-stars for 30s duo videos")
print("co-star group:", gid, flush=True)

out = {}
for gender, path in sources.items():
    if not path.exists():
        print(f"  ⚠️  {gender}: {path} not found — skipping"); continue
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
    _, url = tos_store.upload_image(tos_cfg, buf.getvalue(), prefix="costars", cred=cred)
    aid = assets.create_asset(cred, gid, url, name=f"costar-{gender}")
    assets.wait_asset_active(cred, aid)
    out[gender] = aid
    print(f"  ✅ {gender}: {aid}", flush=True)

print("\n--- add these to secrets (locally + both Cloud apps) ---")
print(f'COSTAR_FEMALE_ASSET = "{out.get("female", "")}"')
print(f'COSTAR_MALE_ASSET = "{out.get("male", "")}"')
