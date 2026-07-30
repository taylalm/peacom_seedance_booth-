"""The Premiere Pictures film catalog — 6 Vietnamese movie-scene themes.

Each guest stars INSIDE a real movie scene set in Vietnam — a romantic ballroom
party, jungle adventure, phim-xưa period melodrama, Saigon noir, Vietnamese
horror, and the beloved đánh-ghen melodrama. English dialogue throughout; the
AI co-star and background characters are Vietnamese. 15s solo or 30s duo.
`c1/c2/c3` drive each poster's gradient (dark -> mid -> glow).
"""

FIXED_SPEC = {"ratio": "9:16", "duration": 15, "resolution": "720p"}

# Shared hard rules — every lesson learned across the booth apps, in one block.
_RULES = (
    " HARD RULES: Every character speaks ONLY in English at all times — never any other "
    "language, not a single word. Every spoken line is delivered ON CAMERA by the person "
    "visibly speaking it — lips, mouth and jaw in PERFECT 100% sync with every word of the "
    "audio; NEVER use voice-over, off-screen narration, or speech over a closed or still "
    "mouth. The video contains ONLY the characters explicitly described in this prompt — "
    "never invent, add, or reveal any extra person, stranger, or third figure that the "
    "prompt does not mention. Characters' eyes always look naturally and precisely at what "
    "they should — direct, aligned eye contact when characters speak to each other, eyes "
    "clearly focused on the other person's eyes; never crossed, drifting, or misaligned "
    "eyes. Prefer frontal or three-quarter camera angles that keep the faces toward the "
    "camera; avoid long side-profile shots. The footage must look like REAL live-action "
    "film shot on a professional cinema camera: physically-plausible practical lighting "
    "coming from actual visible light sources in the scene, true photographic shadows, "
    "natural skin texture — never a CGI, dreamlike, hazy, or artificially glowing look; "
    "absolutely NO lens flares, light streaks, sparks, embers, fireworks, glitter, or "
    "magical glowing particle effects of any kind — every flame, lamp and light in the "
    "scene burns small, steady and natural, and NEVER brightens, flares, sparks or "
    "shoots particles, especially at the beginning or end of the video. "
    "ABSOLUTE TEXT BAN: do NOT render any text anywhere in the video — no captions, "
    "subtitles, labels, watermarks or floating graphics, and NO letters, numbers, script, "
    "runes or inscriptions on ANY surface: walls, floors, stone, signs, papers, books, "
    "carvings, clothing and props are all completely free of any writing in any language; "
    "all clothing, props, sets and backdrops are plain and unbranded. If there is any background "
    "music it must be completely ORIGINAL instrumental audio generated brand-new for this "
    "video — no lyrics, no vocals, never any existing, famous, or copyrighted song or "
    "melody. Everything obeys real-world physics — bodies, hands and objects move exactly "
    "as they do in real life, with correct balance, weight, momentum and follow-through, "
    "no impossible or rubbery movement, no strange or unnatural motion of any kind. "
    "Image 1 is a FACE reference ONLY: take nothing from Image 1 except the face — the "
    "clothing, hairstyle-styling and accessories worn in the video always follow THIS "
    "prompt's wardrobe description, NEVER the clothing visible in the reference photo. "
    "CHARACTER IDENTITY STABILITY: each character keeps the exact same body, height, "
    "build, hair, and gender-presentation in every single frame — INCLUDING when seen "
    "from behind or at a distance; characters NEVER swap positions with each other, "
    "never trade places left/right, and never morph into a different person, even "
    "momentarily. "
    "WARDROBE CONTINUITY: every character's clothing, hat and accessories are exactly "
    "the same from the very first frame to the very last — nothing is ever added, "
    "removed, appears, disappears, or transforms mid-video; if a character wears a hat, "
    "it is on their head from frame one and stays firmly on throughout. "
    "SET CONTINUITY: the environment never changes state on its own — every door, gate, "
    "shutter, curtain and window keeps its exact initial position (open or closed) for "
    "the entire video, and buildings, furniture and background objects stay identical "
    "from first frame to last, unless the prompt explicitly describes a character or "
    "force changing them. "
    "Present the ENTIRE clip as a single continuous full-frame shot from one camera: no "
    "split-screen, no grids, tiles, collage or picture-in-picture. Natural realistic human "
    "movement with visible weight and effort, smooth animation, no flickering."
)

# appended to every SOLO prompt — face-lock + pacing + the shared rules
_SUFFIX = (
    _RULES + " Use the face in Image 1 as the only and exclusive face reference — the face "
    "must stay EXACTLY identical to Image 1 in every single frame: same facial structure, "
    "same features, same identity, with ZERO morphing, drifting or beautifying, even during "
    "fast motion; keep the face clearly visible to the camera as much as possible. Pace the "
    "dialogue so the final line is completely finished by second 12, then hold a natural "
    "closing beat — never cut off mid-sentence or mid-action. 15 seconds."
)

FILMS = [
    {
        "key": "ballroom", "no": "01", "emoji": "💃",
        "title_th": "ONE DANCE, ONE NIGHT", "title_en": "THE MIDNIGHT WALTZ",
        "genre_th": "ROMANCE", "genre_en": "ROMANCE · BALLROOM",
        "logline_en": "One party. One song. One unforgettable dance.",
        "synopsis": ("A romantic ballroom scene at a glamorous evening party — elegant gowns "
                     "and suits, warm chandelier light, and a slow, sweeping couple's dance "
                     "straight out of a romance film."),
        "tags": "BALLROOM · GOWN & VEST · ROMANCE",
        "c1": "#0E1030", "c2": "#4A3A8A", "c3": "#F6C55C",
        "prompt": ("A romantic movie scene at a glamorous evening party in a grand hotel "
                   "ballroom: warm chandelier light from visible chandeliers, round tables "
                   "with candles, elegantly dressed Vietnamese guests — women in evening "
                   "gowns, men in suits and vests — chatting softly at the edges of a "
                   "polished dance floor. Gentle original orchestral music plays. The person "
                   "in Image 1, dressed in elegant plain evening wear (a graceful gown or a "
                   "tailored suit with vest), steps onto the floor and dances a beautiful "
                   "flowing waltz like a trained ballroom dancer — LONG, sweeping gliding "
                   "steps that TRAVEL in wide circles around the floor, smooth full body "
                   "turns with real momentum, clothes flowing with the motion, never "
                   "dancing in one spot — face kept toward the camera in frontal or "
                   "three-quarter view. They finish with one graceful full spin, look "
                   "warmly into the camera and say in clear English: \"Some dances you "
                   "remember forever.\" — holding a soft smile as the music fades." + _SUFFIX),
    },
    {
        "key": "adventure", "no": "02", "emoji": "🗺️",
        "title_th": "THE LOST TEMPLE", "title_en": "TEMPLE OF GOLD",
        "genre_th": "ADVENTURE", "genre_en": "ADVENTURE · EPIC",
        "logline_en": "The map was real. So are the traps.",
        "synopsis": ("Deep in jungle ruins you dodge ancient traps, swing across a chasm and "
                     "lift the golden idol into a shaft of sunlight — a classic adventure-movie "
                     "treasure run."),
        "tags": "JUNGLE · TREASURE · TRAPS",
        "c1": "#0A2414", "c2": "#2E7D32", "c3": "#F6C55C",
        "prompt": ("A cinematic adventure-movie scene: ancient jungle temple ruins, shafts of "
                   "sunlight through the canopy over mossy stone. EXACTLY ONE person appears "
                   "in this entire video — the person in Image 1; no other human ever "
                   "appears, in the background or anywhere. Every stone or wall that moves "
                   "or falls does so only because a real physical force acts on it — a "
                   "stepped-on trigger plate, an impact, or its support visibly giving way "
                   "first; NOTHING collapses or rises by itself. The person in Image 1, in "
                   "rugged plain explorer gear, steps on an ancient trigger plate — it sinks "
                   "with a clunk, and the impact makes a nearby column's support give way so "
                   "it topples visibly from the base. They sprint through the corridor, "
                   "vaulting the fallen pillar with real athletic effort, then grab a "
                   "hanging vine with BOTH hands and swing across a deep chasm, landing on "
                   "two feet in a natural, balanced way. They rise before a stone altar, "
                   "lift a small golden idol into a beam of sunlight, grin at the camera and "
                   "say in clear English: \"Told you the map was real.\" — holding the idol "
                   "up as the light flares." + _SUFFIX),
    },
    {
        "key": "mountain", "no": "03", "emoji": "🏔️",
        "title_th": "TO THE TOP, TOGETHER", "title_en": "MOUNTAIN PEAK",
        "genre_th": "ADVENTURE", "genre_en": "ADVENTURE · SUMMIT",
        "logline_en": "Two climbers. One summit. All the way together.",
        "synopsis": ("Soft morning light on a snow-covered range — two climbing partners "
                     "help each other up the final steps and reach the peak side by side. "
                     "A warm, triumphant summit story."),
        "tags": "SNOW · CLIMBING · SUMMIT",
        "c1": "#0E1E30", "c2": "#3A6A9A", "c3": "#EAF6FF",
        "prompt": ("A cinematic mountaineering movie scene: soft morning sunlight across a "
                   "beautiful snow-covered mountain range, photorealistic alpine light. "
                   "EXACTLY ONE person appears: the person in Image 1 in a professional "
                   "plain mountaineering outfit — climbing harness, gloves, light backpack "
                   "— walking a gentle snowy trail with real weighted steps, breath visible "
                   "in the cold air, face clearly visible toward the camera. They pause at "
                   "a ridge, take in the sweeping view of peaks and clouds, smile and say "
                   "in clear English: \"What a perfect day to climb.\" Then they push up "
                   "the final snowy rise with real effort and step onto the peak, raise "
                   "both arms wide against the sunlit clouds and say joyfully: \"Made it "
                   "— all the way.\" — holding the happy pose as the wind moves the "
                   "snow." + _SUFFIX),
    },
    {
        "key": "hoian", "no": "04", "emoji": "🏮",
        "title_th": "THE NIGHT THE RIVER GLOWS", "title_en": "LANTERN NIGHTS",
        "genre_th": "FESTIVAL", "genre_en": "FESTIVAL · HỘI AN",
        "logline_en": "Lanterns on the water. Fireworks in the sky.",
        "synopsis": ("A warm evening at a Hội An riverside lantern festival — glowing "
                     "lanterns, street food, and a golden firework finale over the water. "
                     "The night every traveler dreams about."),
        "tags": "HỘI AN · LANTERNS · FIREWORKS",
        "c1": "#1A0806", "c2": "#B0501E", "c3": "#F6C55C",
        "prompt": ("A cinematic travel movie scene: warm evening light over the lively "
                   "riverside of Hội An ancient town, Vietnam — yellow-walled heritage "
                   "houses, hundreds of plain silk lanterns glowing warm and steady (all "
                   "lanterns completely blank, no writing), food stalls, festival visitors "
                   "strolling in the background who never approach. EXCEPTION to the "
                   "effects rule: this scene DOES include real festival FIREWORKS — real "
                   "pyrotechnics that launch from across the river, burst high in the "
                   "night sky and fade naturally, reflected in the water; they behave with "
                   "real physics and are the only exception — lanterns and lamps still "
                   "burn small and steady. The person in Image 1, in comfortable plain "
                   "travel clothes, strolls through the festival with relaxed curiosity, "
                   "buys a small local snack at a stall (handing the vendor money, taking "
                   "the snack), walks to a peaceful spot at the river's edge and says in "
                   "clear English: \"This place feels so alive.\" A golden firework "
                   "rises and bursts over the river; they watch it bloom, smile, turn "
                   "slightly to the camera with the glowing river behind them and say: "
                   "\"What a beautiful night.\"" + _SUFFIX),
    },
]

FILM_BY_KEY = {f["key"]: f for f in FILMS}


# ---- 30-second two-character version ----
# Visitor = Image 1 (real face). Companion = a VIETNAMESE AI co-star of the
# chosen gender. Two 15s sequences stitched to 30s; seq B extends seq A.
_DUO_A = (
    " Cinematic, filmic lighting with rich depth of field. Both people are clearly visible "
    "and share the frame. The person from Image 1 keeps the exact face, hair and look of "
    "Image 1 the whole time — the face must stay EXACTLY identical to Image 1 in every "
    "single frame, with ZERO morphing or drifting even during fast motion, and kept "
    "clearly visible to the camera as much as possible." + _RULES + " Natural motion "
    "continues flowing through the VERY LAST frame of the sequence — the characters "
    "keep breathing, shifting and moving naturally to the end; NEVER freeze, hold a "
    "static pose, or stand motionless at the end of the sequence — simply avoid ending "
    "in the middle of a fast action: end on calm, continuous, natural movement. "
    "15 seconds."
)
_DUO_B = (
    " Continue the SAME film from Video 1 — the exact same two people (the face of the "
    "person from Image 1 stays EXACTLY identical to Image 1 in every frame, zero morphing), "
    "same hair, same outfits, same world and lighting. OPEN this sequence as a deliberate "
    "fresh camera angle on the same scene — like the next intentional shot cut by a film "
    "editor — so the transition from the previous sequence feels like professional movie "
    "editing, not a broken join."
    + _RULES + " Bring the story to a satisfying, natural close — a clear, feel-good final "
    "beat, never an abrupt mid-action cut. 15 seconds."
)

# Each theme is a 30s two-character VIETNAMESE MOVIE SCENE with a real arc:
# seq A sets up the stakes, seq B pays it off. Dialogue is genuine back-and-forth.
DUO = {
    "ballroom": (
        "A romantic movie scene at a glamorous evening party in a grand hotel ballroom: "
        "warm chandelier light from visible chandeliers, candlelit tables, elegantly "
        "dressed Vietnamese guests chatting softly at the edges of a polished dance floor "
        "— the guests stay at the edges and never approach the couple. Gentle original "
        "orchestral music plays. The person in Image 1 and a young {costar} — one in a "
        "graceful plain evening gown, the other in a tailored suit with vest — meet at "
        "the center of the floor, both faces framed frontally or three-quarter toward "
        "the camera. The {costar} offers a hand, looking directly and steadily into the "
        "other's eyes, and says in clear English: \"May I have this dance?\" The person "
        "in Image 1 takes the hand with a warm smile, meeting their gaze precisely: \"I "
        "was hoping you'd ask.\" Then they dance a REAL, beautiful, flowing waltz like "
        "trained ballroom dancers: in proper closed hold — one hand clasped high, the "
        "other on shoulder and waist — they take LONG, sweeping gliding steps that "
        "TRAVEL across the floor, rotating together as a couple while orbiting in wide "
        "circles around the ballroom, gowns and jackets flowing with the motion, "
        "covering real distance with every phrase of the music — never dancing in one "
        "spot, never small shuffling steps, continuously moving and turning with grace "
        "and momentum." + _DUO_A,
        "Continue directly from Video 1. The waltz builds into its most beautiful "
        "stretch: the couple keeps TRAVELING in long sweeping steps around the floor, "
        "rotating smoothly; the person from Image 1 leads the {costar} into a graceful "
        "underarm SPIN — the {costar} turning fully under their joined hands — then "
        "back into closed hold without breaking flow; two more long gliding phrases "
        "circling the floor; and on the final swell the couple finishes with a classic "
        "romantic DIP — the {costar} leaning far back over the partner's supporting "
        "arm, back arched, one arm extended elegantly, held for a breath — then drawn "
        "smoothly back up face to face. The {costar} says softly in clear English: \"I "
        "could dance with you all night.\" The person from Image 1 smiles warmly: "
        "\"Then don't stop.\" The guests at the edges applaud softly — a sweeping, "
        "romantic close." + _DUO_B,
    ),
    "adventure": (
        "A cinematic adventure-movie scene: ancient jungle temple ruins, sunlight "
        "shafting through the canopy over mossy stone. EXACTLY TWO people appear in this "
        "entire video — the person in Image 1 and a young {costar}; no third person, "
        "stranger, or extra figure ever appears anywhere. Every stone or wall that moves "
        "or falls does so only because a real physical force acts on it; NOTHING "
        "collapses or rises by itself. Temple walls and stonework bear only plain "
        "weathered shapes — absolutely no letters, script, runes or inscriptions "
        "anywhere. The two explorers, in rugged plain gear, examine the altar. The "
        "person in Image 1 lifts the golden idol off its "
        "pedestal — the pedestal sinks under the released weight, triggering the ancient "
        "mechanism: stone supports visibly slide away and columns topple from their "
        "bases, one knocking into the next. The {costar} shouts in clear English: \"You "
        "had to pick it up — RUN!\" The person in Image 1 clutches the idol: \"Go, go, "
        "GO!\" They sprint through the corridor together with real athletic effort, "
        "vaulting one fallen pillar cleanly and landing on their feet — the person in "
        "Image 1 clearly HOLDING the golden idol in one hand the entire time, still "
        "visibly in hand in the final frame of this sequence." + _DUO_A,
        "Continue directly from Video 1 — still EXACTLY TWO people, the same two "
        "explorers, nobody else ever appears. From the VERY FIRST FRAME the person "
        "from Image 1 is still clearly HOLDING the golden idol in one hand — the idol "
        "never disappears, is never dropped or thrown, and stays visibly in their hand "
        "continuously until the exact moment they tuck it away. They reach a deep "
        "chasm and stop; ON CAMERA, the person from Image 1 tucks the golden idol "
        "securely into their shoulder satchel — a clear, visible motion, idol in hand "
        "until it enters the bag — and only THEN, with BOTH hands now free, grips a "
        "hanging vine firmly with both "
        "hands; the {costar} takes one look down the chasm, panics comically, and "
        "instead of taking the vine wraps BOTH arms tightly around the swinger's waist "
        "in a bear hug, cheek pressed to their back, eyes squeezed shut — and the two "
        "swing across as one, the hugger's legs kicking in the air, funny but "
        "physically real: the vine and the swinger's grip visibly carry both bodies' "
        "weight. They land naturally on their feet on the far side, knees bending to "
        "absorb the landing, the {costar} still clinging on a second too long before "
        "letting go sheepishly. Behind them the last toppling columns crash down and seal the "
        "corridor in dust. Safe in a shaft of sunlight, they catch their breath and "
        "laugh. The {costar} says in clear English: \"Next time, YOU read the "
        "warnings.\" The person from Image 1 pulls the idol from the satchel and holds "
        "it up: \"Next time... we bring a bigger bag.\" They grin and walk out into the "
        "light — a classic adventure close." + _DUO_B,
    ),
    "mountain": (
        "A cinematic mountaineering movie scene: soft morning sunlight across a "
        "beautiful snow-covered mountain range, photorealistic alpine light. EXACTLY "
        "TWO people appear: the person in Image 1 and a young {costar}, climbing "
        "partners, both in professional plain mountaineering outfits — climbing "
        "harnesses, gloves, light backpacks — both faces clearly visible toward the "
        "camera throughout. Sequence, in order: (1) the two stand together on a gentle "
        "snowy mountain trail; the {costar} looks toward the summit and smiles: \"What "
        "a perfect day to climb.\"; (2) medium close-up of the person in Image 1 "
        "smiling warmly with an encouraging nod: \"And even better with good "
        "company.\"; (3) front-facing tracking shot as both climbers walk side by side "
        "up the snowy trail with real weighted steps, talking and laughing, helping "
        "each other over small rocks, faces relaxed and visible; the {costar} grins: "
        "\"Race you to that ridge?\" — the person in Image 1 answers: \"Only if we "
        "finish together.\"; (4) they reach the ridge and stop to admire the sweeping "
        "view; the {costar} offers a small snack from their backpack and the two share "
        "it, smiling, the summit rising beautifully behind them." + _DUO_A,
        "Continue directly from Video 1 — same two climbers, same mountain, higher up "
        "near the summit. Sequence, in order: (1) they reach a small snowy step that "
        "is slightly difficult to cross; the {costar} looks at it, then turns to the "
        "person from Image 1 with a playful expression: \"A little help?\"; (2) "
        "close-up of the person from Image 1 smiling, reaching out a hand and helping "
        "the {costar} step safely onto the higher ground — real supporting grip and "
        "weight: \"That's what climbing partners are for.\"; (3) the {costar} "
        "reaches back and helps the person from Image 1 climb up too; they laugh, "
        "clasp hands, and walk on toward the summit; the {costar}: \"Now we're "
        "even.\" — the person from Image 1: \"Not yet. You owe me a summit "
        "photo.\"; (4) both step onto the mountain peak side by side; warm sunlight "
        "breaks through the clouds as they raise their arms, laugh, and take a joyful "
        "selfie together on a plain phone, both faces clearly visible and full of "
        "happiness; the {costar}: \"We made it!\" — the person from Image 1: "
        "\"Together, all the way.\" — a triumphant, warm close." + _DUO_B,
    ),
    "hoian": (
        "A cinematic travel movie scene: warm evening light over the lively riverside "
        "of Hội An ancient town, Vietnam — yellow-walled heritage houses, hundreds of "
        "plain silk lanterns glowing warm and steady (all lanterns completely blank, "
        "no writing anywhere), food stalls, festival visitors strolling in the "
        "background who never approach the leads. EXACTLY TWO featured people: the "
        "person in Image 1 and a young {costar}, two friends in comfortable plain "
        "travel clothes. Sequence, in order: (1) the two stroll together through the "
        "lantern-lit festival street, relaxed and curious, faces clearly visible; "
        "(2) they stop at a street-food stall — the person in Image 1 hands the "
        "vendor money and receives two small local snacks, passing one to the "
        "{costar}; (3) walking on toward the river, the {costar} takes a bite and "
        "smiles: \"This place feels so alive.\" — the person in Image 1: \"Wait "
        "until you see the river.\"; (4) they find a peaceful viewing spot at the "
        "river's edge, lantern light dancing on the water, just as a first firework "
        "rises into the night sky. EXCEPTION to the effects rule: this scene DOES "
        "include real festival FIREWORKS — real pyrotechnics that launch, burst and "
        "fade with real physics, reflected in the river; lanterns and lamps still "
        "burn small and steady." + _DUO_A,
        "Continue directly from Video 1 — same two friends at the Hội An riverside. "
        "The fireworks EXCEPTION still applies: real pyrotechnics only, everything "
        "else steady. Sequence, in order: (1) a large golden firework blooms above "
        "the river — both watch with happy, impressed expressions, the light playing "
        "on their faces; (2) more fireworks fill the sky in red, blue, gold and "
        "purple as the two watch calmly side by side; (3) the person from Image 1 "
        "takes a few photos on a plain phone, then lowers it to simply enjoy the "
        "moment; the {costar} says softly: \"Some things you don't watch through a "
        "screen.\" — the person from Image 1 smiles: \"Agreed.\"; (4) a final "
        "spread of golden fireworks crosses the sky; the two turn slightly toward "
        "the camera with the glowing river and fireworks behind them, and the person "
        "from Image 1 says warmly in clear English: \"What a beautiful night we got "
        "to experience.\" — a glowing, peaceful close." + _DUO_B,
    ),
}


def duo_prompts(film_key: str, costar_gender: str):
    """Return (sequence_a, sequence_b) for the 30s version. The AI companion is
    always Vietnamese; costar_gender is 'woman' or 'man'. A theme may provide a
    dict keyed by costar gender when the storyline depends on who the guest is
    (e.g. drama: the man is always the cheater, never the one doing đánh ghen)."""
    pair = DUO.get(film_key)
    if not pair:
        return None
    if isinstance(pair, dict):
        pair = pair.get(costar_gender)
        if not pair:
            return None
    costar = f"Vietnamese {costar_gender}"
    return tuple(p.replace("{costar}", costar) for p in pair)
