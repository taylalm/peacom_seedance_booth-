"""The studio lobby + the four-scene wizard: casting → posters → ticket → production."""

import io
import re

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageOps

from core import films, guests, storage, ui, worker

# The only hard image constraint is the asset library (CreateAsset): width & height
# 300–6000px, aspect 0.4–2.5. Rather than reject small webcam captures, upscale them
# to a comfortable size so any device works.
TARGET_SHORT_SIDE = 640
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")

ui.inject()


def goto(scene: str):
    st.session_state["scene"] = scene
    st.rerun()


def reset_visitor():
    for key in ("portrait", "portrait_note", "guest_photo", "film_key", "ticket_no", "celebrated"):
        st.session_state.pop(key, None)
    st.session_state["scene"] = "lobby"


def has_photo() -> bool:
    """A photo is ready if we have local bytes or a selected saved (TOS) photo."""
    return bool(st.session_state.get("portrait") or st.session_state.get("guest_photo"))


def render_active_image():
    if st.session_state.get("portrait"):
        st.image(st.session_state["portrait"], use_container_width=True)
    elif st.session_state.get("guest_photo"):
        st.image(st.session_state["guest_photo"]["tos_url"], use_container_width=True)


def validated_portrait(file) -> tuple[bytes | None, str]:
    """Return (jpeg_bytes, note). Upright JPEG; upscales small captures so the
    asset library's 300px floor is always met — no rejection on size."""
    try:
        img = Image.open(file)
        img = ImageOps.exif_transpose(img).convert("RGB")
    except Exception:
        return None, "Couldn't read that file — please try another."
    w, h = img.size
    short = min(w, h)
    if short < TARGET_SHORT_SIDE:                       # upscale rather than reject
        scale = TARGET_SHORT_SIDE / short
        img = img.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
        w, h = img.size
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=92)
    return buf.getvalue(), f"{w}×{h} px"


# ---------------------------------------------------------------- scenes

def scene_lobby():
    ui.header()
    st.markdown(
        f"""
        <div class="mp-hero">
          <div class="mp-sunburst"></div>
          <div class="mp-hero-kicker">Premiere Pictures proudly presents</div>
          <h1>This one stars <span class="star">YOU</span>.</h1>
          <div class="mp-hero-sub">One photo. One blockbuster. You in the leading role.</div>
          {ui.hero_fan(films.FILMS)}
          <div class="mp-hero-tag">ONE SHOT · ONE EPIC · LIGHTS CAMERA YOU</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, c1, c2, c3, _ = st.columns([1, 3, 3, 3, 1])
    with c1:
        if st.button("🎬 ACTION — START", type="primary", use_container_width=True):
            goto("casting")
    with c2:
        if st.button("📸 GUEST GALLERY", use_container_width=True):
            st.switch_page("views/photo_gallery.py")
    with c3:
        if st.button("🎞 NOW SHOWING", use_container_width=True):
            st.switch_page("views/now_showing.py")

    st.markdown(
        """
        <p style="text-align:center; margin-top:1.2rem; color:#6B5C50">
        Take one photo, pick one film, and we'll cast you as the lead of a 15-second cinematic
        short — delivered straight to your inbox.
        </p>
        """,
        unsafe_allow_html=True,
    )
    ui.footer()


def prime_camera_permission():
    """Fire the browser's native camera-permission prompt as soon as Scene 1
    loads, instead of waiting for the visitor to interact with the camera
    widget. Once granted, the browser remembers it for this origin and
    st.camera_input starts immediately. Runs once per session."""
    if st.session_state.get("cam_primed"):
        return
    st.session_state["cam_primed"] = True
    components.html(
        """
        <script>
        (async () => {
          try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            stream.getTracks().forEach(t => t.stop());  // permission is all we need
          } catch (e) { /* denied or no camera — the widget shows its own hint */ }
        })();
        </script>
        """,
        height=0,
    )


def scene_casting():
    ui.header()
    ui.filmstrip(1)
    prime_camera_permission()
    left, right = st.columns([5, 4], gap="large")

    with left:
        ui.clap("SCENE 1 · CASTING CALL")
        st.markdown("## Send in your headshot.")
        st.markdown(
            """
            Lights, camera — we just need one clear, front-facing photo.
            It becomes the reference for your leading role in every shot.

            - 🎯 One person, centered
            - 💡 Good light on the face
            - 🖼 JPG · PNG · WEBP
            """,
            unsafe_allow_html=True,
        )

    with right:
        realface = guests.realface_available()

        def _accept(source):
            data, note = validated_portrait(source)
            if data is None:
                st.error(note)
                return
            st.session_state["portrait"] = data
            st.session_state["portrait_note"] = note
            st.session_state["cam_on"] = False  # capture done → shut the webcam off
            st.session_state.pop("guest_photo", None)
            if realface:  # host it now so it's reusable from the gallery
                try:
                    with st.spinner("Saving to the guest gallery…"):
                        st.session_state["guest_photo"] = guests.save_capture(data)
                except Exception as exc:
                    st.warning(f"Cloud save failed ({str(exc)[:80]}) — using local copy.")
            st.rerun()

        ready = has_photo()
        tab_cam, tab_up = st.tabs(["📸 SHOOT HERE", "🖼 UPLOAD"])
        with tab_cam:
            if ready:
                st.success("✓ Photo ready — camera is off. Use ↺ below to change it.")
            elif st.session_state.get("cam_on"):
                # camera_input holds the webcam live only while it's rendered
                shot = st.camera_input("Smile, superstar", key="cam")
                if shot is not None:
                    _accept(shot)
                if st.button("⏹ Turn camera off"):
                    st.session_state["cam_on"] = False
                    st.rerun()
            else:
                st.caption("The camera is off.")
                if st.button("📷 Turn camera on", type="primary"):
                    st.session_state["cam_on"] = True
                    st.rerun()
        with tab_up:
            if ready:
                st.success("✓ Photo ready. Use ↺ below to change it.")
            else:
                up = st.file_uploader(
                    "Drag a photo here, or browse", type=["jpg", "jpeg", "png", "webp"], key="upload"
                )
                if up is not None:
                    _accept(up)

        # reuse a previously-saved guest photo (real-face mode) — no retake needed
        if realface and not ready:
            saved = storage.load_guest_photos()
            if saved:
                with st.expander(f"📁 Or reuse a saved photo ({len(saved)})"):
                    cols = st.columns(3, gap="small")
                    for i, g in enumerate(saved[:9]):
                        with cols[i % 3]:
                            st.image(g["tos_url"], use_container_width=True)
                            if st.button("Use", key=f"useg-{g['id']}", use_container_width=True):
                                st.session_state["guest_photo"] = g
                                st.session_state.pop("portrait", None)
                                st.session_state.pop("portrait_note", None)
                                st.rerun()

        if ready:
            with st.container(key="casting-card"):
                st.markdown(
                    '<div class="mp-stamp">CAST ✓<small>LEADING ROLE</small></div>',
                    unsafe_allow_html=True,
                )
                render_active_image()
                cap = st.session_state.get("portrait_note") \
                    or (st.session_state.get("guest_photo") or {}).get("label", "saved photo")
                st.markdown(
                    f'<div class="mp-polaroid-caption">SUBJECT 01 · {cap}</div>',
                    unsafe_allow_html=True,
                )
            if st.button("↺ Retake / choose another"):
                for k in ("portrait", "portrait_note", "cam", "guest_photo"):
                    st.session_state.pop(k, None)
                st.session_state["cam_on"] = False
                st.rerun()

    st.divider()
    b1, _, b2 = st.columns([2, 4, 3])
    with b1:
        if st.button("← LOBBY"):
            goto("lobby")
    with b2:
        if st.button("PICK YOUR FILM →", type="primary", use_container_width=True, disabled=not has_photo()):
            goto("posters")


def scene_posters():
    ui.header()
    ui.filmstrip(2)
    ui.clap("SCENE 2 · THE POSTER WALL")
    st.markdown("## Which story is yours?")
    st.caption("Pick one. Each is a 15-second short (or 30 seconds with a co-star) — its own look, pace, and vibe.")

    selected = st.session_state.get("film_key")
    per_row = 3  # themes tiled 3 per row
    for start in range(0, len(films.FILMS), per_row):
        cols = st.columns(per_row, gap="medium")
        for col, film in zip(cols, films.FILMS[start:start + per_row]):
            with col:
                st.markdown(
                    ui.poster_html(film, selected=(film["key"] == selected), synopsis=True),
                    unsafe_allow_html=True,
                )
                label = "★ YOUR ROLE" if film["key"] == selected else "TAKE THIS ROLE"
                if st.button(
                    label,
                    key=f"pick-{film['key']}",
                    type="primary" if film["key"] == selected else "secondary",
                    use_container_width=True,
                ):
                    st.session_state["film_key"] = film["key"]
                    st.rerun()

    st.divider()
    b1, _, b2 = st.columns([2, 4, 3])
    with b1:
        if st.button("← BACK"):
            goto("casting")
    with b2:
        if st.button(
            "GET YOUR TICKET →",
            type="primary",
            use_container_width=True,
            disabled=selected is None,
        ):
            goto("ticket")


def scene_ticket():
    ui.header()
    ui.filmstrip(3)
    film = films.FILM_BY_KEY[st.session_state["film_key"]]

    left, right = st.columns([2, 3], gap="large")
    with left:
        ui.clap("SCENE 3 · PREMIERE TICKET")
        st.markdown("## Where do we send your film?")
        st.markdown(
            """
            When your film wraps, it goes straight to your inbox —
            no need to wait around at the screen. Enjoy the event.
            """,
            unsafe_allow_html=True,
        )
        st.markdown(ui.poster_html(film, selected=True), unsafe_allow_html=True)

    with right:
        with st.container(key="ticket-card"):
            st.markdown(
                f"""
                <div class="mp-ticket-head">
                  <span class="adm">ADMIT ONE · WORLD PREMIERE</span>
                  <span class="film">{film['title_en']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.form("ticket-form", border=False):
                name = st.text_input("Full name *", placeholder="e.g. Somchai Jaidee")
                company = st.text_input("Company *", placeholder="e.g. BytePlus")
                job = st.text_input("Job title *", placeholder="e.g. Marketing Manager")
                phone = st.text_input("Phone *", placeholder="+66 8x xxx xxxx")
                email = st.text_input("Email *", placeholder="you@example.com")
                costar_label = st.radio(
                    "Your video",
                    ["Solo — 15s", "With a co-star (woman) — 30s", "With a co-star (man) — 30s"],
                    help="A co-star makes a 30-second video where the two of you explore together and chat.",
                )
                consent = st.checkbox(
                    "I consent (PDPA) to my photo being used to generate this video, "
                    "shown in the event gallery, and emailed to me."
                )
                submitted = st.form_submit_button("🎬 ROLL CAMERA →", type="primary", use_container_width=True)

            if submitted:
                problems = []
                if not name.strip():
                    problems.append("name")
                if not company.strip():
                    problems.append("company")
                if not job.strip():
                    problems.append("job title")
                if not phone.strip():
                    problems.append("phone")
                if not EMAIL_RE.match(email.strip()):
                    problems.append("a valid email")
                if not consent:
                    problems.append("PDPA consent")
                if problems:
                    st.error("Still needed: " + " · ".join(problems))
                else:
                    ticket_no = storage.next_ticket()
                    guest = st.session_state.get("guest_photo") or {}
                    costar = {"With a co-star (woman) — 30s": "woman",
                              "With a co-star (man) — 30s": "man"}.get(costar_label, "")
                    storage.save_lead({
                        "ticket": ticket_no,
                        "name": name.strip(),
                        "company": company.strip(),
                        "job_title": job.strip(),
                        "phone": phone.strip(),
                        "email": email.strip(),
                        "film": film["key"],
                        "status": "queued",
                        "consent": "yes",
                        "email_sent": "no",
                        "photo_url": guest.get("tos_url", ""),
                        "asset_id": guest.get("asset_id", ""),
                        "costar": costar,
                    })
                    job_msg = {
                        "ticket": ticket_no,
                        "film_key": film["key"],
                        "name": name.strip(),
                        "email": email.strip(),
                        "costar": costar,
                    }
                    if st.session_state.get("portrait"):
                        job_msg["portrait"] = st.session_state["portrait"]
                    if guest:
                        job_msg["photo_id"] = guest.get("id")
                        job_msg["photo_url"] = guest.get("tos_url")
                        if guest.get("asset_id"):
                            job_msg["asset_id"] = guest["asset_id"]
                        storage.update_guest_photo(guest["id"], label=name.strip())
                    worker.enqueue(job_msg)
                    st.session_state["ticket_no"] = ticket_no
                    goto("production")

    st.divider()
    if st.button("← CHANGE FILM"):
        goto("posters")


def scene_production():
    ui.header()
    ui.filmstrip(4)
    film = films.FILM_BY_KEY[st.session_state["film_key"]]
    ticket_no = st.session_state.get("ticket_no", "PP-????")

    if not st.session_state.get("celebrated"):
        st.balloons()
        st.session_state["celebrated"] = True

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:.6rem">
          <div class="mp-clap">SCENE 4 · ACTION!</div>
          <h2 style="margin:.2rem 0">Your epic is in production 🎥</h2>
          <p style="font-style:italic; color:#55483F">Rolling now — sit back, superstar.</p>
        </div>
        <div class="mp-stub">
          <div class="meta">MAHA PICTURES · KEEP THIS STUB</div>
          <div class="no">{ticket_no}</div>
          <div style="font-family:'Chonburi',serif; font-size:1.15rem">{film['title_en']} · {film['title_th']}</div>
          <div class="divider"></div>
          <div class="meta">
            WORLD PREMIERE: THE NOW SHOWING SCREEN + YOUR INBOX · ~5 MIN
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _production_status(ticket_no)

    _, c1, c2, _ = st.columns([2, 3, 3, 2])
    with c1:
        if st.button("🎬 NEXT STAR", type="primary", use_container_width=True):
            reset_visitor()
            st.rerun()
    with c2:
        if st.button("NOW SHOWING", use_container_width=True):
            st.switch_page("views/now_showing.py")
    ui.footer()


_STATUS_COPY = {
    "queued": ("⏳", "#1E5A5A", "In the queue…"),
    "rendering": ("🎬", "#C8321E", "Rolling — rendering your film…"),
    "done": ("✅", "#1E5A5A", "Premiered! See the NOW SHOWING screen."),
    "rejected_face": ("🙈", "#8E1F10", "Real-face generation isn't enabled on this account yet — please tell the crew."),
    "failed": ("⚠️", "#8E1F10", "Technical hiccup — please tell the crew."),
}


@st.fragment(run_every="5s")
def _production_status(ticket_no: str):
    lead = next((x for x in storage.load_leads() if x["ticket"] == ticket_no), None)
    status = (lead or {}).get("status", "queued")
    emoji, color, text = _STATUS_COPY.get(status, _STATUS_COPY["queued"])
    st.markdown(
        f'<div style="text-align:center;margin:.4rem 0 1rem;font-family:\'Prompt\',sans-serif;'
        f'letter-spacing:.06em;color:{color};font-weight:600">{emoji} {text}</div>',
        unsafe_allow_html=True,
    )


SCENES = {
    "lobby": scene_lobby,
    "casting": scene_casting,
    "posters": scene_posters,
    "ticket": scene_ticket,
    "production": scene_production,
}

def _dev_seed():
    """Rehearsal mode: `?dev=1&scene=posters` seeds a placeholder portrait so the
    wizard can be walked without a camera (booth dry-runs, UI review)."""
    if st.query_params.get("dev") != "1":
        return
    if not st.session_state.get("portrait"):
        img = Image.new("RGB", (640, 800), "#EADCC4")
        from PIL import ImageDraw

        d = ImageDraw.Draw(img)
        d.ellipse((170, 160, 470, 460), fill="#C8956C")          # face
        d.ellipse((240, 260, 280, 300), fill="#2B2320")          # eyes
        d.ellipse((360, 260, 400, 300), fill="#2B2320")
        d.arc((250, 330, 390, 430), 20, 160, fill="#2B2320", width=8)  # smile
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=90)
        st.session_state["portrait"] = buf.getvalue()
        st.session_state["portrait_note"] = "640×800 px (rehearsal)"
    if not st.session_state.get("film_key"):
        st.session_state["film_key"] = films.FILMS[0]["key"]
    if (want := st.query_params.get("scene")) in SCENES:
        if want == "production" and not st.session_state.get("ticket_no"):
            st.session_state["ticket_no"] = "PP-0000"
        st.session_state["scene"] = want
        del st.query_params["scene"]  # apply once, or it overrides every transition


_dev_seed()
scene = st.session_state.setdefault("scene", "lobby")
# guard: later scenes need earlier state
if scene in ("posters", "ticket") and not has_photo():
    scene = st.session_state["scene"] = "casting"
if scene == "ticket" and not st.session_state.get("film_key"):
    scene = st.session_state["scene"] = "posters"
if scene == "production" and not st.session_state.get("ticket_no"):
    scene = st.session_state["scene"] = "lobby"

SCENES[scene]()
