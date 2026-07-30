"""BIG SCREEN — /screen: one continuous premiere reel with a unified timeline.

All Now Showing films play as ONE long video (no visible breaks): a single
YouTube-style seek bar spans every clip, hovering it shows a live frame
preview + theme/guest label so a particular face is easy to find, and the
NEWEST premiere always sits at the front of the reel — when a guest's film
finishes rendering it jumps to the head and plays immediately, then the whole
reel loops.

Sound: browsers block unmuted autoplay; one tap enables audio for the whole
session (the page never reloads — the reel updates in-place via fetch).
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

# newest first — the reel plays head -> tail, then loops
_initial = [
    {"ticket": e.get("ticket", ""), "name": e.get("name", ""),
     "film": e.get("film", ""), "video": e.get("video", ""), "created": e.get("created", "")}
    for e in sorted(storage.load_gallery(), key=lambda x: x.get("created", ""), reverse=True)
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
  video#v{height:100vh;max-width:100vw;object-fit:contain;background:#000;}
  #caption{position:fixed;left:50%;transform:translateX(-50%);top:18px;z-index:6;
           width:min(60vh,86vw);text-align:center;color:#F6E08A;
           text-shadow:0 2px 10px #000;pointer-events:none;}
  #caption .t{font-size:24px;letter-spacing:.08em;}
  #caption .s{font-size:15px;color:#D8C49A;letter-spacing:.22em;margin-top:4px;}
  #live{position:fixed;top:24px;left:24px;color:#D8C49A;font-size:13px;letter-spacing:.3em;z-index:6;}
  #live b{color:#E04A2A;}
  #mutehint{position:fixed;top:20px;right:24px;color:#fff;background:rgba(0,0,0,.55);
            border:1px solid #F6C55C;border-radius:999px;padding:8px 18px;font-size:14px;
            letter-spacing:.12em;cursor:pointer;display:none;z-index:6;}
  #empty{position:fixed;inset:0;display:none;align-items:center;justify-content:center;
         flex-direction:column;color:#F6E08A;letter-spacing:.2em;text-align:center;}
  #empty h1{font-size:34px;margin:0 0 12px;}
  #empty p{color:#D8C49A;font-size:15px;}

  /* ---- unified control bar ---- */
  #controls{position:fixed;left:0;right:0;bottom:0;z-index:8;padding:34px 22px 14px;
            background:linear-gradient(transparent,rgba(0,0,0,.82));
            transition:opacity .3s;opacity:0;}
  body.showui #controls{opacity:1;}
  #seekwrap{position:relative;height:18px;display:flex;align-items:center;cursor:pointer;}
  #track{position:relative;height:5px;width:100%;background:rgba(255,255,255,.25);
         border-radius:3px;overflow:visible;}
  #fill{position:absolute;left:0;top:0;bottom:0;width:0%;background:#F6C55C;border-radius:3px;}
  .tick{position:absolute;top:-3px;bottom:-3px;width:2px;background:rgba(0,0,0,.85);z-index:2;}
  #seekwrap:hover #track{height:8px;}
  #row{display:flex;align-items:center;gap:18px;margin-top:10px;color:#EDE3CC;}
  .btn{cursor:pointer;font-size:20px;user-select:none;opacity:.9;}
  .btn:hover{opacity:1;}
  #time{font-size:13px;letter-spacing:.08em;color:#D8C49A;}
  #spacer{flex:1;}

  /* ---- hover preview ---- */
  #peek{position:fixed;bottom:76px;z-index:9;display:none;width:158px;
        transform:translateX(-50%);text-align:center;pointer-events:none;}
  #peek video{width:158px;height:280px;object-fit:cover;border-radius:10px;
              border:2px solid #F6C55C;background:#000;display:block;}
  #peek .pt{margin-top:6px;font-size:12px;color:#F6E08A;letter-spacing:.06em;
            text-shadow:0 1px 6px #000;}
  #peek .pn{font-size:11px;color:#D8C49A;letter-spacing:.12em;}
</style></head><body class="showui">
<div id="stage"><video id="v" playsinline></video></div>
<div id="caption"><div class="t"></div><div class="s"></div></div>
<div id="live">● <b>LIVE</b> · PREMIERE PICTURES</div>
<div id="mutehint">🔇 TAP FOR SOUND</div>
<div id="empty"><h1>PREMIERE PICTURES</h1><p>WAITING FOR THE FIRST PREMIERE…</p></div>

<div id="controls">
  <div id="seekwrap"><div id="track"><div id="fill"></div></div></div>
  <div id="row">
    <span class="btn" id="pp">⏸</span>
    <span id="time">0:00 / 0:00</span>
    <span id="spacer"></span>
    <span class="btn" id="mute">🔊</span>
  </div>
</div>
<div id="peek"><video muted preload="auto"></video><div class="pt"></div><div class="pn"></div></div>

<script>
const TITLES = __TITLES__;
const META = '__META__';
let list = __INITIAL__;              // newest first; reel plays 0..n-1 then loops
const dur = {};                      // video url -> seconds (30 until probed)
const D_DEFAULT = 30;
let idx = 0;

const v = document.getElementById('v');
const capT = document.querySelector('#caption .t');
const capS = document.querySelector('#caption .s');
const hint = document.getElementById('mutehint');
const empty = document.getElementById('empty');
const track = document.getElementById('track');
const fill = document.getElementById('fill');
const timeEl = document.getElementById('time');
const ppBtn = document.getElementById('pp');
const muteBtn = document.getElementById('mute');
const peek = document.getElementById('peek');
const pv = peek.querySelector('video');
const peekT = peek.querySelector('.pt');
const peekN = peek.querySelector('.pn');

const d = e => dur[e.video] || D_DEFAULT;
const total = () => list.reduce((s, e) => s + d(e), 0);
const before = i => list.slice(0, i).reduce((s, e) => s + d(e), 0);
const fmt = t => { t = Math.max(0, Math.floor(t));
  return Math.floor(t/60) + ':' + String(t%60).padStart(2,'0'); };

function locate(gt){                 // global seconds -> [segment index, offset]
  let acc = 0;
  for (let i = 0; i < list.length; i++){
    if (gt < acc + d(list[i])) return [i, gt - acc];
    acc += d(list[i]);
  }
  return [Math.max(0, list.length - 1), 0];
}

function drawTicks(){
  track.querySelectorAll('.tick').forEach(x => x.remove());
  const T = total();
  let acc = 0;
  for (let i = 0; i < list.length - 1; i++){
    acc += d(list[i]);
    const t = document.createElement('div');
    t.className = 'tick'; t.style.left = (acc / T * 100) + '%';
    track.appendChild(t);
  }
}

function caption(e){
  capT.textContent = TITLES[e.film] || (e.film || '').toUpperCase();
  capS.textContent = 'STARRING ' + (e.name || 'A GUEST').toUpperCase()
                   + '  ·  ' + (e.ticket || '');
}

function playIndex(i, offset){
  if (!list.length){ empty.style.display = 'flex'; return; }
  empty.style.display = 'none';
  idx = ((i % list.length) + list.length) % list.length;
  const e = list[idx];
  caption(e);
  if (v.getAttribute('src') !== e.video){ v.src = e.video; }
  const seekTo = offset || 0;
  const go = () => { if (seekTo) v.currentTime = seekTo;
    v.play().catch(() => { v.muted = true; syncMute(); hint.style.display = 'block';
                           v.play().catch(()=>{}); }); };
  (v.readyState >= 1) ? go() : v.addEventListener('loadedmetadata', go, {once: true});
}

v.addEventListener('ended', () => playIndex(idx + 1));
v.addEventListener('error', () => setTimeout(() => playIndex(idx + 1), 800));
v.addEventListener('loadedmetadata', () => {          // learn true durations
  const e = list[idx];
  if (e && v.duration && isFinite(v.duration)){ dur[e.video] = v.duration; drawTicks(); }
});
v.addEventListener('timeupdate', () => {
  const T = total();
  const g = before(idx) + (v.currentTime || 0);
  fill.style.width = (T ? g / T * 100 : 0) + '%';
  timeEl.textContent = fmt(g) + ' / ' + fmt(T);
});

/* ---- pause / sound ---- */
function syncPP(){ ppBtn.textContent = v.paused ? '▶' : '⏸'; }
function syncMute(){ muteBtn.textContent = v.muted ? '🔇' : '🔊'; }
v.addEventListener('play', syncPP); v.addEventListener('pause', syncPP);
v.addEventListener('click', () => { v.paused ? v.play() : v.pause(); });
ppBtn.addEventListener('click', e => { e.stopPropagation(); v.paused ? v.play() : v.pause(); });
muteBtn.addEventListener('click', e => { e.stopPropagation(); v.muted = !v.muted; syncMute();
                                         if (!v.muted) hint.style.display = 'none'; });
function soundOn(){ if (v.muted){ v.muted = false; syncMute(); hint.style.display = 'none'; } }
document.addEventListener('click', soundOn, {capture: true});
document.addEventListener('touchstart', soundOn, {capture: true});

/* ---- unified seek + hover preview ---- */
const wrap = document.getElementById('seekwrap');
function frac(ev){
  const r = track.getBoundingClientRect();
  return Math.min(1, Math.max(0, (ev.clientX - r.left) / r.width));
}
wrap.addEventListener('click', ev => {
  const [i, off] = locate(frac(ev) * total());
  playIndex(i, off);
});
let lastPeek = 0;
wrap.addEventListener('mousemove', ev => {
  const f = frac(ev);
  const [i, off] = locate(f * total());
  const e = list[i]; if (!e) return;
  peek.style.display = 'block';
  peek.style.left = ev.clientX + 'px';
  peekT.textContent = TITLES[e.film] || e.film;
  peekN.textContent = (e.name || 'GUEST').toUpperCase() + ' · ' + fmt(off);
  const now = Date.now();
  if (now - lastPeek > 180){                     // throttle frame seeks
    lastPeek = now;
    if (pv.getAttribute('src') !== e.video) pv.src = e.video;
    const seek = () => { try { pv.currentTime = Math.min(off, (pv.duration || off)); } catch(_){} };
    (pv.readyState >= 1) ? seek() : pv.addEventListener('loadedmetadata', seek, {once: true});
  }
});
wrap.addEventListener('mouseleave', () => { peek.style.display = 'none'; });

/* ---- auto-hide controls ---- */
let uiTimer;
function showUI(){
  document.body.classList.add('showui');
  clearTimeout(uiTimer);
  uiTimer = setTimeout(() => { if (!v.paused) document.body.classList.remove('showui'); }, 3500);
}
document.addEventListener('mousemove', showUI);
document.addEventListener('touchstart', showUI);
v.addEventListener('pause', showUI);
showUI();

/* ---- live updates: newest premiere goes to the FRONT and plays now ---- */
async function poll(){
  try {
    const r = await fetch(META + '?t=' + Date.now(), {cache: 'no-store'});
    if (!r.ok) return;
    const incoming = (await r.json())
      .filter(e => String(e.video || '').startsWith('http'))
      .sort((a, b) => String(b.created || '').localeCompare(String(a.created || '')));
    const seen = new Set(list.map(e => e.video));
    const brandNew = incoming.filter(e => !seen.has(e.video));
    const currentSrc = list[idx] ? list[idx].video : null;
    list = incoming;                                  // newest-first canonical order
    drawTicks();
    if (brandNew.length){
      playIndex(0);                                   // fresh premiere: front + play now
    } else if (currentSrc){
      const k = list.findIndex(e => e.video === currentSrc);
      idx = (k >= 0) ? k : Math.min(idx, Math.max(0, list.length - 1));
      if (k < 0) playIndex(idx);                      // current was removed
    }
    if ((!v.currentSrc || v.ended) && list.length) playIndex(idx);
  } catch(err){ /* network blip — keep looping current reel */ }
}
setInterval(poll, 15000);

/* ---- start ---- */
if (list.length){ drawTicks(); playIndex(0); }
else { empty.style.display = 'flex'; poll(); }
syncPP(); syncMute();
</script></body></html>
    """
    .replace("__TITLES__", json.dumps(_titles))
    .replace("__INITIAL__", json.dumps(_initial))
    .replace("__META__", META_URL),
    height=1200,
    scrolling=False,
)
