"""BACKLOT — crew-only admin: leads, render queue, exports."""

import streamlit as st

from core import films, storage, ui, worker

ui.inject()
ui.header()

ui.clap("CREW ONLY")
st.markdown("## The Backlot")

try:
    admin_password = st.secrets.get("ADMIN_PASSWORD", "")
except FileNotFoundError:
    admin_password = ""

if not admin_password:
    st.warning("Set ADMIN_PASSWORD in .streamlit/secrets.toml to use this page.")
    st.stop()

if not st.session_state.get("crew_ok"):
    pw = st.text_input("Crew password", type="password")
    if st.button("ENTER", type="primary"):
        if pw == admin_password:
            st.session_state["crew_ok"] = True
            st.rerun()
        else:
            st.error("Wrong password.")
    st.stop()

leads = storage.load_leads()

c1, c2, c3, c4, c5 = st.columns(5)
statuses = [lead.get("status", "") for lead in leads]
c1.metric("Tickets", len(leads))
c2.metric("In progress", statuses.count("queued") + statuses.count("rendering"))
c3.metric("Done", statuses.count("done"))
c4.metric("Face-blocked", statuses.count("rejected_face"))
c5.metric("Failed", statuses.count("failed"))

st.divider()
st.markdown("### 🎟 Guest list")
if leads:
    display = [
        {
            "Ticket": lead["ticket"],
            "Name": lead["name"],
            "Company": lead["company"],
            "Job": lead["job_title"],
            "Phone": lead["phone"],
            "Email": lead["email"],
            "Film": films.FILM_BY_KEY.get(lead["film"], {}).get("title_en", lead["film"]),
            "Status": lead["status"],
            "Emailed": lead["email_sent"],
            "When": lead["timestamp"],
        }
        for lead in leads
    ]
    st.dataframe(display, use_container_width=True, hide_index=True)
    st.download_button(
        "⬇ EXPORT LEADS (CSV)",
        data=storage.LEADS_CSV.read_bytes(),
        file_name="premiere_pictures_leads.csv",
        mime="text/csv",
        type="primary",
    )

    st.divider()
    st.markdown("### 🔁 Regenerate a film")
    st.caption("Re-run a film reusing the guest's saved photo — no retake, no re-upload.")
    reusable = [l for l in leads if l.get("asset_id") or l.get("photo_url")]
    if reusable:
        labels = {
            f"{l['ticket']} · {l['name']} · {films.FILM_BY_KEY.get(l['film'], {}).get('title_en', l['film'])} ({l['status']})": l["ticket"]
            for l in reusable
        }
        pick = st.selectbox("Guest", list(labels), key="regen_pick")
        if st.button("🎬 Regenerate", type="primary"):
            if worker.regenerate(labels[pick]):
                st.success(f"Re-queued {labels[pick]} — watch NOW SHOWING.")
            else:
                st.error("No reusable photo on that lead.")
    else:
        st.info("No guests with a saved cloud photo yet (real-face mode only).")
else:
    st.info("No guests yet.")

st.divider()
st.markdown("### 🗑 Remove a film from NOW SHOWING")
st.caption("Deletes the clip from the public gallery. Seeded demo clips (SAMPLE-…) "
           "come back on restart unless also removed from seed/gallery.json.")
_gallery = storage.load_gallery()
if _gallery:
    _labels = {
        f"{e['ticket']} · {e.get('name','')} · "
        f"{films.FILM_BY_KEY.get(e.get('film'), {}).get('title_en', e.get('film',''))}": e["ticket"]
        for e in _gallery
    }
    _pick = st.selectbox("Film to remove", list(_labels), key="remove_pick")
    if st.button("🗑 Remove from Now Showing", type="primary", key="remove_btn"):
        storage.delete_gallery_entry(_labels[_pick])
        st.success(f"Removed {_labels[_pick]} from NOW SHOWING.")
        st.rerun()
else:
    st.info("Nothing in NOW SHOWING yet.")

st.divider()
if st.button("← LOBBY"):
    st.switch_page("views/lobby.py")
