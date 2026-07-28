"""The Premiere Pictures film catalog — 7 Vietnamese movie-scene themes.

Each guest stars INSIDE a real movie scene set in Vietnam — Saigon action,
jungle adventure, vintage-Saigon romance, street dance, Saigon noir, Vietnamese
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
    "mouth. Do NOT render any text anywhere in the video — no captions, subtitles, labels, "
    "watermarks or floating graphics; all clothing, props, sets and backdrops are completely "
    "plain and unbranded with no writing, logos or trademarks. If there is any background "
    "music it must be completely ORIGINAL instrumental audio generated brand-new for this "
    "video — no lyrics, never any existing, famous, or copyrighted song or melody. Everything "
    "obeys real-world physics — bodies, hands and objects move exactly as they do in real "
    "life, and every physical performance (fighting, dancing, running, jumping) looks like "
    "real trained performers: correct balance, weight, momentum and follow-through, with no "
    "impossible or rubbery movement. Present the ENTIRE clip as a single continuous "
    "full-frame shot from one camera: no split-screen, no grids, tiles, collage or "
    "picture-in-picture. Natural realistic human movement with visible weight and effort, "
    "smooth animation, no flickering."
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
        "key": "action", "no": "01", "emoji": "💥",
        "title_th": "SAIGON STREETS", "title_en": "ACTION BLOCKBUSTER",
        "genre_th": "ACTION", "genre_en": "ACTION · SAIGON",
        "logline_en": "Saigon nights. No brakes. No fear.",
        "synopsis": ("A Vietnamese gangster-action scene — a motorbike pursuit through neon "
                     "Saigon streets, a skidding stop in a narrow alley, and one clean move "
                     "that ends the fight. Pure Vietnamese action cinema."),
        "tags": "MOTORBIKE · SAIGON · SHOWDOWN",
        "c1": "#0A0E2A", "c2": "#C8321E", "c3": "#F6C55C",
        "prompt": ("A cinematic Vietnamese gangster-action movie scene: the neon-lit streets "
                   "of Saigon (Ho Chi Minh City) at night — narrow streets with shophouses, "
                   "hanging cables, street-food steam, parked motorbikes everywhere. The "
                   "person in Image 1, in a sleek plain jacket, rides a motorbike smoothly "
                   "through the busy streets, weaving past traffic with realistic riding "
                   "physics, then skids to a controlled stop in a narrow alley where a masked "
                   "rival gang member blocks the way. In one SHORT, crisp exchange — no more "
                   "than three seconds — they dismount, sidestep the rival's lunge and answer "
                   "with a single clean sweep that sends him stumbling back into the shadows. "
                   "The hero straightens up, face clearly lit by the neon signs, and says in "
                   "clear English with a wry smile: \"These streets are mine.\" — then walks "
                   "back to the bike as the alley glows." + _SUFFIX),
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
                   "sunlight through the canopy, mist over mossy stone. Every stone or wall "
                   "that moves or falls does so only because a real physical force acts on it "
                   "— a stepped-on trigger plate, an impact, or its support visibly giving way "
                   "first; NOTHING collapses or rises by itself without a clear physical "
                   "cause. The person in Image 1, in rugged plain explorer gear, steps on an "
                   "ancient trigger plate — it sinks with a clunk, and the impact makes a "
                   "nearby column's support give way so it topples visibly from the base. "
                   "They sprint through the corridor, vaulting the fallen pillar with real "
                   "athletic effort, then grab a hanging vine and swing across a deep chasm, "
                   "landing in a controlled roll. They rise before a stone altar, lift a "
                   "small golden idol into a beam of sunlight, grin at the camera and say in "
                   "clear English: \"Told you the map was real.\" — holding the idol up as "
                   "the light flares." + _SUFFIX),
    },
    {
        "key": "goldenage", "no": "03", "emoji": "🎞️",
        "title_th": "SAIGON SERENADE", "title_en": "GOLDEN AGE CINEMA",
        "genre_th": "ROMANCE", "genre_en": "ROMANCE · SAIGON XƯA",
        "logline_en": "Old Saigon. One dance. Forever.",
        "synopsis": ("A timeless vintage-Saigon romance scene — a 1960s Saigon ballroom with "
                     "lanterns and ceiling fans, elegant áo dài, and a sweeping waltz that "
                     "old Vietnamese cinema never forgot."),
        "tags": "SAIGON XƯA · ÁO DÀI · WALTZ",
        "c1": "#1A140A", "c2": "#8A6A2A", "c3": "#F6E08A",
        "prompt": ("A vintage Vietnamese romance movie scene set in 1960s old Saigon: an "
                   "elegant colonial-era ballroom with warm lantern light, slow ceiling fans, "
                   "wooden shutters and tropical plants, filled with elegantly dressed "
                   "Vietnamese guests — women in graceful plain áo dài, men in tailored "
                   "suits. The person in Image 1, dressed in timeless Vietnamese evening "
                   "elegance, glides across the floor in a graceful waltz — smooth turns, "
                   "poised arms, real dancer's balance and footwork — as the guests watch "
                   "admiringly. They finish with a slow, elegant spin into a poised final "
                   "pose, look warmly to the camera and say in clear English: \"Some nights "
                   "belong to old Saigon.\" — as the lanterns glow." + _SUFFIX),
    },
    {
        "key": "dance", "no": "04", "emoji": "🕺",
        "title_th": "OWN THE FLOOR", "title_en": "DANCE FEVER",
        "genre_th": "DANCE", "genre_en": "DANCE · HIP-HOP",
        "logline_en": "The floor clears. The beat drops. You own it.",
        "synopsis": ("A high-energy Saigon street-dance scene — non-stop hip-hop and breaking: "
                     "sharp footwork, spins, a windmill into a headspin-style power move, all "
                     "flowing without a pause."),
        "tags": "HIP-HOP · BREAKING · SAIGON",
        "c1": "#14082A", "c2": "#7A2AB0", "c3": "#57E0F0",
        "prompt": ("A cinematic street-dance movie scene: a Saigon night plaza with warm "
                   "practical lights and a small circle of young Vietnamese dancers watching "
                   "with smiles, nodding along. A smooth, upbeat ORIGINAL instrumental groove "
                   "plays and the person in Image 1, in stylish plain streetwear, dances "
                   "CONTINUOUSLY from the first beat to the last — never stopping, never "
                   "freezing in place, no long held poses; the body keeps moving and grooving "
                   "with the music at all times. The routine is real hip-hop and breaking: "
                   "sharp footwork, a smooth spin, a toprock into a windmill and a "
                   "controlled headspin-style power move, flowing move into move with real "
                   "b-boy momentum and balance. Any accent hit lands ON the beat and lasts "
                   "less than half a second before flowing on. They finish the last move, "
                   "flash a confident grin to camera and say in clear English: \"That's how "
                   "it's done.\" — as the circle gives warm, gentle applause." + _SUFFIX),
    },
    {
        "key": "noir", "no": "05", "emoji": "🕵️",
        "title_th": "SAIGON MIDNIGHT", "title_en": "FILM NOIR",
        "genre_th": "MYSTERY", "genre_en": "MYSTERY · SAIGON NOIR",
        "logline_en": "One clue. One chase. Case closed.",
        "synopsis": ("A moody old-Saigon noir scene in rich cinematic color — rain-slicked "
                     "shophouse alleys, lantern light and phở-cart steam, a fleeing shadow, "
                     "and the clue that closes the case with timeless style."),
        "tags": "DETECTIVE · OLD SAIGON · RAIN",
        "c1": "#0A0A0C", "c2": "#2E2E36", "c3": "#D8D8E0",
        "prompt": ("A moody Vietnamese film-noir movie scene set in old Saigon at night, in "
                   "rich, realistic cinematic color — deep blue night tones with warm amber "
                   "lantern light, natural skin tones, wet streets reflecting the glow (NOT "
                   "black-and-white, no desaturated or artificial filter look): a rain-"
                   "slicked alley of old Vietnamese shophouses, paper lanterns swaying, steam "
                   "rising from a late-night phở cart, vintage motorbikes and a cyclo parked "
                   "in the shadows. The person in Image 1, a noir detective in a plain trench "
                   "coat and fedora, spots a shadowy figure dart from a shophouse doorway — "
                   "and gives chase: a quick, realistic pursuit through the rain, splashing "
                   "past the phở cart, rounding a corner with natural momentum. The figure "
                   "vanishes, but a small dropped notebook lies in the lantern light. The "
                   "detective picks it up, reads it with a slow knowing smile, tips their hat "
                   "to the camera and says in clear English: \"Case closed.\" — then strolls "
                   "into the mist." + _SUFFIX),
    },
    {
        "key": "horror", "no": "06", "emoji": "👻",
        "title_th": "DON'T LOOK BACK", "title_en": "VIETNAMESE HORROR",
        "genre_th": "HORROR", "genre_en": "HORROR · THRILLER",
        "logline_en": "The old house remembers you.",
        "synopsis": ("A Vietnamese horror-movie scene — an old wooden house at midnight, a "
                     "flickering oil lamp, and a pale figure in white that shouldn't be "
                     "there. Classic Vietnamese ghost-film chills with a fun scare."),
        "tags": "GHOST · OLD HOUSE · MIDNIGHT",
        "c1": "#04140E", "c2": "#0E3A2A", "c3": "#B8E8D0",
        "prompt": ("A Vietnamese horror-movie scene: inside an old traditional wooden "
                   "Vietnamese house at midnight — dark carved-wood furniture, a flickering "
                   "oil lamp, moonlight through slatted shutters, mist drifting along the "
                   "floor. The person in Image 1 walks slowly through the creaking house "
                   "holding the oil lamp, its light trembling. A draft they walk past makes "
                   "a wooden door swing slowly shut with a creak. They freeze, whisper in "
                   "clear English: \"...Hello?\" In the dusty mirror behind them, a pale "
                   "figure in white with long black hair appears for a single heartbeat — "
                   "then is gone when they spin around. Eyes wide, they back toward the "
                   "door, look right into the camera and whisper: \"Time to go.\" — then "
                   "hurry out as the lamp flickers, a fun cinematic chill." + _SUFFIX),
    },
    {
        "key": "drama", "no": "07", "emoji": "💔",
        "title_th": "NOBODY CROSSES ME", "title_en": "DRAMA ROYALE",
        "genre_th": "DRAMA", "genre_en": "DRAMA · MELODRAMA",
        "logline_en": "The tea is hot. The drama is hotter.",
        "synopsis": ("The Vietnamese melodrama everyone secretly loves — a glamorous café "
                     "confrontation with the 'tiểu tam', a dramatic glass of water, a "
                     "hair-flip exit. Pure drama-queen cinema."),
        "tags": "MELODRAMA · CONFRONTATION · ICONIC",
        "c1": "#2A0614", "c2": "#B01E4A", "c3": "#F6B7D8",
        "prompt": ("A Vietnamese melodrama movie scene, glossy TV-drama style: an elegant "
                   "modern Saigon café with marble tables and soft afternoon light. The "
                   "person in Image 1, impeccably dressed, strides in with theatrical "
                   "confidence and stops at a table where a glamorous Vietnamese woman — the "
                   "story's scheming 'other woman' — sits smugly with an iced tea. The "
                   "person in Image 1 delivers the line in clear English with icy calm: \"I "
                   "believe you have something that belongs to me.\" The woman smirks — and "
                   "the person in Image 1 lifts the glass of water from the table and, in "
                   "classic melodrama fashion, splashes it toward her as she gasps in "
                   "theatrical shock (staged drama-style, water only). The person in Image 1 "
                   "sets the glass down elegantly, flips their hair, looks to camera and "
                   "says: \"Nobody crosses me.\" — then struts out in slow motion, "
                   "cinematic and iconic." + _SUFFIX),
    },
]

FILM_BY_KEY = {f["key"]: f for f in FILMS}


# ---- 30-second two-character version ----
# Visitor = Image 1 (real face). Companion = a VIETNAMESE AI co-star of the
# chosen gender ({costar} = "Vietnamese woman"/"Vietnamese man") described in
# the prompt (the endpoint allows only one real face). Two 15s sequences
# stitched to 30s; seq B extends seq A via reference_video.
_DUO_A = (
    " Cinematic, filmic lighting with rich depth of field. Both people are clearly visible "
    "and share the frame. The person from Image 1 keeps the exact face, hair and look of "
    "Image 1 the whole time — the face must stay EXACTLY identical to Image 1 in every "
    "single frame, with ZERO morphing or drifting even during fast motion, and kept "
    "clearly visible to the camera as much as possible." + _RULES + " End the sequence "
    "on a brief, stable, holdable moment — both people settling into a natural still "
    "pose for the final second — never cut off mid-action. 15 seconds."
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
    "action": (
        "A cinematic Vietnamese gangster-action movie scene: the neon-lit streets of Saigon "
        "(Ho Chi Minh City) at night — narrow shophouse streets, hanging cables, street-food "
        "steam, motorbikes everywhere. The person in Image 1 and a young {costar}, PARTNERS "
        "and allies on the same side, ride two motorbikes side by side through the streets "
        "with realistic riding physics, masked rival riders tailing them. They skid to a "
        "controlled stop in a lantern-lit alley and dismount as two masked rivals close in. "
        "The {costar} says in clear English: \"They followed us.\" The person in Image 1 "
        "answers calmly: \"Then let's finish this.\" IMPORTANT: the two partners are on the "
        "SAME side and NEVER fight, strike, or touch each other — they only ever fight the "
        "masked rivals. In one SHORT crisp exchange the two partners, fighting side by side "
        "AGAINST the masked rivals, each sidestep a lunge and answer with one clean counter "
        "each, sending the rivals stumbling back. The partners settle side by side, faces "
        "to camera." + _DUO_A,
        "Continue directly from Video 1. The masked rivals scramble up and flee down the "
        "alley on foot — the fight is over. The two partners (still allies, never fighting "
        "each other) relax, faces clearly lit by neon and lanterns. The {costar} laughs in "
        "clear English: \"Saigon nights are never boring.\" The person from Image 1 grins: "
        "\"Not with you around.\" They bump fists, get back on their motorbikes, and ride "
        "off side by side into the glowing street — a cool, confident close." + _DUO_B,
    ),
    "adventure": (
        "A cinematic adventure-movie scene: ancient jungle temple ruins, sunlight shafting "
        "through the canopy, mist over mossy stone. Every stone or wall that moves or falls "
        "does so only because a real physical force acts on it — a stepped-on trigger "
        "plate, an impact, or its support visibly giving way first; NOTHING collapses or "
        "rises by itself without a clear physical cause. The person in Image 1 and a "
        "young {costar}, both explorers in rugged plain gear, study a stone map on an altar. "
        "The person in Image 1 lifts the golden idol off its pedestal — and the pedestal "
        "sinks under the released weight, triggering the ancient mechanism: stone supports "
        "visibly slide away and columns begin toppling from their bases, one knocking into "
        "the next. The {costar} shouts in clear English: \"You had to pick it up — RUN!\" "
        "The person in Image 1 clutches the idol: \"Go, go, GO!\" They sprint through the "
        "corridor together, vaulting a pillar that a falling neighbor has knocked down — "
        "real athletic effort and momentum." + _DUO_A,
        "Continue directly from Video 1. The two explorers reach a deep chasm; the person "
        "from Image 1 grabs a hanging vine, the {costar} holds on, and they swing across "
        "together, landing in a controlled roll as behind them the last toppling columns — "
        "each knocked over by the one before it — crash down and seal the corridor in a "
        "cloud of dust. Safe in a shaft of sunlight, they catch their breath and start "
        "laughing. The {costar} says in clear English: \"Next time, YOU read the warnings.\" "
        "The person from Image 1 holds up the gleaming golden idol: \"Next time... we bring "
        "a bigger bag.\" They grin and walk out into the light — a classic adventure "
        "close." + _DUO_B,
    ),
    "goldenage": (
        "A vintage Vietnamese romance movie scene set in 1960s old Saigon: an elegant "
        "colonial-era ballroom with warm lantern light, slow ceiling fans, wooden shutters "
        "and tropical plants, filled with elegantly dressed Vietnamese guests — women in "
        "graceful plain áo dài, men in tailored suits. The person in Image 1 and a young "
        "{costar}, both dressed in timeless Vietnamese evening elegance, meet at the center "
        "of the floor. The {costar} offers a hand and says in clear English: \"They're all "
        "watching, you know.\" The person in Image 1 takes it with a warm smile: \"Then "
        "let's give them something to remember.\" Gentle original orchestral music rises "
        "and they sweep into a graceful, flowing waltz — real dancer's frame, balance and "
        "footwork, turning elegantly across the floor." + _DUO_A,
        "Continue directly from Video 1. The waltz builds — sweeping turns across the "
        "lantern-lit floor, a graceful underarm spin, the Vietnamese guests watching "
        "enchanted — every step with real dancer's poise and momentum. The music swells and "
        "they finish with a gentle, elegant dip and a poised recovery, holding the final "
        "pose as the guests applaud warmly. The {costar} says softly in clear English: "
        "\"Told you they'd remember.\" The person from Image 1 smiles: \"So will I.\" They "
        "share a warm look under the lanterns — a timeless, romantic close." + _DUO_B,
    ),
    "dance": (
        "A cinematic street-dance movie scene: a Saigon night plaza with warm practical "
        "lights and a small circle of young Vietnamese dancers watching with smiles, "
        "nodding along. The ONLY audio besides the spoken lines is a simple ORIGINAL percussion beat — drums only, absolutely NO rap, NO vocals, NO singing, NO vocal samples of any kind. The person in "
        "Image 1 and a young {costar}, both in stylish plain streetwear, step into the "
        "circle. Both dance CONTINUOUSLY from the first beat to the last — never stopping, "
        "never freezing in place, no long held poses; bodies always moving and grooving "
        "with the music. The {costar} opens with real hip-hop: sharp toprock footwork into "
        "a smooth spin, calling in clear English mid-groove: \"Show me what you've got!\" "
        "The person in Image 1 answers while already moving: \"Try to keep up.\" — and "
        "flows into a breaking combo: footwork, a windmill, a controlled headspin-style "
        "power move, every transition flowing with real b-boy momentum." + _DUO_A,
        "Continue directly from Video 1. The two dance TOGETHER non-stop — synchronized "
        "hip-hop grooves, trading breaking moves, mirroring each other perfectly on the "
        "beat, never pausing or freezing; any accent hit lands ON the beat and flows "
        "onward in under half a second. The circle of Vietnamese dancers sways along, "
        "delighted. On the final beat they land one clean shared ending move, then break "
        "into laughter, still bouncing with the groove. The {costar} says in clear "
        "English: \"Okay — we OWN this floor.\" The person from Image 1 high-fives them: "
        "\"Every night.\" The circle gives warm, gentle applause — an electric, joyful "
        "close." + _DUO_B,
    ),
    "noir": (
        "A moody Vietnamese film-noir movie scene set in old Saigon at night, in rich, "
        "realistic cinematic color — deep blue night tones with warm amber lantern light, "
        "natural skin tones, wet streets reflecting the glow (NOT black-and-white, no "
        "desaturated or artificial filter look): a rain-slicked alley of old Vietnamese "
        "shophouses, paper lanterns swaying, steam rising from a late-night phở cart, "
        "vintage motorbikes and a cyclo in the shadows. The person in Image 1 and a young "
        "{costar}, two noir detectives in plain trench coats and fedoras, study a small "
        "notebook under a lantern. Suddenly a shadowy figure darts from a shophouse "
        "doorway. The {costar} snaps in clear English: \"There — that's our lead!\" The "
        "person in Image 1 is already moving: \"Cut through the alley!\" The two give "
        "chase through the rain — a quick, realistic pursuit, splashing past the phở "
        "cart, coats flaring as they round the corner with natural momentum." + _DUO_A,
        "Continue directly from Video 1. The two detectives corner the empty alley — the "
        "figure is gone, but a small key glints on the wet stones under a swaying paper "
        "lantern. The person from Image 1 picks it up and holds it to the light with a "
        "slow, knowing smile. The {costar} laughs softly in clear English: \"The theater "
        "locker. It was there all along.\" The person from Image 1 tips their hat: \"Case "
        "closed, partner.\" They shake hands in the lantern glow and stroll off side by "
        "side past the steaming phở cart into the mist — a stylish, timeless close." + _DUO_B,
    ),
    "horror": (
        "A Vietnamese horror-movie scene: inside an old traditional wooden Vietnamese "
        "house at midnight — dark carved-wood furniture, a flickering oil lamp, moonlight "
        "through slatted shutters, mist along the floor. The person in Image 1 and a young "
        "{costar} explore the creaking house together, the {costar} holding the trembling "
        "oil lamp. A draft they walk past makes a wooden door swing slowly shut with a "
        "creak. They freeze back to back. The {costar} whispers in clear English: \"Tell "
        "me that was the wind.\" The person in Image 1 whispers back: \"...That wasn't "
        "the wind.\" In the dusty mirror behind them, a pale figure in white with long "
        "black hair appears for a single heartbeat — then is gone when they both spin "
        "around, eyes wide." + _DUO_A,
        "Continue directly from Video 1. The oil lamp flickers hard; down the corridor, "
        "the pale figure in white appears once more at the far end — and the two grab "
        "each other and RUN, a realistic panicked sprint through the creaking house and "
        "out the front door into the moonlit courtyard, where they double over catching "
        "their breath. The {costar} gasps in clear English: \"We are NEVER coming back "
        "here.\" The person from Image 1, half-laughing half-terrified: \"Deal.\" They "
        "look at each other and burst into nervous laughter under the moonlight — a fun, "
        "spooky, shareable close." + _DUO_B,
    ),
    "drama": (
        "A Vietnamese melodrama movie scene, glossy TV-drama style: an elegant modern "
        "Saigon café with marble tables and soft afternoon light. The person in Image 1, "
        "impeccably dressed, strides in with theatrical confidence alongside a young "
        "{costar} — their fiercely loyal best friend, arms crossed, ready for drama. At a "
        "corner table sits a glamorous Vietnamese woman — the story's scheming 'other "
        "woman' — sipping iced tea smugly. The person in Image 1 stops at her table and "
        "delivers the line in clear English with icy calm: \"I believe you have something "
        "that belongs to me.\" The {costar} adds with a slow clap: \"Oh, this is going to "
        "be good.\" The woman smirks and rises." + _DUO_A,
        "Continue directly from Video 1. The person from Image 1 lifts the glass of water "
        "from the table and, in classic melodrama fashion, splashes it toward the scheming "
        "woman, who gasps in theatrical shock (staged drama-style, water only, nobody "
        "hurt). The café goes silent. The person from Image 1 sets the glass down "
        "elegantly and says in clear English: \"Nobody crosses me.\" The {costar} snaps a "
        "dramatic hair-flip of their own: \"And nobody crosses my best friend.\" The two "
        "link arms and strut out of the café in glorious slow motion, heads high, as the "
        "scheming woman fumes — an iconic, deliciously dramatic close." + _DUO_B,
    ),
}


def duo_prompts(film_key: str, costar_gender: str):
    """Return (sequence_a, sequence_b) for the 30s version. The AI companion is
    always Vietnamese; costar_gender is 'woman' or 'man'."""
    pair = DUO.get(film_key)
    if not pair:
        return None
    costar = f"Vietnamese {costar_gender}"
    return tuple(p.replace("{costar}", costar) for p in pair)
