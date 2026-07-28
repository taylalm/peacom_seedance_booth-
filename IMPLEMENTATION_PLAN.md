# MAHA PICTURES · มหาพิคเจอร์ส — Implementation Plan

A Streamlit booth app for Thai marketing events showcasing **Seedance 2.0** (BytePlus ModelArk).

**Concept:** a retro-modern **Thai movie studio**. The visitor walks into a casting office, gets cast as the lead of a Thai blockbuster, picks their film from a wall of hand-painted-style posters, receives a premiere ticket, and their 15-second "epic" premieres on the booth's *Now Showing* marquee — and in their inbox.

This matches the *capabilities* of the original VN demo (portrait capture → themed worlds → lead form → async render → gallery → email) but shares none of its branding, copy, or layout. The original is a black-and-blue editorial "Seedance Studio"; this is a warm, poster-art **film studio fantasy** built on Thailand's iconic hand-painted cinema billboard tradition.

---

## 1. Capability parity (what we keep functionally, nothing else)

| Capability (from original) | Maha Pictures equivalent |
|---|---|
| Landing with begin + gallery entry | Studio lobby with **ACTION! →** and **NOW SHOWING →** |
| Photo upload / webcam capture, quality guidance | Step 1 · **CASTING CALL** |
| Exactly 4 fixed themes w/ hidden prompts | Step 2 · **THE POSTER WALL** (4 movie posters) |
| Required lead form (name/company/title/phone/email) | Step 3 · **THE PREMIERE TICKET** |
| Async render → email delivery, visitor doesn't wait | Step 4 · **IN PRODUCTION** ticket stub → email "premiere invitation" |
| Public gallery of finished videos | **NOW SHOWING** marquee wall |
| Fixed spec 15 s · 720p · 9:16, ModelArk AP-Southeast | Same (framed as "ONE REEL · 15 SEC · VERTICAL CUT") |

---

## 2. Creative direction

### Identity
- **Name:** MAHA PICTURES (มหา = grand/epic, as in มหากาพย์ "epic saga") — logo lockup: a golden Garuda-wing film reel.
- **Landing headline (own copy, not the original's):**
  **"หนังเรื่องนี้… คุณแสดงนำ"** / *"This one stars you."*
- **Tagline:** `ONE SHOT · ONE EPIC · หนึ่งช็อต หนึ่งตำนาน`
- **Voice:** playful Thai-blockbuster hype — trailer-announcer energy ("IN A WORLD… somewhere in Bangkok…"), not minimalist gallery prose.

### Visual system (deliberately opposite of the original)
- **Palette:** aged-poster **cream `#F4E9D8`** background, **vermillion red `#C8321E`**, **marigold gold `#E8A020`**, **teal ink `#1E5A5A`**, charcoal text — warm daylight poster art vs. the original's near-black night UI.
- **Type:** big Thai display type — **Chonburi** or **Charmonman/Srisakdi** for Thai headlines, a bold slab/condensed (e.g., **Archivo Black / Bebas-style**) for English; body in **Taviraj / Noto Sans Thai**. No serif-italic editorial styling, no monospace micro-labels.
- **Texture & ornament:** subtle halftone/paper grain, sunburst rays behind hero art, ticket perforations, marquee bulbs (CSS), starburst "ใหม่ล่าสุด!" badges — the visual grammar of Thai billboard painting and vintage ticket stubs.
- **Layout grammar:** centered big-poster compositions and horizontal poster rails — not the original's left-text/right-panel split. Progress shown as a **filmstrip stepper** (4 sprocket frames that fill in) instead of `STEP 0X/0X` corner text.

---

## 3. Screens & flow

```
Lobby ── ACTION! → 1 CASTING CALL → 2 POSTER WALL → 3 PREMIERE TICKET → 4 IN PRODUCTION (stub)
  │                                                                            │ async worker
  └── NOW SHOWING → Marquee gallery  ◄── film saved ──┬── premiere email ◄─────┘
Hidden: BACKLOT (admin)
```

Single Streamlit app; wizard on `st.session_state["scene"]`, `st.navigation` pages for Lobby/Now Showing/Backlot, sidebar hidden (kiosk).

### Lobby (landing)
Full-width poster composition: sunburst rays, the four film posters fanned like a hand of cards, marquee-style title, headline **"หนังเรื่องนี้… คุณแสดงนำ"** with English subtitle. Two CTAs: **🎬 ACTION! เริ่มเลย** (primary, red with gold border) and **NOW SHOWING · รอบฉาย** (ghost). Footer strip: `MAHA PICTURES · POWERED BY SEEDANCE 2.0 ON BYTEPLUS MODELARK · ONE REEL · 15 SEC`.

### Scene 1 · CASTING CALL — "ส่งหน้ามาแคสต์ / Send in your headshot"
- Framed as an audition: a **director's clapperboard card** holds the capture area.
- `st.tabs(["📸 ถ่ายตรงนี้ / SHOOT HERE", "🖼 อัปโหลด / UPLOAD"])` — camera-first (booth context), upload second (reverse of the original).
- `st.camera_input` / `st.file_uploader` (JPG/PNG/WEBP); validate ≥1024 px short side with Pillow; friendly retake copy ("ไฟไม่พอ! หันหน้าเข้าแสงหน่อยครับ / More light please, superstar").
- Accepted photo renders inside a **polaroid "casting card"** — stamped `CAST ✓ นักแสดงนำ (LEADING ROLE)` — with **RE-SHOOT** underneath. Filmstrip stepper frame 1 fills in. CTA: **ไปเลือกหนัง → PICK YOUR FILM**.

### Scene 2 · THE POSTER WALL — "เรื่องไหนคือตำนานของคุณ? / Which epic is yours?"
Four **vertical 2:3 movie-poster cards** in a row (wrap 2×2 on small screens) — poster art + Thai movie-title typography + genre ribbon + one-line logline + **จองบท / TAKE THIS ROLE** button. Selecting flips the card to show "YOU" on the poster (visitor's casting photo composited in a starburst). Each poster carries a hidden Seedance prompt (§4).

### Scene 3 · THE PREMIERE TICKET — "กรอกบัตรพรีเมียร์ / Fill in your premiere ticket"
The form *is* a **golden admission ticket**: a wide perforated ticket card with the chosen film's title on the stub and blanks to fill —
ชื่อ-นามสกุล / Full name · บริษัท / Company · ตำแหน่ง / Job title · เบอร์โทร / Phone (`+66 8x xxx xxxx`) · อีเมล / Email — all required, plus a **PDPA consent** checkbox (required; Thailand's privacy law covers the portrait + contact processing).
Copy sets async expectations: "ฉายเสร็จเมื่อไหร่ ส่งตรงถึงอีเมลคุณ — ไม่ต้องรอหน้าจอ / When your film wraps, it goes straight to your inbox. No waiting around."
CTA: **🎬 เปิดกล้อง! / ROLL CAMERA →**

### Scene 4 · IN PRODUCTION — the tear-off stub
On submit: lead + job persisted, worker queued, and the screen **tears the ticket** (CSS animation): visitor keeps a stub with **ticket no. `MP-0042`**, film title, and "world premiere: จอ NOW SHOWING + อีเมลของคุณ ภายใน ~5 นาที". Confetti (`st.balloons` or CSS), auto-return to Lobby after ~20 s for the next visitor.

### NOW SHOWING — marquee gallery
Booth big-screen page: **marquee header with animated CSS lightbulbs**, below it a poster-wall grid of finished films — each a 9:16 video in a poster frame captioned like a billing block: **first name (ดารานำ)** · film title · ticket no. Newest premiere slides in with a `เข้าฉายแล้ว!` starburst. Auto-refresh every ~10 s.

### BACKLOT — admin (password-gated)
Leads table + CSV export, render queue log (queued/rendering/done/failed + retry), delete film, API health check.

---

## 4. The four films (posters + hidden Seedance prompts)

Genre spread: action-fantasy epic · neon action · romance · feel-good comedy — chosen for Thai audiences, not mapped to the original's slots.

### 🎬 1 · นาคาผงาด — *NAGA RISING* `แอ็กชันแฟนตาซี · EPIC`
Logline: *One fighter. One storm. The Naga answers.*
> **Prompt:** The person from the reference image is a legendary Muay Thai warrior in a mongkhon headband and pra jiad armbands, in a rain-swept ancient Thai temple courtyard at dusk. Shot 1: close-up — they exhale, golden energy coiling around their fists. Shot 2: they unleash a flying knee and a colossal luminous golden Naga serpent bursts from the storm clouds, spiraling through lightning behind them. Shot 3: warrior and Naga roar toward camera, rain frozen mid-air, temple bells tolling. Epic taiko-and-phin score, live-action-anime VFX, heroic color grade. 15 seconds.

### 🎬 2 · เยาวราช 2099 — *YAOWARAT 2099* `ไซเบอร์พังก์ · NEON ACTION`
Logline: *Green light. Chinatown goes supersonic.*
> **Prompt:** The person from the reference image pilots a hover-tuk-tuk through cyberpunk Bangkok Chinatown at night, rain-slicked streets mirroring pink and cyan neon Thai signage. Shot 1: cockpit close-up, neon sliding across their determined face as the countdown hits green. Shot 2: low chase cam — the tuk-tuk drifts a corner past holographic street-food stalls, sparks and light trails. Shot 3: slow-motion hero shot, they glance at camera and grin as the city streaks past. Pounding synthwave with engine roar. 15 seconds.

### 🎬 3 · แสงพันดวง — *A THOUSAND LIGHTS* `โรแมนติก · FESTIVAL`
Logline: *At Yi Peng, one wish takes flight.*
> **Prompt:** The person from the reference image, in elegant traditional Lanna clothing, stands riverside at Chiang Mai's Yi Peng festival at night. Shot 1: warm close-up — their face lit by the paper lantern in their hands, eyes full of a wish. Shot 2: they release it; camera tilts up as it joins thousands of lanterns rising, soft fireworks blooming beyond. Shot 3: they laugh among friends setting krathong onto the glittering river, candlelight bokeh everywhere. Tender acoustic score with festival ambience, golden romantic grade. 15 seconds.

### 🎬 4 · สงกรานต์มหาสนุก — *SONGKRAN SUPERSOAKED* `คอมเมดี้ · FEEL-GOOD`
Logline: *The nation's biggest water fight has a new champion.*
> **Prompt:** The person from the reference image is the joyful hero of a Songkran street water battle on a sunlit Bangkok road. Shot 1: they cock a rainbow water blaster and grin at camera, floral shirt, chalk-powder cheeks. Shot 2: epic slow-motion — they spin through crossing arcs of water, droplets sparkling like diamonds in golden light, crowd cheering. Shot 3: they strike a victory pose atop a pickup truck as friends shower them with glittering spray. Upbeat luk thung–pop remix, pure celebration. 15 seconds.

**Alternate reels:** ตลาดน้ำมหาภัย / *Floating Market Heist* (action-comedy boat chase), มหานครผู้พิทักษ์ / *Guardian of Mahanakhon* (Khon-mask superhero), อันดามันดรีม / *Andaman Dream* (longtail-boat island epic).

Prompt rules: person referenced explicitly; 3-shot structure for 15 s; per-shot camera + lighting language; audio direction (Seedance 2.0 generates audio); no brands or on-screen text; ≤ ~150 words. Catalog is data in `core/films.py` (`key, title_th, title_en, genre, logline, poster, prompt`) so marketing can tune prompts without code changes.

---

## 5. Seedance 2.0 integration (BytePlus ModelArk)

- Base URL `https://ark.ap-southeast.bytepluses.com/api/v3` · `ARK_API_KEY` auth · model `dreamina-seedance-2-0-260128`.

```python
from byteplussdkarkruntime import Ark
client = Ark(api_key=st.secrets["ARK_API_KEY"])

task = client.content_generation.tasks.create(
    model=MODEL_ID,
    content=[
        {"type": "text", "text": film["prompt"]},
        {"type": "image_url",
         "image_url": {"url": f"data:image/jpeg;base64,{face_b64}"},
         "role": "reference_image"},   # cast the person into new scenes
    ],
    ratio="9:16", duration=15, resolution="720p",
    generate_audio=True, watermark=False,
)
# poll client.content_generation.tasks.get(task_id=...) until succeeded/failed
```

- Fixed spec **15 s · 720p · 9:16** (vertical = poster-shaped, phone-shareable).
- Result URLs are temporary — worker downloads the MP4 immediately.
- **Real-face i2v is an account entitlement on ModelArk** (the VN demo advertises it) — request the same enablement for the Thailand account first; test with real portraits on day one.
- Limits ~2 QPS / **3 concurrent tasks** → worker semaphore caps in-flight jobs at 3; one retry on failure, then `failed` (visible in Backlot).

## 6. Async production pipeline

`core/worker.py`: single consumer thread + `queue.Queue`, started once per server process. On ROLL CAMERA: persist lead + job (`queued`) → thread submits task → polls every 10 s → downloads MP4 to `gallery/` → writes metadata → sends premiere email → `done`. UI never blocks; ticket stub screen returns the booth to the Lobby.

## 7. Premiere email

Bilingual HTML styled as a **premiere invitation**: golden ticket header, "🎬 คุณ {first_name} — หนังของคุณเข้าฉายแล้ว! / Your film has premiered!", film title + logline, MP4 attached (15 s 720p ≈ 8–15 MB) + hosted link fallback, closing line "ขอบคุณที่ร่วมแคสต์กับ Maha Pictures · Powered by Seedance 2.0 on BytePlus". SMTP app-password or SendGrid/Resend; `email_sent` recorded per lead.

## 8. Data & storage

- `data/leads.csv` — timestamp, ticket no, name, company, job title, phone, email, film, task_id, status, video_path, consent, email_sent. Exported from Backlot (marketing's takeaway).
- `gallery/MP-XXXX.mp4` + `gallery/metadata.json`.
- Portraits kept in memory for the render only — not persisted (PDPA-friendly default).
- Secrets in `.streamlit/secrets.toml`: `ARK_API_KEY`, `SMTP_*`, `ADMIN_PASSWORD`.

## 9. Project structure

```
seedance_demo_app/
├── app.py                    # st.navigation: lobby / now_showing / backlot
├── views/
│   ├── lobby.py              # landing + 4-scene wizard
│   ├── now_showing.py        # marquee gallery
│   └── backlot.py            # admin
├── core/
│   ├── films.py              # 4 films + alternates, prompts as data
│   ├── seedance.py           # Ark client: create/poll/download
│   ├── worker.py             # production queue → save → email
│   ├── emailer.py            # premiere invitation template + SMTP
│   ├── storage.py            # leads.csv + gallery metadata
│   └── ui.py                 # CSS: poster palette, filmstrip stepper, ticket, marquee
├── assets/                   # logo, 4 poster art images, fonts, textures
├── gallery/                  # finished films (gitignored)
├── data/                     # leads.csv (gitignored)
├── .streamlit/config.toml    # cream/red/gold theme, wide layout
├── .streamlit/secrets.toml   # gitignored
└── requirements.txt          # streamlit, byteplus sdk, pillow, requests
```

## 10. Milestones

1. **Design system + shell** — palette/fonts/CSS components (poster card, ticket, filmstrip stepper, marquee), lobby + 4 scenes with static data (1 d)
2. **Casting + poster wall + ticket form** — camera/upload with validation, polaroid casting card, poster selection state, PDPA form (0.5 d)
3. **Production pipeline** — Seedance client, worker queue, gallery save; live render test with real key + real face (1 d, needs entitled `ARK_API_KEY`)
4. **Premiere email + Now Showing + Backlot** — invitation template, marquee auto-refresh, CSV export (0.5 d)
5. **Dress rehearsal** — end-to-end on the booth machine (camera on localhost/HTTPS, venue Wi-Fi), timing, prompt tuning with marketing (before event)

## 11. Risks & checks

- **Real-face entitlement** on the Thai ModelArk account gates everything — confirm first.
- **Render time vs booth flow** — async email de-risks it; measure real 15 s/720p times and set the stub's "~5 min" honestly.
- **3-concurrent ceiling** — queue grows at peak; stub shows ticket position; ask BytePlus about a second key if needed.
- **Poster art assets** — 4 poster images needed for the wall; generate with an image model (e.g., Seedream) in the hand-painted billboard style, or commission from the design team.
- **Hosting** — booth laptop + localhost is most reliable for camera + no cold starts; Streamlit Cloud (private) if remote staff need the Now Showing link. Support both.
- **PDPA** — consent copy reviewed by the local team; portraits not persisted; lead handling documented.
