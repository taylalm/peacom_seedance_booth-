"""Premiere email — delivers the finished film as a 'premiere invitation'.

Bilingual TH/EN HTML. Attaches the MP4 when it's a local file under the size
cap, otherwise links to it. Mock mode (no SMTP secrets) just logs, so the rest
of the pipeline runs without a mail account.
"""

import logging
import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

from core import films

log = logging.getLogger("premiere.emailer")

MAX_ATTACH_MB = 18
ROOT = Path(__file__).resolve().parent.parent


def _html(name: str, film: dict, ticket: str, link: str | None) -> str:
    first = name.split()[0] if name.strip() else "Star"
    watch = (
        f'<a href="{link}" style="color:#C8321E;font-weight:bold">▶ Watch your film</a>'
        if link else "attached to this email"
    )
    return f"""\
<div style="background:#F4E9D8;padding:28px;font-family:Georgia,serif;color:#2B2320">
  <div style="max-width:560px;margin:auto;background:#FFFDF7;border:3px solid #2B2320;border-radius:16px;overflow:hidden">
    <div style="background:#2B2320;color:#F6C55C;padding:18px 24px">
      <div style="letter-spacing:.2em;font-size:12px">🎬 PREMIERE PICTURES</div>
      <div style="font-size:22px;margin-top:4px">YOUR PREMIERE NIGHT</div>
    </div>
    <div style="padding:24px">
      <p style="font-size:18px">Hello <b>{first}</b> 🌟</p>
      <p>Your film has premiered!</p>
      <div style="background:#F4E9D8;border:2px dashed #C8321E;border-radius:12px;padding:16px;text-align:center;margin:18px 0">
        <div style="font-size:20px;font-weight:bold;letter-spacing:.06em">{film['title_en']}</div>
        <div style="color:#C8321E;font-size:18px">{film['title_th']}</div>
        <div style="font-style:italic;color:#55483F;margin-top:6px">{film['logline_en']}</div>
        <div style="margin-top:10px;font-size:13px;letter-spacing:.12em;color:#1E5A5A">TICKET {ticket}</div>
      </div>
      <p style="text-align:center;font-size:16px">{watch}</p>
      <p style="font-size:12px;color:#8B7E6E;margin-top:24px;text-align:center">
        Thank you for starring with Premiere Pictures<br>
        Powered by Seedance 2.0 on BytePlus ModelArk · EST. 2026
      </p>
    </div>
  </div>
</div>"""


def send_premiere(cfg: dict, *, name: str, email: str, film_key: str, ticket: str, video_ref: str) -> bool:
    """Send the premiere email. cfg: host, port, user, app_password, sender.
    Returns True if actually sent, False in mock mode. Raises on SMTP failure."""
    film = films.FILM_BY_KEY[film_key]

    local = ROOT / video_ref if not video_ref.startswith("http") else None
    link = video_ref if video_ref.startswith("http") else None
    attach = local if (local and local.exists() and local.stat().st_size <= MAX_ATTACH_MB * 1e6) else None
    if local and not attach and not link:
        link = None  # file too big and no URL — email still goes with neither; body says attached

    msg = EmailMessage()
    msg["Subject"] = f"🎬 {film['title_en']} — Your Premiere Pictures premiere"
    msg["From"] = cfg.get("sender") or cfg.get("user", "")
    msg["To"] = email
    msg.set_content(
        f"Your Premiere Pictures film '{film['title_en']}' ({ticket}) has premiered! "
        f"{'Watch: ' + link if link else 'See the attached video.'}"
    )
    msg.add_alternative(_html(name, film, ticket, link), subtype="html")
    if attach:
        msg.add_attachment(
            attach.read_bytes(), maintype="video", subtype="mp4", filename=f"{ticket}.mp4"
        )

    if not (cfg.get("host") and cfg.get("user") and cfg.get("app_password")):
        log.info("MOCK email to %s for %s (no SMTP configured)", email, ticket)
        return False

    ca = os.environ.get("REQUESTS_CA_BUNDLE")  # trust corporate proxy's SMTP TLS (see netfix)
    ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    app_password = str(cfg["app_password"]).replace(" ", "")  # Gmail shows it spaced
    with smtplib.SMTP(cfg["host"], int(cfg.get("port", 587)), timeout=60) as s:
        s.ehlo()                    # explicit EHLO around STARTTLS — required behind
        s.starttls(context=ctx)     # the corporate proxy (implicit handling drops it)
        s.ehlo()
        s.login(cfg["user"], app_password)
        s.send_message(msg)
    log.info("emailed %s premiere to %s", ticket, email)
    return True
