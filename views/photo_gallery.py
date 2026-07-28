"""GUEST GALLERY — every photo captured at the booth, reusable for new films."""

import streamlit as st

from core import guests, storage, ui

ui.inject()
ui.header()

ui.clap("GUEST GALLERY")
st.markdown("## Guest photos")
st.caption("Every photo captured at the booth. Pick one to cast into a film — no retake needed.")

photos = storage.load_guest_photos()

if not photos:
    note = (
        "No guest photos yet. Photos captured in ACTION will appear here automatically."
        if guests.realface_available()
        else "The guest gallery is available in real-face mode (cloud credentials). "
             "Photos captured now are kept on this device only."
    )
    st.markdown(
        f"""
        <div class="mp-empty">
          <div style="font-size:2.6rem">📸</div>
          {note}
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    cols = st.columns(4, gap="medium")
    for i, g in enumerate(photos):
        with cols[i % 4]:
            with st.container(key=f"guest-{g['id']}"):
                st.markdown('<div class="mp-showcard">', unsafe_allow_html=True)
                st.image(g["tos_url"], use_container_width=True)
                ready = "✓ ready" if g.get("asset_id") else "• new"
                st.markdown(
                    f'<div class="mp-billing"><b>{g.get("label", "Guest")}</b><br>'
                    f'{g.get("created", "")[:16].replace("T", " ")} · {ready}</div></div>',
                    unsafe_allow_html=True,
                )
            if st.button("🎬 Cast into a film", key=f"cast-{g['id']}", type="primary", use_container_width=True):
                st.session_state["guest_photo"] = g
                st.session_state.pop("portrait", None)
                st.session_state.pop("portrait_note", None)
                st.session_state["scene"] = "posters"
                st.switch_page("views/lobby.py")
            if st.button("🗑 Remove", key=f"del-{g['id']}", use_container_width=True):
                storage.delete_guest_photo(g["id"])
                st.rerun()

st.divider()
_, c1, c2, _ = st.columns([2, 3, 3, 2])
with c1:
    if st.button("← LOBBY", use_container_width=True):
        st.switch_page("views/lobby.py")
with c2:
    if st.button("⟳ REFRESH", type="primary", use_container_width=True):
        st.rerun()

ui.footer()
