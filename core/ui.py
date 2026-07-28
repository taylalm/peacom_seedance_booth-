"""Premiere Pictures design system — classic cinema-poster aesthetic.

Palette: aged-poster cream / vermillion red / marigold gold / teal ink.
Type: Chonburi (Thai display), Archivo Black (EN slab), Taviraj (body),
Prompt (UI labels). All styling injected as one CSS block.
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Archivo+Black&family=Taviraj:ital,wght@0,400;0,500;0,600;1,400&family=Prompt:wght@400;500;600&family=Noto+Sans+Thai:wght@400;600&display=swap');

:root {
  --cream:   #100D0A;   /* canvas: deep warm black */
  --cream-2: #1C1712;   /* raised surfaces */
  --paper:   #1E1913;   /* cards */
  --coal:    #0A0806;   /* darkest surfaces (film strip, marquee) */
  --verm:    #D93A20;   /* curtain crimson */
  --verm-d:  #7E1B0C;
  --gold:    #E8A020;
  --gold-l:  #F6C55C;
  --teal:    #C8A96A;   /* champagne secondary text */
  --ink:     #F2E8D5;   /* main text: warm cream on dark */
}

/* ---------- canvas ---------- */
.stApp {
  background:
    radial-gradient(circle at 50% -5%, rgba(246,197,92,.14), transparent 48%),
    radial-gradient(circle at 85% 95%, rgba(200,50,30,.12), transparent 42%),
    radial-gradient(rgba(246,197,92,.05) 1px, transparent 1.4px),
    var(--cream);
  background-size: auto, auto, 14px 14px, auto;
  color: var(--ink);
}
header[data-testid="stHeader"] { display: none; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 1.4rem; padding-bottom: 3rem; max-width: 1180px; }

h1, h2, h3 { font-family: 'Playfair Display', 'Archivo Black', serif !important; color: var(--ink); }
p, li, label, .stMarkdown { font-family: 'Taviraj', 'Noto Sans Thai', serif; }

/* ---------- header bar ---------- */
.mp-header {
  display: flex; align-items: baseline; justify-content: space-between;
  border-bottom: 3px double var(--ink); padding-bottom: .55rem; margin-bottom: 1.1rem;
}
.mp-logo { font-family: 'Archivo Black', sans-serif; font-size: 1.5rem; letter-spacing: .02em; }
.mp-logo .reel { color: var(--verm); }
.mp-logo em {
  font-family: 'Playfair Display', serif; font-style: normal; font-size: .95rem;
  color: var(--teal); margin-left: .5rem;
}
.mp-spec {
  font-family: 'Prompt', sans-serif; font-size: .68rem; letter-spacing: .18em;
  color: var(--teal); text-align: right;
}

/* ---------- filmstrip stepper ---------- */
.mp-strip {
  display: flex; gap: 10px; background: var(--coal); border-radius: 12px;
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
  border-style: solid; border-color: var(--gold-l); color: #171207;
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
  color: #171207; background: var(--gold-l);
  border: 2px solid #171207; border-radius: 999px; padding: .3rem 1.1rem;
  box-shadow: 3px 3px 0 rgba(0,0,0,.5);
}

/* fanned mini posters */
.mp-fan { position: relative; z-index: 1; display: flex; justify-content: center; margin: 1.6rem 0 .8rem; height: 190px; }
.mp-fan-card {
  position: relative; width: 118px; height: 168px; border-radius: 10px; margin: 0 -12px; overflow: hidden;
  border: 3px solid #EFE6D2; box-shadow: 0 12px 26px rgba(0,0,0,.6);
  display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
  transform: rotate(var(--r)) translateY(var(--y));
}
.mp-fan-card svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.mp-fan-card span {
  position: relative; z-index: 1; font-family: 'Playfair Display', serif; font-size: .6rem; color: #FFF8EC;
  text-shadow: 0 2px 5px rgba(0,0,0,.8); padding: 0 6px 8px; text-align: center; line-height: 1.2;
}

/* ---------- poster cards ---------- */
.mp-poster {
  background: var(--paper); border: 3px solid var(--gold); border-radius: 14px;
  overflow: hidden; box-shadow: 7px 7px 0 rgba(0,0,0,.55);
  margin-bottom: .7rem; position: relative;
}
.mp-poster.selected { outline: 4px solid var(--gold); outline-offset: 2px; }
.mp-poster-art {
  aspect-ratio: 3 / 4; position: relative; overflow: hidden; background: var(--coal);
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
  background: var(--gold-l); color: #171207; border: 2px solid #171207;
  border-radius: 999px; padding: .2rem .65rem;
  font-family: 'Prompt', sans-serif; font-size: .66rem; font-weight: 600; letter-spacing: .08em;
  transform: rotate(6deg); box-shadow: 2px 2px 0 rgba(0,0,0,.5);
}
.mp-poster-ribbon {
  background: var(--coal); color: var(--gold-l); text-align: center;
  font-family: 'Prompt', sans-serif; font-size: .66rem; letter-spacing: .16em; padding: 5px 6px;
}
.mp-poster-body { padding: .7rem .85rem .85rem; }
.mp-poster-body h3 {
  margin: 0; font-family: 'Archivo Black', sans-serif; font-size: 1.12rem;
  letter-spacing: .01em; line-height: 1.15; color: var(--ink);
}
.mp-poster-th {
  font-family: 'Playfair Display', serif; font-size: 1.02rem; color: var(--verm); margin: .1rem 0 .4rem;
}
.mp-logline { font-size: .9rem; font-style: italic; color: #C9BCA8; margin: 0 0 .35rem; min-height: 2.4em; }
.mp-synopsis { font-size: .82rem; line-height: 1.5; color: #BDB09A; margin: 0 0 .5rem; }
.mp-tags { font-family: 'Prompt', sans-serif; font-size: .62rem; letter-spacing: .14em; color: var(--teal); }

/* ---------- casting polaroid ---------- */
.st-key-casting-card {
  position: relative; background: var(--paper); border: 1px solid #3A3226;
  padding: 16px 16px 10px; transform: rotate(-1.6deg);
  box-shadow: 0 14px 28px rgba(0,0,0,.6); border-radius: 4px;
}
.st-key-casting-card img { border: 1px solid #3A3226; }
.mp-stamp {
  position: absolute; top: 24px; right: 20px; z-index: 5; transform: rotate(10deg);
  border: 3px solid var(--verm); color: var(--verm); border-radius: 8px;
  padding: .25rem .7rem; background: rgba(12,9,6,.85);
  font-family: 'Archivo Black', sans-serif; font-size: .78rem; letter-spacing: .1em;
  text-align: center;
}
.mp-stamp small { display: block; font-family: 'Prompt', sans-serif; font-size: .6rem; letter-spacing: .16em; }
.mp-polaroid-caption {
  font-family: 'Playfair Display', serif; text-align: center; color: var(--ink);
  font-size: .85rem; padding-top: .5rem;
}

/* clapperboard headline */
.mp-clap {
  display: inline-block; background: var(--coal); color: var(--ink);
  border-radius: 10px 10px 4px 4px; padding: .45rem 1.1rem .5rem; margin-bottom: .8rem;
  font-family: 'Prompt', sans-serif; font-size: .72rem; letter-spacing: .22em;
  background-image: repeating-linear-gradient(115deg,
    var(--gold-l) 0 14px, var(--coal) 14px 28px);
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
  box-shadow: 7px 7px 0 rgba(0,0,0,.55);
}
.mp-ticket-head {
  display: flex; justify-content: space-between; align-items: baseline;
  border-bottom: 2px dashed rgba(43,35,32,.45); padding-bottom: .55rem; margin-bottom: .8rem;
}
.mp-ticket-head .adm { font-family: 'Archivo Black', sans-serif; font-size: .72rem; letter-spacing: .22em; color: var(--verm-d); }
.mp-ticket-head .film { font-family: 'Playfair Display', serif; font-size: 1.05rem; }
.st-key-ticket-card .stTextInput input {
  background: var(--paper); border: 2px solid var(--ink); border-radius: 8px;
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif;
}
.st-key-ticket-card .stTextInput label, .st-key-ticket-card .stCheckbox label {
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif !important; font-weight: 600;
  color: #171207 !important;
}
.st-key-ticket-card [data-testid="stForm"] { border: none; padding: 0; }

/* ---------- ticket stub (production) ---------- */
.mp-stub {
  max-width: 560px; margin: 1rem auto; position: relative;
  background: linear-gradient(135deg, #F9E9BE, var(--gold-l) 55%, #EFB63C);
  border: 3px solid var(--ink); border-radius: 16px; padding: 1.4rem 1.7rem;
  box-shadow: 7px 7px 0 rgba(0,0,0,.55); text-align: center;
  transform: rotate(-1.2deg);
}
.mp-stub .no { font-family: 'Archivo Black', sans-serif; font-size: 2rem; color: var(--verm-d); letter-spacing: .06em; }
.mp-stub .divider { border-top: 2px dashed rgba(43,35,32,.45); margin: .8rem 0; }
.mp-stub .meta { font-family: 'Prompt', sans-serif; font-size: .74rem; letter-spacing: .16em; color: #171207; }

/* ---------- marquee (now showing) ---------- */
.mp-marquee {
  background: var(--coal); border: 5px solid var(--gold); border-radius: 18px;
  padding: 1.5rem 1rem 1.6rem; text-align: center; margin-bottom: 1.4rem;
  box-shadow: 0 0 34px rgba(232,160,32,.35), 7px 7px 0 rgba(0,0,0,.55);
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
  text-align: center; border: 3px dashed rgba(242,232,213,.28); border-radius: 16px;
  padding: 3rem 1rem; color: #9A8C78; font-style: italic;
}

/* gallery poster frame */
.mp-showcard {
  background: var(--paper); border: 3px solid var(--gold); border-radius: 12px;
  padding: 10px 10px 6px; box-shadow: 6px 6px 0 rgba(0,0,0,.55); margin-bottom: 1rem;
}
.mp-billing { text-align: center; font-family: 'Prompt', sans-serif; font-size: .7rem; letter-spacing: .12em; color: var(--ink); padding: .45rem 0 .3rem; }
.mp-billing b { font-family: 'Playfair Display', serif; font-size: .85rem; letter-spacing: 0; }

/* ---------- footer strip ---------- */
.mp-footer {
  margin-top: 2.2rem; border-top: 3px double var(--ink); padding-top: .6rem;
  text-align: center; font-family: 'Prompt', sans-serif; font-size: .64rem;
  letter-spacing: .26em; color: var(--teal);
}

/* ---------- buttons ---------- */
.stButton > button, .stFormSubmitButton > button {
  font-family: 'Playfair Display', 'Prompt', serif !important;
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
  background: #2E2820 !important; color: #7A6E5E !important;
  border-color: #4A4234 !important; box-shadow: none !important;
}

/* ---------- tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: .4rem; border-bottom: 2px solid var(--ink); }
.stTabs [data-baseweb="tab"] {
  font-family: 'Prompt', 'Noto Sans Thai', sans-serif; font-weight: 600;
  background: var(--cream-2); border-radius: 10px 10px 0 0; padding: .45rem 1rem;
  color: var(--ink);
}
.stTabs [aria-selected="true"] { background: var(--coal) !important; color: var(--gold-l) !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

[data-testid="stFileUploaderDropzone"] {
  background: var(--paper); border: 2px dashed var(--ink); border-radius: 12px;
}
[data-testid="stCameraInput"] button { border-radius: 12px; }

.st-key-ticket-card, .st-key-ticket-card p, .st-key-ticket-card .film { color: #171207; }
.mp-stub { color: #171207; }
.mp-stub h1, .mp-stub h2, .mp-stub h3 { color: #171207; }

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
        # --- Temple of Gold: jungle ruins, idol in sunbeam, vines ---
        "adventure": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="ad-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#06180C"/><stop offset="0.6" stop-color="#14401E"/><stop offset="1" stop-color="#2E7D32"/></linearGradient>
  <linearGradient id="ad-beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6E08A" stop-opacity="0.65"/><stop offset="1" stop-color="#F6E08A" stop-opacity="0.05"/></linearGradient>
 </defs>
 <rect width="300" height="400" fill="url(#ad-bg)"/>
 <g fill="#04120A" opacity="0.9">
  <rect x="10" y="60" width="34" height="300" rx="4"/><rect x="256" y="60" width="34" height="300" rx="4"/>
  <rect x="0" y="40" width="54" height="22" rx="4"/><rect x="246" y="40" width="54" height="22" rx="4"/>
  <path d="M60 396 L84 320 L108 396 Z" opacity="0.7"/><path d="M196 396 L220 320 L244 396 Z" opacity="0.7"/>
 </g>
 <g stroke="#0E2E14" stroke-width="5" fill="none" opacity="0.9">
  <path d="M60 0 Q80 90 60 180 M240 0 Q225 70 244 150 M110 0 Q118 50 108 100"/>
 </g>
 <g fill="#3E8E44" opacity="0.85"><ellipse cx="60" cy="182" rx="14" ry="7"/><ellipse cx="243" cy="152" rx="12" ry="6"/><ellipse cx="108" cy="102" rx="10" ry="5"/></g>
 <path d="M150 30 L102 340 L198 340 Z" fill="url(#ad-beam)"/>
 <g transform="translate(150 262)">
  <rect x="-52" y="52" width="104" height="26" rx="5" fill="#0A2410"/>
  <rect x="-42" y="34" width="84" height="18" rx="4" fill="#123618"/>
  <g fill="#F6C55C" stroke="#8A5A10" stroke-width="1.5">
   <rect x="-14" y="-6" width="28" height="40" rx="6"/>
   <circle cx="0" cy="-16" r="12"/>
   <path d="M-14 6 L-26 22 M14 6 L26 22" stroke-width="4" fill="none"/>
  </g>
 </g>
 <g fill="#F6E08A" opacity="0.9"><circle cx="132" cy="180" r="2"/><circle cx="168" cy="150" r="2"/><circle cx="150" cy="210" r="2.5"/><circle cx="180" cy="230" r="2"/></g>
 <rect y="356" width="300" height="44" fill="#04120A" opacity="0.8"/>
 <text x="150" y="384" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#F6E08A" opacity="0.95">THE MAP WAS REAL</text>
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
        # --- Dance Fever: neon floor, mid-spin silhouette, crowd ---
        "dance": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="dc-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0C0518"/><stop offset="0.6" stop-color="#3A1258"/><stop offset="1" stop-color="#7A2AB0"/></linearGradient>
  <radialGradient id="dc-gl" cx="0.5" cy="0.62" r="0.55"><stop offset="0" stop-color="#57E0F0" stop-opacity="0.45"/><stop offset="1" stop-color="#57E0F0" stop-opacity="0"/></radialGradient>
 </defs>
 <rect width="300" height="400" fill="url(#dc-bg)"/>
 <rect width="300" height="400" fill="url(#dc-gl)"/>
 <g opacity="0.8">
  <path d="M40 0 L80 190 L20 190 Z" fill="#57E0F0" opacity="0.14"/>
  <path d="M260 0 L280 190 L220 190 Z" fill="#FE7AC8" opacity="0.14"/>
 </g>
 <g fill="#0A0412" opacity="0.85">
  <circle cx="40" cy="300" r="12"/><path d="M28 312 h24 v46 h-24 Z"/>
  <circle cx="262" cy="296" r="12"/><path d="M250 308 h24 v50 h-24 Z"/>
  <circle cx="86" cy="322" r="10"/><path d="M76 332 h20 v34 h-20 Z"/>
  <circle cx="216" cy="320" r="10"/><path d="M206 330 h20 v36 h-20 Z"/>
 </g>
 <g transform="translate(150 240) rotate(-8)" fill="#0C0518">
  <circle cx="6" cy="-64" r="14"/>
  <path d="M2 -50 c-18 4 -24 20 -18 38 l-26 20 10 12 28 -22 10 24 30 4 2 -14 -24 -4 -4 -26 c6 -18 4 -30 -8 -32Z"/>
 </g>
 <g stroke="#57E0F0" stroke-width="3" fill="none" opacity="0.8" stroke-linecap="round">
  <path d="M96 160 a70 70 0 0 1 60 -34 M204 260 a70 70 0 0 1 -50 40"/>
 </g>
 <ellipse cx="150" cy="332" rx="76" ry="10" fill="#57E0F0" opacity="0.2"/>
 <rect y="356" width="300" height="44" fill="#0C0518" opacity="0.85"/>
 <text x="150" y="384" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#57E0F0" opacity="0.95">OWN THE FLOOR</text>
</svg>""",
        # --- Sci-Fi Epic: nebula, ringed planet, starship ---
        "scifi": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="sf-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#03051A"/><stop offset="0.55" stop-color="#0A1240"/><stop offset="1" stop-color="#1E3CA8"/></linearGradient>
  <radialGradient id="sf-neb" cx="0.7" cy="0.25" r="0.5"><stop offset="0" stop-color="#57E0F0" stop-opacity="0.5"/><stop offset="1" stop-color="#57E0F0" stop-opacity="0"/></radialGradient>
  <radialGradient id="sf-pl" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#8AE0F0"/><stop offset="1" stop-color="#1E64B0"/></radialGradient>
 </defs>
 <rect width="300" height="400" fill="url(#sf-bg)"/>
 <ellipse cx="210" cy="100" rx="130" ry="90" fill="url(#sf-neb)"/>
 <g fill="#EAF7FF"><circle cx="40" cy="50" r="2"/><circle cx="90" cy="90" r="1.5"/><circle cx="250" cy="40" r="2"/><circle cx="270" cy="150" r="1.5"/><circle cx="60" cy="160" r="1.5"/><circle cx="150" cy="60" r="1.5"/><circle cx="30" cy="240" r="2"/><circle cx="270" cy="240" r="1.5"/><circle cx="120" cy="130" r="1"/></g>
 <g transform="translate(150 270)">
  <circle r="70" fill="url(#sf-pl)"/>
  <ellipse rx="112" ry="26" fill="none" stroke="#8AE0F0" stroke-width="6" opacity="0.7" transform="rotate(-16)"/>
  <path d="M-70 4 a70 70 0 0 0 140 -8" fill="#03051A" opacity="0.35"/>
 </g>
 <g transform="translate(92 148) rotate(38)">
  <path d="M0 -26 C7 -16 8 4 6 18 L-6 18 C-8 4 -7 -16 0 -26 Z" fill="#EAF7FF"/>
  <path d="M-6 8 L-16 22 L-6 18 Z" fill="#8AE0F0"/>
  <path d="M6 8 L16 22 L6 18 Z" fill="#8AE0F0"/>
  <circle cx="0" cy="-4" r="4.5" fill="#1E3CA8"/>
  <path d="M-3 19 L0 34 L3 19 Z" fill="#F6C55C"/>
 </g>
 <rect y="356" width="300" height="44" fill="#03051A" opacity="0.8"/>
 <text x="150" y="384" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#57E0F0" opacity="0.95">STARBOUND</text>
</svg>""",
        # --- Film Noir: streetlamp cone, fedora silhouette, rain ---
        "noir": """
<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
 <defs>
  <linearGradient id="nr-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060608"/><stop offset="0.7" stop-color="#1A1A20"/><stop offset="1" stop-color="#2E2E36"/></linearGradient>
  <linearGradient id="nr-cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D8D8E0" stop-opacity="0.55"/><stop offset="1" stop-color="#D8D8E0" stop-opacity="0.05"/></linearGradient>
 </defs>
 <rect width="300" height="400" fill="url(#nr-bg)"/>
 <g stroke="#8A8A98" stroke-width="1.5" opacity="0.5">
  <path d="M40 30 L34 60 M90 10 L84 40 M140 40 L134 70 M200 20 L194 50 M250 50 L244 80 M70 110 L64 140 M180 100 L174 130 M260 140 L254 170 M110 160 L104 190 M30 190 L24 220"/>
 </g>
 <rect x="196" y="60" width="8" height="290" fill="#0A0A0C"/>
 <path d="M200 60 Q170 58 168 78 L176 80 Q180 68 200 68 Z" fill="#0A0A0C"/>
 <ellipse cx="172" cy="84" rx="10" ry="6" fill="#F6E8B0"/>
 <path d="M172 88 L92 350 L252 350 Z" fill="url(#nr-cone)"/>
 <g transform="translate(160 268)" fill="#08080A">
  <ellipse cx="0" cy="-58" rx="26" ry="7"/>
  <path d="M-13 -60 a13 13 0 0 1 26 0 Z"/>
  <path d="M0 -50 c-18 0 -26 14 -24 32 l-10 60 h68 l-10 -60 c2 -18 -6 -32 -24 -32Z"/>
  <path d="M-24 -20 L-34 30 M24 -20 L34 30" stroke="#08080A" stroke-width="10" stroke-linecap="round"/>
 </g>
 <ellipse cx="160" cy="352" rx="70" ry="8" fill="#D8D8E0" opacity="0.14"/>
 <rect y="360" width="300" height="40" fill="#060608" opacity="0.85"/>
 <text x="150" y="386" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" fill="#D8D8E0" opacity="0.9">CASE CLOSED</text>
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
    rotations = [("-18deg", "30px"), ("-11deg", "14px"), ("-4deg", "3px"),
                 ("4deg", "3px"), ("11deg", "14px"), ("18deg", "30px")]
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
