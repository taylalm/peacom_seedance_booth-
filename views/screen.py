"""BIG SCREEN — /screen: fullscreen auto-looping premiere reel.

Point a booth TV/projector at this URL. It plays every Now Showing film in a
continuous loop and polls the cloud gallery list live, so each new guest
premiere slides into the rotation automatically — no crew interaction.

Sound: browsers block unmuted autoplay, so the screen starts muted after a
moment; one tap/click anywhere enables sound for the whole session (the page
never reloads — the playlist updates in-place via fetch).
"""

import json

import streamlit as st
import streamlit.components.v1 as components

from core import films, storage

st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer { display: none !important; }
      .stApp { background: #000; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      iframe { width: 100vw !important; height: 100vh !important; display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

_titles = {k: f["title_en"] for k, f in films.FILM_BY_KEY.items()}

# initial playlist from local state (instant start); JS then polls the cloud copy
_initial = [
    {"ticket": e.get("ticket", ""), "name": e.get("name", ""),
     "film": e.get("film", ""), "video": e.get("video", ""), "created": e.get("created", "")}
    for e in sorted(storage.load_gallery(), key=lambda x: x.get("created", ""))
    if str(e.get("video", "")).startswith("http")
]

META_URL = ("https://seedance-booth-guests.tos-ap-southeast-1.bytepluses.com/"
            "appdata/premiere/gallery_metadata.json")

components.html(
    """
<!DOCTYPE html><html><head><style>
  html,body{margin:0;height:100%;background:#000;overflow:hidden;
             font-family:Georgia,'Times New Roman',serif;}
  #stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;}
  video{height:100vh;max-width:100vw;object-fit:contain;background:#000;}
  #caption{position:fixed;left:50%;transform:translateX(-50%);top:18px;
           width:min(60vh,86vw);text-align:center;color:#F6E08A;
           text-shadow:0 2px 10px #000;pointer-events:none;}
  .navbtn{position:fixed;top:50%;transform:translateY(-50%);z-index:5;
          color:#F6E08A;background:rgba(0,0,0,.45);border:1px solid rgba(246,197,92,.5);
          border-radius:999px;width:52px;height:52px;font-size:26px;line-height:50px;
          text-align:center;cursor:pointer;user-select:none;opacity:.35;}
  .navbtn:hover{opacity:1;}
  #prev{left:18px;} #next{right:18px;}
  #caption .t{font-size:24px;letter-spacing:.08em;}
  #caption .s{font-size:16px;color:#D8C49A;letter-spacing:.24em;margin-top:4px;}
  #live{position:fixed;bottom:70px;left:24px;color:#D8C49A;font-size:13px;letter-spacing:.3em;}
  #live b{color:#E04A2A;}
  #mutehint{position:fixed;top:20px;right:24px;color:#fff;background:rgba(0,0,0,.55);
            border:1px solid #F6C55C;border-radius:999px;padding:8px 18px;font-size:14px;
            letter-spacing:.12em;cursor:pointer;display:none;}
  #empty{position:fixed;inset:0;display:none;align-items:center;justify-content:center;
         flex-direction:column;color:#F6E08A;letter-spacing:.2em;text-align:center;}
  #empty h1{font-size:34px;margin:0 0 12px;}
  #empty p{color:#D8C49A;font-size:15px;}
</style></head><body>
<div id="stage"><video id="v" playsinline controls controlslist="nodownload"></video></div>
<div class="navbtn" id="prev" title="Previous film">&#8249;</div>
<div class="navbtn" id="next" title="Next film">&#8250;</div>
<div id="caption"><div class="t"></div><div class="s"></div></div>
<div id="live">● <b>LIVE</b> · PREMIERE PICTURES</div>
<div id="mutehint">🔇 TAP FOR SOUND</div>
<div id="empty"><h1>PREMIERE PICTURES</h1><p>WAITING FOR THE FIRST PREMIERE…</p></div>
<script>
const TITLES = __TITLES__;
let playlist = __INITIAL__;          // ordered oldest -> newest
const known = new Set(playlist.map(e => e.video));
const fresh = [];                    // newly arrived premieres jump the queue
let idx = -1;

const v = document.getElementById('v');
const capT = document.querySelector('#caption .t');
const capS = document.querySelector('#caption .s');
const hint = document.getElementById('mutehint');
const empty = document.getElementById('empty');

function show(entry){
  capT.textContent = TITLES[entry.film] || (entry.film || '').toUpperCase();
  capS.textContent = 'STARRING ' + (entry.name || 'A GUEST').toUpperCase()
                   + '  ·  ' + (entry.ticket || '');
  v.src = entry.video;
  v.play().catch(()=>{ v.muted = true; hint.style.display='block';
                       v.play().catch(()=>{}); });
}
function next(){
  if (fresh.length) { show(fresh.shift()); return; }
  if (!playlist.length) { empty.style.display='flex'; return; }
  empty.style.display='none';
  idx = (idx + 1) % playlist.length;
  show(playlist[idx]);
}
function prevFilm(){
  if (!playlist.length) return;
  idx = (idx - 1 + playlist.length) % playlist.length;
  show(playlist[idx]);
}
v.addEventListener('ended', next);
v.addEventListener('error', () => setTimeout(next, 800));
document.getElementById('next').addEventListener('click', e => { e.stopPropagation(); next(); });
document.getElementById('prev').addEventListener('click', e => { e.stopPropagation(); prevFilm(); });
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' && e.shiftKey) next();
  if (e.key === 'ArrowLeft' && e.shiftKey) prevFilm();
});

// first tap/click enables sound for the whole session (native controls still work)
function soundOn(){ v.muted = false; hint.style.display='none'; }
document.addEventListener('click', soundOn);
document.addEventListener('touchstart', soundOn);

// poll the cloud gallery list; new premieres play right after the current film
async function poll(){
  try {
    const r = await fetch('__META__' + '?t=' + Date.now(), {cache:'no-store'});
    if (!r.ok) return;
    const list = (await r.json())
      .filter(e => String(e.video||'').startsWith('http'))
      .sort((a,b) => String(a.created||'').localeCompare(String(b.created||'')));
    for (const e of list){
      if (!known.has(e.video)){
        known.add(e.video);
        playlist.push(e);
        fresh.push(e);            // premiere it next
      }
    }
    // only auto-advance if nothing is loaded or the current film finished —
    // never while the user has paused mid-video
    if ((!v.currentSrc || v.ended) && (playlist.length || fresh.length)) next();
  } catch(err){ /* network blip — keep looping current list */ }
}
setInterval(poll, 15000);

// start: try with sound; browsers will fall back to muted via show()'s catch
if (playlist.length) next(); else { empty.style.display='flex'; poll(); }
</script></body></html>
    """
    .replace("__TITLES__", json.dumps(_titles))
    .replace("__INITIAL__", json.dumps(_initial))
    .replace("__META__", META_URL),
    height=1200,
    scrolling=False,
)
