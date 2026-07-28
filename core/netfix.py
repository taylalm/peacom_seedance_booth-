"""Corporate-TLS survival kit.

On networks that intercept HTTPS (e.g. a corporate proxy), Python's bundled
certifi CA list doesn't trust the proxy's root, so `requests` fails with
SSLCertVerificationError even though the macOS keychain trusts it fine.

We export the system + admin keychain roots into a PEM (merged with certifi)
and point `requests` at it via REQUESTS_CA_BUNDLE. Harmless off corporate
networks — the extra roots are all legitimate CAs.
"""

import os
import subprocess
from pathlib import Path

import certifi

_BUNDLE = Path(__file__).resolve().parent.parent / ".streamlit" / "ca-bundle.pem"
_KEYCHAINS = [
    "/System/Library/Keychains/SystemRootCertificates.keychain",
    "/Library/Keychains/System.keychain",
]


def _build_bundle() -> bool:
    parts: list[str] = []
    for kc in _KEYCHAINS:
        if not os.path.exists(kc):
            continue
        try:
            out = subprocess.run(
                ["security", "find-certificate", "-a", "-p", kc],
                capture_output=True, text=True, timeout=30,
            )
            if out.stdout:
                parts.append(out.stdout)
        except Exception:
            pass
    if not parts:
        return False
    parts.append(Path(certifi.where()).read_text())
    _BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    _BUNDLE.write_text("\n".join(parts))
    return True


def ensure_ca_bundle() -> None:
    """Make `requests` trust the OS keychain. Idempotent; call once at startup."""
    if os.environ.get("REQUESTS_CA_BUNDLE"):
        return
    if not _BUNDLE.exists():
        if not _build_bundle():
            return  # not macOS / no keychain — leave certifi defaults in place
    os.environ["REQUESTS_CA_BUNDLE"] = str(_BUNDLE)
