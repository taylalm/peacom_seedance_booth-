"""Premiere Pictures design system — classic cinema-poster aesthetic.

Palette: aged-poster cream / vermillion red / marigold gold / teal ink.
Type: Chonburi (Thai display), Archivo Black (EN slab), Taviraj (body),
Prompt (UI labels). All styling injected as one CSS block.
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Chonburi&family=Archivo+Black&family=Taviraj:ital,wght@0,400;0,500;0,600;1,400&family=Prompt:wght@400;500;600&family=Noto+Sans+Thai:wght@400;600&display=swap');

:root {
  --cream:   #F4E9D8;
  --cream-2: #EADCC4;
  --paper:   #FFFDF7;
  --verm:    #C8321E;
  --verm-d:  #8E1F10;
  --gold:    #E8A020;
  --gold-l:  #F6C55C;
  --teal:    #1E5A5A;
  --ink:     #2B2320;
}

/* ---------- canvas ---------- */
.stApp {
  background:
    radial-gradient(circle at 20% 10%, rgba(232,160,32,.10), transparent 45%),
    radial-gradient(circle at 85% 90%, rgba(30,90,90,.08), transparent 40%),
    radial-gradient(rgba(43,35,32,.045) 1px, transparent 1.4px),
    var(--cream);
  background-size: auto, auto, 14px 14px, auto;
  color: var(--ink);
}
header[data-testid="stHeader"] { display: none; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 1.4rem; padding-bottom: 3rem; max-width: 1180px; }

h1, h2, h3 { font-family: 'Chonburi', 'Archivo Black', serif !important; color: var(--ink); }
p, li, label, .stMarkdown { font-family: 'Taviraj', 'Noto Sans Thai', serif; }

/* ---------- header bar ---------- */
.mp-header {
  display: flex; align-items: baseline; justify-content: space-between;
  border-bottom: 3px double var(--ink); padding-bottom: .55rem; margin-bottom: 1.1rem;
}
.mp-logo { font-family: 'Archivo Black', sans-serif; font-size: 1.5rem; letter-spacing: .02em; }
.mp-logo .reel { color: var(--verm); }
.mp-logo em {
  font-family: 'Chonburi', serif; font-style: normal; font-size: .95rem;
  color: var(--teal); margin-left: .5rem;
}
.mp-spec {
  font-family: 'Prompt', sans-serif; font-size: .68rem; letter-spacing: .18em;
  color: var(--teal); text-align: right;
}

/* ---------- filmstrip stepper ---------- */
.mp-strip {
  display: flex; gap: 10px; background: var(--ink); border-radius: 12px;
  padding: 16px 14px; margin: .3rem 0 1.4rem;
  background-image:
    radial-gradient(circle, rgba(244,233,216,.85) 2px, transparent 2.7px),
    radial-gradient(circle, rgba(244,233,216,.85) 2px, transparent 2.7px);
  background-size: 18px 6px, 18px 6px;
  background-position: 6px 5px, 6px calc(100% - 11px);
  background-repeat: repeat-x, repeat-x;
}
.mp-frame {
  flex: 1; text-align: center; padding: .5rem .3rem;
  border: 2px dashed rgba(244,233,216,.30); border-radius: 8px;
  color: rgba(244,233,216,.45);
  font-family: 'Prompt', sans-serif; font-size: .78rem; letter-spacing: .06em;
}
.mp-frame.done   { border-style: solid; border-color: var(--gold);  color: var(--gold-l); }
.mp-frame.active {
  border-style: solid; border-color: var(--gold-l); color: var(--ink);
  background: var(--gold-l); font-weight: 600;
  box-shadow: 0 0 14px rgba(246,197,92,.45);
}

/* ---------- hero (lobby) ---------- */
.mp-hero { position: relative; text-align: center; padding: 1.6rem 0 .6rem; overflow: hidden; }
.mp-sunburst {
  position: absolute; inset: -55% -20%; z-index: 0; pointer-events: none;
  background: repeating-conic-gradient(from 8deg at 50% 42%,
    rgba(232,160,32,.13) 0 6deg, transparent 6deg 14deg);
  -webkit-mask-image: radial-gradient(circle at 50% 42%, black 0%, transparent 62%);
          mask-image: radial-gradient(circle at 50% 42%, black 0%, transparent 62%);
}
.mp-hero-kicker {
  position: relative; z-index: 1;
  font-family: 'Prompt', sans-serif; font-size: .74rem; letter-spacing: .34em;
  color: var(--verm); text-transform: uppercase;
}
.mp-hero h1 {
  position: relative; z-index: 1; font-size: 3.4rem; line-height: 1.14; margin: .5rem 0 .2rem;
}
.mp-hero h1 .star { color: var(--verm); }
.mp-hero-sub {
  position: relative; z-index: 1;
  font-family: 'Taviraj', serif; font-style: italic; font-size: 1.22rem; color: var(--teal);
}
.mp-hero-tag {
  position: relative; z-index: 1; display: inline-block; margin-top: .9rem;
  font-family: 'Prompt', sans-serif; font-size: .72rem; letter-spacing: .22em;
  color: var(--ink); background: var(--gold-l);
  border: 2px solid var(--ink); border-radius: 999px; padding: .3rem 1.1rem;
  box-shadow: 3px 3px 0 rgba(43,35,32,.25);
}

/* fanned mini posters */
.mp-fan { position: relative; z-index: 1; display: flex; justify-content: center; margin: 1.6rem 0 .8rem; height: 190px; }
.mp-fan-card {
  position: relative; width: 118px; height: 168px; border-radius: 10px; margin: 0 -12px; overflow: hidden;
  border: 3px solid var(--paper); box-shadow: 0 10px 22px rgba(43,35,32,.35);
  display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
  transform: rotate(var(--r)) translateY(var(--y));
}
.mp-fan-card svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.mp-fan-card span {
  position: relative; z-index: 1; font-family: 'Chonburi', serif; font-size: .6rem; color: var(--paper);
  text-shadow: 0 2px 5px rgba(0,0,0,.8); padding: 0 6px 8px; text-align: center; line-height: 1.2;
}

/* ---------- poster cards ---------- */
.mp-poster {
  background: var(--paper); border: 3px solid var(--ink); border-radius: 14px;
  overflow: hidden; box-shadow: 7px 7px 0 rgba(43,35,32,.16);
  margin-bottom: .7rem; position: relative;
}
.mp-poster.selected { outline: 4px solid var(--gold); outline-offset: 2px; }
.mp-poster-art {
  aspect-ratio: 3 / 4; position: relative; overflow: hidden; background: var(--ink);
}
.mp-poster-art svg { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }
.mp-poster-vignette {
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(to bottom, rgba(0,0,0,.35) 0%, transparent 22%, transparent 68%, rgba(0,0,0,.35) 100%);
}
.mp-poster-no {
  position: absolute; top: 10px; left: 12px; z-index: 2;
  font-family: 'Archivo Black', sans-serif; font-size: .8rem; color: rgba(255,253,247,.9);
  letter-spacing: .12em; text-shadow: 0 1px 4px rgba(0,0,0,.7);
}
.mp-cast-badge {
  position: absolute; top: 10px; right: 10px; z-index: 2;
  background: var(--gold-l); color: var(--ink); border: 2px solid var(--ink);
  border-radius: 999px; padding: .2rem .65rem;
  font-family: 'Prompt', sans-serif; font-size: .66rem; font-weight: 600; letter-spacing: .08em;
  transform: rotate(6deg); box-shadow: 2px 2px 0 rgba(43,35,32,.3);
}
.mp-poster-ribbon {
  background: var(--ink); color: var(--gold-l); text-align: center;
  font-family: 'Prompt', sans-serif; font-size: .66rem; letter-spacing: .16em; padding: 5px 6px;
}
.mp-poster-body { padding: .7rem .85rem .85rem; }
.mp-poster-body h3 {
  margin: 0; font-family: 'Archivo Black', sans-serif; font-size: 1.12rem;
  letter-spacing: .01em; line-height: 1.15; color: var(--ink);
}
.mp-poster-th {
  font-family: 'Chonburi', serif; font-size: 1.02rem; color: var(--verm); margin: .1rem 0 .4rem;
}
.mp-logline { font-size: .9rem; font-style: italic; color: #55483F; margin: 0 0 .35rem; min-height: 2.4em; }
.mp-synopsis { font-size: .82rem; line-height: 1.5; color: #4A3F38; margin: 0 0 .5rem; }
.mp-tags { font-family: 'Prompt', sans-serif; font-size: .62rem; letter-spacing: .14em; color: var(--teal); }

/* ---------- casting polaroid ---------- */
.st-key-casting-card {
  position: relative; background: var(--paper); border: 1px solid #E2D6BF;
  padding: 16px 16px 10px; transform: rotate(-1.6deg);
  box-shadow: 0 14px 28px rgba(43,35,32,.24); border-radius: 4px;
}
.st-key-casting-card img { border: 1px solid #E2D6BF; }
.mp-stamp {
  position: absolute; top: 24px; right: 20px; z-index: 5; transform: rotate(10deg);
  border: 3px solid var(--verm); color: var(--verm); border-radius: 8px;
  padding: .25rem .7rem; background: rgba(255,253,247,.82);
  font-family: 'Archivo Black', sans-serif; font-size: .78rem; letter-spacing: .1em;
  text-align: center;
}
.mp-stamp small { display: block; font-family: 'Prompt', sans-serif; font-size: .6rem; letter-spacing: .16em; }
.mp-polaroid-caption {
  font-family: 'Chonburi', serif; text-align: center; color: var(--ink);
  font-size: .85rem; padding-top: .5rem;
}

/* clapperboard headline */
.mp-clap {
  display: inline-block; background: var(--ink); color: var(--paper);
  border-radius: 10px 10px 4px 4px; padding: .45rem 1.1rem .5rem; margin-bottom: .8rem;
  font-family: 'Prompt', sans-serif; font-size: .72rem; letter-spacing: .22em;
  background-image: repeating-linear-gradient(115deg,
    var(--gold-l) 0 14px, var(--ink) 14px 28px);
  background-size: 100% 8px; background-repeat: no-repeat; background-position: top;
  padding-top: .85rem;
}

/* ---------- premiere ticket ---------- */
.st-key-ticket-card {
  position: relative;
  background:
    radial-gradient(circle at 0 50%, var(--cream) 11px, transparent 12px),
    radial-gradient(circle at 100% 50%, var(--cream) 11px, transparent 12px),
    linear-gradient(135deg, #F9E9BE, var(--gold-l) 55%, #EFB63C);
  border: 3px solid var(--ink); border-radius: 16px; padding: 1.3rem 1.5rem;
  box-shadow: 7px 7px 0 rgba(43,35,32,.16);
}
.mp-ticket-head {
  display: flex; justify-content: space-between; align-items: baseline;
  border-bottom: 2px dashed rgba(43,35,32,.45); padding-bottom: .55rem; margin-bottom: .8rem;
}
.mp-ticket-head .adm { font-family: 'Archivo Black', sans-serif; font-size: .72rem; letter-spacing: .22em; color: var(--verm-d); }
.mp-ticket-head .film { font-family: 'Chonburi', serif; font-size: 1.05rem; }
.st-key-ticket-card .stTextInput input {
  background: var(--paper); border: 2px solid var(--ink); border-radius: 8px;
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif;
}
.st-key-ticket-card .stTextInput label, .st-key-ticket-card .stCheckbox label {
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif !important; font-weight: 600;
  color: var(--ink) !important;
}
.st-key-ticket-card [data-testid="stForm"] { border: none; padding: 0; }

/* ---------- ticket stub (production) ---------- */
.mp-stub {
  max-width: 560px; margin: 1rem auto; position: relative;
  background: linear-gradient(135deg, #F9E9BE, var(--gold-l) 55%, #EFB63C);
  border: 3px solid var(--ink); border-radius: 16px; padding: 1.4rem 1.7rem;
  box-shadow: 7px 7px 0 rgba(43,35,32,.16); text-align: center;
  transform: rotate(-1.2deg);
}
.mp-stub .no { font-family: 'Archivo Black', sans-serif; font-size: 2rem; color: var(--verm-d); letter-spacing: .06em; }
.mp-stub .divider { border-top: 2px dashed rgba(43,35,32,.45); margin: .8rem 0; }
.mp-stub .meta { font-family: 'Prompt', sans-serif; font-size: .74rem; letter-spacing: .16em; color: var(--ink); }

/* ---------- marquee (now showing) ---------- */
.mp-marquee {
  background: var(--ink); border: 5px solid var(--gold); border-radius: 18px;
  padding: 1.5rem 1rem 1.6rem; text-align: center; margin-bottom: 1.4rem;
  box-shadow: 0 0 34px rgba(232,160,32,.35), 7px 7px 0 rgba(43,35,32,.16);
}
.mp-marquee h2 { color: var(--gold-l); margin: .35rem 0; font-size: 2rem; }
.mp-marquee .sub { color: rgba(244,233,216,.75); font-family: 'Prompt', sans-serif; font-size: .74rem; letter-spacing: .3em; }
.mp-bulbs {
  height: 12px; margin: 0 auto; width: 88%;
  background-image: radial-gradient(circle, var(--gold-l) 3px, rgba(246,197,92,.18) 4px, transparent 5px);
  background-size: 24px 12px; background-repeat: repeat-x; background-position: center;
  animation: mp-blink 1.1s steps(2) infinite;
}
@keyframes mp-blink { 50% { opacity: .35; } }

.mp-empty {
  text-align: center; border: 3px dashed rgba(43,35,32,.3); border-radius: 16px;
  padding: 3rem 1rem; color: #6B5C50; font-style: italic;
}

/* gallery poster frame */
.mp-showcard {
  background: var(--paper); border: 3px solid var(--ink); border-radius: 12px;
  padding: 10px 10px 6px; box-shadow: 6px 6px 0 rgba(43,35,32,.16); margin-bottom: 1rem;
}
.mp-billing { text-align: center; font-family: 'Prompt', sans-serif; font-size: .7rem; letter-spacing: .12em; color: var(--ink); padding: .45rem 0 .3rem; }
.mp-billing b { font-family: 'Chonburi', serif; font-size: .85rem; letter-spacing: 0; }

/* ---------- footer strip ---------- */
.mp-footer {
  margin-top: 2.2rem; border-top: 3px double var(--ink); padding-top: .6rem;
  text-align: center; font-family: 'Prompt', sans-serif; font-size: .64rem;
  letter-spacing: .26em; color: var(--teal);
}

/* ---------- buttons ---------- */
.stButton > button, .stFormSubmitButton > button {
  font-family: 'Chonburi', 'Prompt', serif !important;
  border-radius: 12px !important; padding: .55rem 1.4rem !important;
  transition: transform .08s ease, box-shadow .08s ease !important;
}
.stButton > button[kind="primary"], button[data-testid="stBaseButton-primary"],
.stFormSubmitButton > button[kind="primary"] {
  background: var(--verm) !important; color: #FFF8EC !important;
  border: 3px solid var(--gold) !important;
  box-shadow: 0 5px 0 var(--verm-d) !important;
}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button[kind="primary"]:hover {
  transform: translateY(2px); box-shadow: 0 3px 0 var(--verm-d) !important;
}
.stButton > button[kind="secondary"], button[data-testid="stBaseButton-secondary"] {
  background: transparent !important; color: var(--teal) !important;
  border: 2px solid var(--teal) !important;
}
.stButton > button:disabled {
  background: #D8CBB4 !important; color: #8B7E6E !important;
  border-color: #B8AA92 !important; box-shadow: none !important;
}

/* ---------- tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: .4rem; border-bottom: 2px solid var(--ink); }
.stTabs [data-baseweb="tab"] {
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif; font-weight: 600;
  background: var(--cream-2); border-radius: 10px 10px 0 0; padding: .45rem 1rem;
  color: var(--ink);
}
.stTabs [aria-selected="true"] { background: var(--ink) !important; color: var(--gold-l) !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

[data-testid="stFileUploaderDropzone"] {
  background: var(--paper); border: 2px dashed var(--ink); border-radius: 12px;
}
[data-testid="stCameraInput"] button { border-radius: 12px; }

.stAlert { border-radius: 12px; }
</style>
"""


def inject():
    st.markdown(CSS, unsafe_allow_html=True)


def header():
    st.markdown(
        """
        <div class="mp-header">
          <div class="mp-logo"><span class="reel">🎬</span> PREMIERE PICTURES <em>lights · camera · you</em></div>
          <div class="mp-spec">ONE REEL · 15 SEC · 9:16 · 720P<br>POWERED BY SEEDANCE 2.0 · BYTEPLUS MODELARK</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


STEPS = [
    ("1", "CASTING"),
    ("2", "THE POSTER"),
    ("3", "TICKET"),
    ("4", "ACTION"),
]


def filmstrip(current: int):
    """Progress stepper as a strip of film. `current` is 1-based; frames before it are done."""
    frames = []
    for i, (num, label) in enumerate(STEPS, start=1):
        cls = "done" if i < current else "active" if i == current else ""
        frames.append(f'<div class="mp-frame {cls}">{num} · {label}</div>')
    st.markdown(f'<div class="mp-strip">{"".join(frames)}</div>', unsafe_allow_html=True)


def clap(text: str):
    st.markdown(f'<div class="mp-clap">{text}</div>', unsafe_allow_html=True)


def _tidy(html: str) -> str:
    """Strip leading whitespace from every line so Streamlit's markdown parser
    never mistakes indented HTML/SVG for a code block (which leaks raw tags)."""
    return "\n".join(line.strip() for line in html.strip().splitlines())


def poster_art(key: str) -> str:
    """Hand-built cinematic SVG poster art per film — self-contained (no network),
    so it renders anywhere including an offline booth. viewBox 0 0 300 400 (3:4)."""
    art = {
        # --- Action Blockbuster: dusk rooftop set, crane, running star ---
        "action": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="ac-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0A0E2A"/><stop offset="0.6" stop-color="#5A1430"/><stop offset="1" stop-color="#C8321E"/></linearGradient>
  <radialGradient id="ac-sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FBE38A"/><stop offset="0.6" stop-color="#F6C55C"/><stop offset="1" stop-color="#F6C55C" stop-opacity="0"/></radialGradient>
 </defs>
 <rect width="300" height="400" fill="url(#ac-sky)"/>
 <circle cx="150" cy="180" r="110" fill="url(#ac-sun)" opacity="0.8"/>
 <g fill="#060818" opacity="0.9">
  <rect x="0" y="250" width="46" height="150"/><rect x="54" y="290" width="40" height="110"/>
  <rect x="206" y="270" width="44" height="130"/><rect x="258" y="240" width="42" height="160"/>
 </g>
 <g fill="#F6C55C" opacity="0.7"><rect x="8" y="262" width="5" height="5"/><rect x="22" y="280" width="5" height="5"/><rect x="216" y="284" width="5" height="5"/><rect x="268" y="256" width="5" height="5"/><rect x="282" y="300" width="5" height="5"/></g>
 <g stroke="#060818" stroke-width="6" fill="none" opacity="0.95"><path d="M20 130 L120 96 M120 96 L96 250"/><circle cx="20" cy="130" r="8" fill="#060818"/></g>
 <rect x="96" y="330" width="120" height="8" rx="4" fill="#060818" opacity="0.8"/>
 <g transform="translate(150 300)" fill="#0A0612">
  <circle cx="0" cy="-52" r="13"/>
  <path d="M-4 -40 c-16 4 -20 18 -16 34 l-22 30 14 8 20 -28 6 22 26 10 6 -14 -20 -8 -2 -24 c4 -16 0 -28 -12 -30Z"/>
 </g>
 <g stroke="#F6C55C" stroke-width="3" opacity="0.8" stroke-linecap="round"><path d="M92 236 l-14 -8 M96 252 l-16 0 M212 260 l14 -8"/></g>
 <rect y="360" width="300" height="40" fill="#060818" opacity="0.7"/>
 <text x="150" y="386" text-anchor="middle" font-family="Space Mono,monospace" font-size="13" fill="#F6C55C" opacity="0.95">ACTION!</text>
</svg>""",
        # --- Red Carpet Premiere: carpet perspective, ropes, flashes ---
        "redcarpet": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="rc-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#12060E"/><stop offset="0.55" stop-color="#2A0A14"/><stop offset="1" stop-color="#5A0F24"/></linearGradient>
  <linearGradient id="rc-cp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7A1020"/><stop offset="1" stop-color="#C8321E"/></linearGradient>
  <radialGradient id="rc-gl" cx="0.5" cy="0.3" r="0.55"><stop offset="0" stop-color="#F8D98A" stop-opacity="0.6"/><stop offset="1" stop-color="#F8D98A" stop-opacity="0"/></radialGradient>
 </defs>
 <rect width="300" height="400" fill="url(#rc-bg)"/>
 <rect width="300" height="400" fill="url(#rc-gl)"/>
 <g fill="#FFF" opacity="0.9">
  <g transform="translate(52 84)"><path d="M0 -10 L2 -2 L10 0 L2 2 L0 10 L-2 2 L-10 0 L-2 -2 Z"/></g>
  <g transform="translate(246 66)"><path d="M0 -8 L2 -2 L8 0 L2 2 L0 8 L-2 2 L-8 0 L-2 -2 Z"/></g>
  <g transform="translate(210 130)" opacity="0.7"><path d="M0 -6 L1.5 -1.5 L6 0 L1.5 1.5 L0 6 L-1.5 1.5 L-6 0 L-1.5 -1.5 Z"/></g>
  <g transform="translate(84 150)" opacity="0.6"><path d="M0 -6 L1.5 -1.5 L6 0 L1.5 1.5 L0 6 L-1.5 1.5 L-6 0 L-1.5 -1.5 Z"/></g>
 </g>
 <path d="M120 180 L180 180 L262 400 L38 400 Z" fill="url(#rc-cp)"/>
 <g stroke="#F6C55C" stroke-width="4" fill="none" opacity="0.9">
  <path d="M96 214 Q70 232 66 260 M204 214 Q230 232 234 260 M60 288 Q34 306 30 334 M240 288 Q266 306 270 334"/>
 </g>
 <g fill="#F6C55C"><circle cx="96" cy="210" r="7"/><circle cx="204" cy="210" r="7"/><circle cx="60" cy="284" r="7"/><circle cx="240" cy="284" r="7"/></g>
 <g fill="#8A5A10"><rect x="92" y="210" width="8" height="70" rx="3"/><rect x="200" y="210" width="8" height="70" rx="3"/><rect x="56" y="284" width="8" height="90" rx="3"/><rect x="236" y="284" width="8" height="90" rx="3"/></g>
 <g transform="translate(150 240)" fill="#160408">
  <circle cx="0" cy="-42" r="12"/>
  <path d="M0 -30 c-16 0 -22 14 -20 30 l-8 56 h56 l-8 -56 c2 -16 -4 -30 -20 -30Z"/>
 </g>
 <text x="150" y="382" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#F8D98A" opacity="0.95">OPENING NIGHT</text>
</svg>""",
        # --- Golden Age Cinema: spotlight, vintage camera, film reel ---
        "goldenage": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="ga-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E0A04"/><stop offset="0.6" stop-color="#3A2C12"/><stop offset="1" stop-color="#8A6A2A"/></linearGradient>
  <radialGradient id="ga-gl" cx="0.5" cy="0.35" r="0.6"><stop offset="0" stop-color="#F6E08A" stop-opacity="0.7"/><stop offset="1" stop-color="#F6E08A" stop-opacity="0"/></radialGradient>
 </defs>
 <rect width="300" height="400" fill="url(#ga-bg)"/>
 <path d="M150 40 L70 330 L230 330 Z" fill="url(#ga-gl)"/>
 <g transform="translate(150 120)" fill="#F6E08A" opacity="0.9">
  <circle r="34" fill="none" stroke="#F6E08A" stroke-width="6"/>
  <circle r="6"/><circle cx="0" cy="-18" r="6"/><circle cx="17" cy="9" r="6"/><circle cx="-17" cy="9" r="6"/>
 </g>
 <g fill="#14100A" opacity="0.95">
  <circle cx="86" cy="238" r="20"/><circle cx="118" cy="238" r="16"/>
  <rect x="72" y="252" width="60" height="34" rx="6"/>
  <rect x="128" y="258" width="22" height="12" rx="4"/>
  <path d="M84 286 L70 350 M104 286 L104 350 M120 286 L134 350" stroke="#14100A" stroke-width="7"/>
 </g>
 <g transform="translate(206 268)" fill="#14100A">
  <circle cx="0" cy="-36" r="11"/>
  <path d="M0 -26 c-14 0 -20 12 -18 27 l-7 49 h50 l-7 -49 c2 -15 -4 -27 -18 -27Z"/>
 </g>
 <rect y="356" width="300" height="44" fill="#0E0A04" opacity="0.75"/>
 <text x="150" y="384" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#F6E08A" opacity="0.95">LIGHTS · CAMERA · MAGIC</text>
</svg>""",
    }
    return art.get(key, "")


def poster_html(film: dict, selected: bool = False, synopsis: bool = False) -> str:
    badge = '<div class="mp-cast-badge">YOU STAR ★</div>' if selected else ""
    sel = " selected" if selected else ""
    body_extra = (
        f'<p class="mp-synopsis">{film["synopsis"]}</p>' if synopsis
        else f'<p class="mp-logline">{film["logline_en"]}</p>'
    )
    html = f"""
    <div class="mp-poster{sel}" style="--c1:{film['c1']};--c2:{film['c2']};--c3:{film['c3']}">
      {badge}
      <div class="mp-poster-art">
        <div class="mp-poster-no">FILM {film['no']}</div>
        {poster_art(film['key'])}
        <div class="mp-poster-vignette"></div>
      </div>
      <div class="mp-poster-ribbon">{film['genre_en']}</div>
      <div class="mp-poster-body">
        <h3>{film['title_en']}</h3>
        <div class="mp-poster-th">{film['title_th']}</div>
        {body_extra}
        <div class="mp-tags">{film['tags']}</div>
      </div>
    </div>
    """
    return _tidy(html)


def hero_fan(films: list) -> str:
    rotations = [("-14deg", "18px"), ("-5deg", "2px"), ("5deg", "2px"), ("14deg", "18px")]
    cards = "".join(
        f'<div class="mp-fan-card" style="--r:{r};--y:{y}">{poster_art(f["key"])}'
        f'<span>{f["title_en"]}</span></div>'
        for f, (r, y) in zip(films, rotations)
    )
    return _tidy(f'<div class="mp-fan">{cards}</div>')


def footer():
    st.markdown(
        '<div class="mp-footer">PREMIERE PICTURES · A BYTEPLUS SEEDANCE 2.0 EXPERIENCE · EST. 2026</div>',
        unsafe_allow_html=True,
    )
