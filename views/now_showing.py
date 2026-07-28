"""NOW SHOWING — the booth's marquee gallery of finished premieres."""

import streamlit as st

from core import films, storage, ui

ui.inject()
ui.header()

st.markdown(
    """
    <div class="mp-marquee">
      <div class="mp-bulbs"></div>
      <h2>NOW SHOWING</h2>
      <div class="sub">WORLD PREMIERES · FRESH FROM THE MAHA PICTURES BACKLOT</div>
      <div class="mp-bulbs"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

@st.fragment(run_every="10s")
def premiere_wall():
    """Redraws itself every 10s so new premieres appear on the booth screen."""
    entries = storage.load_gallery()

    if not entries:
        st.markdown(
            """
            <div class="mp-empty">
              <div style="font-size:2.6rem">🎞️</div>
              The theatre awaits today's first premiere.<br>
              <i>Be the first star on the marquee!</i>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    cols = st.columns(3, gap="medium")
    for i, entry in enumerate(entries):
        film = films.FILM_BY_KEY.get(entry.get("film", ""), None)
        title = f"{film['title_en']} · {film['title_th']}" if film else entry.get("film", "")
        with cols[i % 3]:
            with st.container(key=f"show-{entry['ticket']}"):
                st.markdown('<div class="mp-showcard">', unsafe_allow_html=True)
                st.video(entry["video"])
                st.markdown(
                    f"""
                    <div class="mp-billing">
                      Starring <b>{entry.get('name', '')}</b><br>
                      {title} · {entry.get('ticket', '')}
                    </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


premiere_wall()

st.divider()
_, c1, c2, _ = st.columns([2, 3, 3, 2])
with c1:
    if st.button("← LOBBY", use_container_width=True):
        st.switch_page("views/lobby.py")
with c2:
    if st.button("⟳ REFRESH", type="primary", use_container_width=True):
        st.rerun()

ui.footer()
