"""Refresh the expiring STS creds inside .streamlit/secrets_cloud.toml.

The Streamlit Cloud secrets need ARK_AK / ARK_SK / ARK_SESSION_TOKEN inline
(Cloud can't source byteplus_creds.sh). This splices fresh values into the FULL
cloud block so you can copy the whole file into Streamlit Cloud unchanged.

Sources, in order:
  1. env BYTEPLUS_ACCESS_KEY / BYTEPLUS_SECRET_KEY / BYTEPLUS_SESSION_TOKEN
     (i.e. `source byteplus_creds.sh` first) — zero retyping.
  2. otherwise a hidden getpass prompt per field (Enter = keep current).

Values are never printed — only their lengths. Everything else in the file is
left byte-for-byte untouched.

Run:  source byteplus_creds.sh && .venv/bin/python scripts/sync_cloud_secrets.py
"""
import getpass
import os
import re
from pathlib import Path

CLOUD = Path(__file__).resolve().parent.parent / ".streamlit" / "secrets_cloud.toml"

# toml key in secrets_cloud.toml  <-  env var from byteplus_creds.sh
FIELDS = [
    ("ARK_AK", "BYTEPLUS_ACCESS_KEY", "IAM Access Key ID"),
    ("ARK_SK", "BYTEPLUS_SECRET_KEY", "IAM Secret Access Key"),
    ("ARK_SESSION_TOKEN", "BYTEPLUS_SESSION_TOKEN", "STS session token"),
]


def set_top_level_key(text: str, key: str, value: str) -> str:
    """Replace a top-level `key = "..."` line (before any [table]). Returns text."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip().startswith("["):
            break  # only touch keys above the first table
        if re.match(rf'^\s*{re.escape(key)}\s*=', ln):
            lines[i] = f'{key} = "{value}"'
            return "\n".join(lines)
    raise SystemExit(f"key {key} not found in top-level section of {CLOUD.name}")


def main():
    if not CLOUD.exists():
        raise SystemExit(f"missing {CLOUD}")
    text = CLOUD.read_text()
    changed = 0
    for toml_key, env_var, label in FIELDS:
        val = (os.environ.get(env_var) or "").strip()
        src = f"env {env_var}"
        if not val:
            val = getpass.getpass(f"{label} ({toml_key}) [Enter=keep]: ").strip()
            src = "typed"
        if not val:
            print(f"  keep   {toml_key}")
            continue
        text = set_top_level_key(text, toml_key, val)
        print(f"  set    {toml_key}  ({len(val)} chars, from {src})")
        changed += 1
    CLOUD.write_text(text)
    print(f"done — updated {changed} field(s) in {CLOUD.name} (values not shown).")
    print("Next: copy the ENTIRE file below into Streamlit Cloud → Settings → Secrets:")
    print(f"  {CLOUD}")


if __name__ == "__main__":
    main()
