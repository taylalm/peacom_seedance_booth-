"""Premiere Pictures — Seedance 2.0 booth experience.

Run: streamlit run app.py
"""

import streamlit as st

from core import creds, netfix, seed, worker

netfix.ensure_ca_bundle()  # trust corporate proxy CA before any HTTPS call

st.set_page_config(
    page_title="Premiere Pictures",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

try:
    _assets = creds.resolve(dict(st.secrets))
    _assets["project"] = st.secrets.get("ARK_PROJECT", "default")
    _config = {
        "api_key": st.secrets.get("ARK_API_KEY", ""),
        "model": st.secrets.get("ARK_MODEL_EP", ""),
        "smtp": dict(st.secrets.get("smtp", {})),
        "assets": _assets,
        "tos": dict(st.secrets.get("tos", {})),
        "event_prefix": st.secrets.get("EVENT_PREFIX", "premiere"),
        "group_name": st.secrets.get("ASSET_GROUP_NAME", "seedance-booth"),
        "costar_female": st.secrets.get("COSTAR_FEMALE_ASSET", ""),
        "costar_male": st.secrets.get("COSTAR_MALE_ASSET", ""),
    }
except FileNotFoundError:
    _config = {"api_key": "", "model": "", "smtp": {}, "assets": {}, "tos": {}}
worker.ensure_started(_config)
seed.seed_demo_content()  # populate galleries with sample face + films (demo)

pages = [
    st.Page("views/lobby.py", title="Premiere Pictures", default=True),
    st.Page("views/photo_gallery.py", title="Guest Gallery", url_path="guests"),
    st.Page("views/now_showing.py", title="Now Showing", url_path="now-showing"),
    st.Page("views/backlot.py", title="Backlot", url_path="backlot"),
]

st.navigation(pages, position="hidden").run()
