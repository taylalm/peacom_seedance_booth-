"""Populate asset-library / TOS secrets without echoing them.

Run:  .venv/bin/python scripts/fill_secrets.py
Each prompt is hidden (getpass). Press Enter to skip a field (keeps current).
"""
import getpass
import re
from pathlib import Path

SECRETS = Path(__file__).resolve().parent.parent / ".streamlit" / "secrets.toml"

# (toml key, prompt, whether it lives under [tos])
FIELDS = [
    ("ARK_AK", "IAM Access Key ID (ARK_AK)", False),
    ("ARK_SK", "IAM Secret Access Key (ARK_SK)", False),
    ("bucket", "TOS bucket name", True),
    ("ak", "TOS access key (Enter to reuse ARK_AK)", True),
    ("sk", "TOS secret key (Enter to reuse ARK_SK)", True),
]


def set_key(text: str, key: str, value: str, in_tos: bool) -> str:
    lines = text.split("\n")
    in_section = not in_tos  # top-level keys are before any [table]
    for i, ln in enumerate(lines):
        if ln.strip().startswith("["):
            in_section = ln.strip() == "[tos]" if in_tos else False
        if in_section and re.match(rf'^\s*{re.escape(key)}\s*=', ln):
            lines[i] = f'{key} = "{value}"'
            return "\n".join(lines)
    return text  # key not found — leave as-is


def main():
    text = SECRETS.read_text()
    for key, prompt, in_tos in FIELDS:
        val = getpass.getpass(f"{prompt}: ").strip()
        if val:
            text = set_key(text, key, val, in_tos)
            print(f"  set {'[tos].' if in_tos else ''}{key} ({len(val)} chars)")
        else:
            print(f"  skipped {key}")
    SECRETS.write_text(text)
    print("done — secrets.toml updated (values not shown).")


if __name__ == "__main__":
    main()
