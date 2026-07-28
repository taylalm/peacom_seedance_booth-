"""Resolve BytePlus asset-library credentials.

Temporary (STS) credentials expire and carry a session token, so environment
variables you can re-source win over static secrets. Order of precedence:

  1. environment  — BYTEPLUS_ACCESS_KEY / BYTEPLUS_SECRET_KEY / BYTEPLUS_SESSION_TOKEN
  2. secrets.toml — ARK_AK / ARK_SK / ARK_SESSION_TOKEN

Use an env-file (byteplus_creds.sh, gitignored): source it before launching
Streamlit and the app picks the creds up automatically.
"""

import os


def resolve(secrets: dict | None = None) -> dict:
    s = secrets or {}

    def pick(env_key: str, secret_key: str) -> str:
        return (os.environ.get(env_key) or s.get(secret_key) or "").strip()

    return {
        "ak": pick("BYTEPLUS_ACCESS_KEY", "ARK_AK"),
        "sk": pick("BYTEPLUS_SECRET_KEY", "ARK_SK"),
        "session_token": pick("BYTEPLUS_SESSION_TOKEN", "ARK_SESSION_TOKEN"),
        "region": (os.environ.get("BYTEPLUS_REGION") or s.get("ARK_REGION") or "ap-southeast-1").strip(),
        "project": (s.get("ARK_PROJECT") or "default").strip(),
    }


def is_complete(cfg: dict) -> bool:
    return bool(cfg.get("ak") and cfg.get("sk"))
