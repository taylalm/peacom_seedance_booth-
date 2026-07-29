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
    "natural skin texture — never a CGI, dreamlike, hazy, or artificially glowing look. "
    "Do NOT render any text anywhere in the video — no captions, subtitles, labels, "
    "watermarks or floating graphics; all clothing, props, sets and backdrops are completely "
    "plain and unbranded with no writing, logos or trademarks. If there is any background "
    "music it must be completely ORIGINAL instrumental audio generated brand-new for this "
    "video — no lyrics, no vocals, never any existing, famous, or copyrighted song or "
    "melody. Everything obeys real-world physics — bodies, hands and objects move exactly "
    "as they do in real life, with correct balance, weight, momentum and follow-through, "
    "no impossible or rubbery movement, no strange or unnatural motion of any kind. "
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
                   "tailored suit with vest), steps onto the floor and dances a slow, "
                   "romantic ballroom waltz — smooth unhurried turns, poised frame, real "
                   "dancer's balance and footwork — face kept toward the camera in frontal "
                   "or three-quarter view. They finish with one gentle final turn, look "
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
        "key": "goldenage", "no": "03", "emoji": "🎞️",
        "title_th": "RAIN ON THE VERANDA", "title_en": "GOLDEN AGE CINEMA",
        "genre_th": "PHIM XƯA", "genre_en": "ROMANCE · PHIM XƯA",
        "logline_en": "A love the old mansion never allowed.",
        "synopsis": ("The classic Vietnamese period melodrama — a 1950s Mekong Delta "
                     "landowner's mansion, oil lamps and pouring rain, and a forbidden "
                     "confession on the veranda straight out of the phim xưa everyone "
                     "grew up watching."),
        "tags": "PHIM XƯA · MIỀN TÂY · RAIN",
        "c1": "#1A140A", "c2": "#8A6A2A", "c3": "#F6E08A",
        "prompt": ("A classic Vietnamese period-drama movie scene ('phim xưa' style) set in "
                   "1950s Southern Vietnam, in the Mekong Delta countryside: the grand "
                   "traditional wooden mansion of a wealthy landowner family — dark "
                   "carved-wood pillars, an ancestral hall glowing with oil lamps, a wide "
                   "veranda facing a rain-soaked courtyard. Only the person in Image 1 and "
                   "two distant servants in plain áo bà ba (visible far in the background, "
                   "never approaching) appear. Heavy rain pours as gentle original string "
                   "music plays. The person in Image 1, dressed as the elegant young master "
                   "or young lady of the house in refined 1950s Vietnamese attire, stands "
                   "on the veranda framed FRONTALLY toward the camera, watching the rain, "
                   "then looks straight into the camera lens with steady, focused eyes and "
                   "says in clear English with deep dramatic feeling: \"This house has "
                   "rules... but the heart has none.\" Thunder rolls softly; they hold the "
                   "frontal gaze as the oil lamps glow — pure classic Vietnamese "
                   "melodrama." + _SUFFIX),
    },
    {
        "key": "noir", "no": "04", "emoji": "🕵️",
        "title_th": "SAIGON MIDNIGHT", "title_en": "FILM NOIR",
        "genre_th": "MYSTERY", "genre_en": "MYSTERY · SAIGON NOIR",
        "logline_en": "One clue. One chase. Case closed.",
        "synopsis": ("A grounded, realistic old-Saigon detective scene — a wet shophouse "
                     "street lit only by real shop lights and a phở cart's bulb, a fleeing "
                     "shadow, and the clue that closes the case."),
        "tags": "DETECTIVE · OLD SAIGON · RAIN",
        "c1": "#0A0A0C", "c2": "#2E2E36", "c3": "#D8D8E0",
        "prompt": ("A REALISTIC live-action detective movie scene in old Saigon at night — "
                   "shot like real 35mm film footage, absolutely photorealistic: a narrow "
                   "street of aged Vietnamese shophouses with peeling paint and real worn "
                   "textures, wet asphalt after rain reflecting ONLY the actual light "
                   "sources present — a single bare bulb over a phở cart, dim warm light "
                   "from two shophouse windows, one distant streetlamp. No fog, no haze, no "
                   "glow effects, no stylized color wash — just the natural darkness of a "
                   "real street at 1 a.m. with true photographic shadows and natural skin "
                   "tones. The person in Image 1, a detective in a plain worn trench coat, "
                   "stands near the phở cart checking a small notebook when a figure darts "
                   "from a doorway down the street. They give chase — a quick, realistic "
                   "sprint with real footsteps splashing shallow puddles — but the figure "
                   "is gone around the corner. On the wet ground under the streetlamp lies "
                   "a dropped key. The detective picks it up, turns it in the light with a "
                   "slow knowing smile, looks into the camera and says in clear English: "
                   "\"Case closed.\" — then walks off down the quiet street." + _SUFFIX),
    },
    {
        "key": "horror", "no": "05", "emoji": "👻",
        "title_th": "DON'T LOOK BACK", "title_en": "VIETNAMESE HORROR",
        "genre_th": "HORROR", "genre_en": "HORROR · THRILLER",
        "logline_en": "The old house remembers you.",
        "synopsis": ("A Vietnamese horror-movie scene — an old wooden house at midnight, a "
                     "flickering oil lamp, and a pale figure in white that shouldn't be "
                     "there. Classic Vietnamese ghost-film chills with a fun scare."),
        "tags": "GHOST · OLD HOUSE · MIDNIGHT",
        "c1": "#04140E", "c2": "#0E3A2A", "c3": "#B8E8D0",
        "prompt": ("A Vietnamese horror-movie scene, staged with precise control: inside an "
                   "old traditional wooden Vietnamese house at midnight — dark carved-wood "
                   "furniture, ONE oil lamp as the only light source, its warm flame "
                   "flickering naturally, moonlight through slatted shutters. EXACTLY TWO "
                   "figures exist in this video: the person in Image 1, and ONE pale "
                   "ghostly woman in a white dress with long black hair who appears ONLY "
                   "inside the mirror, ONLY once, for exactly one second — she never "
                   "appears outside the mirror, never moves toward anyone, and nothing else "
                   "in the house ever moves by itself except one door pushed by a visible "
                   "draft. Sequence, in order: (1) the person in Image 1 walks slowly "
                   "through the house holding the oil lamp, floorboards creaking under "
                   "their real steps; (2) a draft makes one wooden door swing slowly shut "
                   "with a creak — they freeze and whisper in clear English: \"...Hello?\"; "
                   "(3) in the dusty mirror behind them the pale woman appears for one "
                   "second, then is gone when they spin around; (4) eyes wide, they back "
                   "toward the exit, look into the camera and whisper: \"Time to go.\" — "
                   "then hurry out. Nothing else happens; no other scares, objects, or "
                   "figures." + _SUFFIX),
    },
    {
        "key": "drama", "no": "06", "emoji": "💔",
        "title_th": "NOBODY CROSSES ME", "title_en": "DRAMA ROYALE",
        "genre_th": "DRAMA", "genre_en": "DRAMA · MELODRAMA",
        "logline_en": "The tea is hot. The drama is hotter.",
        "synopsis": ("The Vietnamese melodrama everyone secretly loves — a glamorous café "
                     "confrontation with the 'tiểu tam', a dramatic glass of water, a "
                     "hair-flip exit. Pure drama-queen cinema."),
        "tags": "MELODRAMA · CONFRONTATION · ICONIC",
        "c1": "#2A0614", "c2": "#B01E4A", "c3": "#F6B7D8",
        "prompt": ("A Vietnamese melodrama movie scene, glossy TV-drama style, staged with "
                   "precise control: an elegant modern Saigon café in soft natural "
                   "afternoon window light. EXACTLY THREE people appear: the person in "
                   "Image 1, one glamorous seated Vietnamese woman (the story's scheming "
                   "'other woman'), and one waiter far in the background who never "
                   "approaches. Sequence, in order: (1) the person in Image 1, impeccably "
                   "dressed, walks calmly to the woman's marble table and stops, standing "
                   "naturally; (2) they say in clear English, calm and cold: \"I think you "
                   "know why I'm here.\" — the seated woman puts down her iced tea and "
                   "smirks; (3) the person in Image 1 picks up the glass of water from the "
                   "table with one hand and tips it forward so the water splashes onto the "
                   "woman — a real, physical splash, the glass stays firmly in hand, the "
                   "woman flinches back with a theatrical gasp, her hair and blouse wet "
                   "(staged drama, water only, nobody hurt); (4) the person in Image 1 "
                   "sets the glass back down gently, says in clear English: \"Stay away "
                   "from what's mine.\" — then turns and walks out at a natural pace with "
                   "one small hair-flip, the camera following their confident exit. "
                   "Nothing else happens; no other actions or gestures." + _SUFFIX),
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
        "was hoping you'd ask.\" They begin a slow, romantic ballroom dance — smooth "
        "unhurried turns, gentle frame, real dancer's balance — eyes naturally on each "
        "other." + _DUO_A,
        "Continue directly from Video 1. The slow dance sweeps gently on — unhurried "
        "romantic turns under the chandelier light, the two looking into each other's "
        "eyes with natural, precisely-aligned gazes, faces kept toward the camera in "
        "frontal or three-quarter view. The music swells softly and they finish with a "
        "gentle final turn and a tender pause, foreheads almost touching. The {costar} "
        "says softly in clear English: \"I could dance with you all night.\" The person "
        "from Image 1 smiles warmly: \"Then don't stop.\" They share one more slow turn "
        "as the guests at the edges applaud softly — a warm, romantic close." + _DUO_B,
    ),
    "adventure": (
        "A cinematic adventure-movie scene: ancient jungle temple ruins, sunlight "
        "shafting through the canopy over mossy stone. EXACTLY TWO people appear in this "
        "entire video — the person in Image 1 and a young {costar}; no third person, "
        "stranger, or extra figure ever appears anywhere. Every stone or wall that moves "
        "or falls does so only because a real physical force acts on it; NOTHING "
        "collapses or rises by itself. The two explorers, in rugged plain gear, study a "
        "stone map on an altar. The person in Image 1 lifts the golden idol off its "
        "pedestal — the pedestal sinks under the released weight, triggering the ancient "
        "mechanism: stone supports visibly slide away and columns topple from their "
        "bases, one knocking into the next. The {costar} shouts in clear English: \"You "
        "had to pick it up — RUN!\" The person in Image 1 clutches the idol: \"Go, go, "
        "GO!\" They sprint through the corridor together with real athletic effort, "
        "vaulting one fallen pillar cleanly and landing on their feet." + _DUO_A,
        "Continue directly from Video 1 — still EXACTLY TWO people, the same two "
        "explorers, nobody else ever appears. They reach a deep chasm; the person from "
        "Image 1 quickly tucks the golden idol securely into their shoulder satchel — "
        "BOTH hands now completely free — then grips a hanging vine firmly with both "
        "hands; the {costar} grips the same vine with both hands below them, and they "
        "swing across together with realistic weight and momentum, releasing the vine "
        "and landing naturally on their feet on the far side, knees bending to absorb "
        "the landing. Behind them the last toppling columns crash down and seal the "
        "corridor in dust. Safe in a shaft of sunlight, they catch their breath and "
        "laugh. The {costar} says in clear English: \"Next time, YOU read the "
        "warnings.\" The person from Image 1 pulls the idol from the satchel and holds "
        "it up: \"Next time... we bring a bigger bag.\" They grin and walk out into the "
        "light — a classic adventure close." + _DUO_B,
    ),
    "goldenage": (
        "A classic Vietnamese period-drama movie scene ('phim xưa' style) set in 1950s "
        "Southern Vietnam, in the Mekong Delta countryside: the grand traditional wooden "
        "mansion of a wealthy landowner family — dark carved-wood pillars, an ancestral "
        "hall glowing with oil lamps, a wide veranda facing a rain-soaked courtyard. "
        "EXACTLY TWO people appear in this video: the person in Image 1 and a young "
        "{costar}; nobody else ever appears. Heavy rain pours as gentle original string "
        "music plays. The person in Image 1, the elegant young master or young lady of "
        "the house in refined 1950s Vietnamese attire, stands on the veranda; the young "
        "{costar}, a household servant in plain áo bà ba holding an oil lamp, approaches. "
        "BOTH faces stay framed FRONTALLY or three-quarter toward the camera at all "
        "times — never in side profile — and when they speak they look directly and "
        "steadily into each other's eyes, gazes precisely aligned and focused, never "
        "crossed or drifting. The {costar} says softly in clear English: \"You shouldn't "
        "be out here — if the family sees us talking, I'll be sent away.\" The person in "
        "Image 1 turns to face them fully, eyes locked on theirs: \"Then let them see. "
        "I'm done pretending.\" Thunder rolls softly; the rain glitters in the "
        "lamplight." + _DUO_A,
        "Continue directly from Video 1 — the same TWO people only, both faces kept "
        "frontal or three-quarter to the camera, their eyes locked directly on each "
        "other whenever they speak. The person from Image 1 steps down into the rain "
        "and gently takes the {costar}'s hand; the {costar}'s eyes, looking straight "
        "into the other's eyes, brim with a single dramatic tear, the oil lamp steady "
        "in their other hand — the iconic rain-drenched confession of classic "
        "Vietnamese period films. The person from Image 1 says in clear English: \"Rich "
        "or poor doesn't matter to me. It never did.\" The {costar} replies, voice "
        "breaking, gaze never leaving them: \"...Then I'll stay. Whatever happens, I'll "
        "stay.\" The original string music swells; the two stand together in the "
        "glittering rain as the oil lamps glow — a sweeping, tearful, timeless "
        "close." + _DUO_B,
    ),
    "noir": (
        "A REALISTIC live-action detective movie scene in old Saigon at night — shot "
        "like real 35mm film footage, absolutely photorealistic: a narrow street of aged "
        "Vietnamese shophouses with peeling paint and worn textures, wet asphalt after "
        "rain reflecting ONLY the actual light sources present — a single bare bulb over "
        "a phở cart, dim warm light from two shophouse windows, one distant streetlamp. "
        "No fog, no haze, no glow effects, no stylized color wash — the natural darkness "
        "of a real street at 1 a.m., true photographic shadows, natural skin tones. "
        "EXACTLY THREE people exist in this video: the person in Image 1 and a young "
        "{costar} — two detectives in plain worn trench coats — plus ONE fleeing figure "
        "seen only briefly and only from behind. The two detectives study a small "
        "notebook near the phở cart. The figure darts from a doorway down the street. "
        "The {costar} snaps in clear English: \"There — that's our lead!\" The person "
        "in Image 1 is already moving: \"Cut through the alley!\" The two give chase — "
        "a quick, realistic sprint, real footsteps splashing shallow puddles, coats "
        "moving with real fabric weight." + _DUO_A,
        "Continue directly from Video 1 — same rules: photorealistic, natural darkness, "
        "only the two detectives now (the figure has escaped; nobody else appears). "
        "They round the corner into an empty dead-end — and on the wet ground under the "
        "streetlamp lies a small dropped key. The person from Image 1 picks it up and "
        "turns it in the light with a slow, knowing smile. The {costar} laughs softly "
        "in clear English: \"The theater locker. It was there all along.\" The person "
        "from Image 1 tips their hat: \"Case closed, partner.\" They shake hands under "
        "the streetlamp and walk back toward the glow of the phở cart — a grounded, "
        "stylish close." + _DUO_B,
    ),
    "horror": (
        "A Vietnamese horror-movie scene, staged with precise control: inside an old "
        "traditional wooden Vietnamese house at midnight — dark carved-wood furniture, "
        "ONE oil lamp as the only light source with a naturally flickering flame, "
        "moonlight through slatted shutters. EXACTLY THREE figures exist in this video: "
        "the person in Image 1, a young {costar}, and ONE pale ghostly woman in a white "
        "dress with long black hair who appears ONLY inside the mirror and ONLY for one "
        "second — she never appears outside the mirror and never moves toward anyone; "
        "nothing in the house ever moves by itself except one door pushed by a visible "
        "draft. Sequence, in order: (1) the two friends walk slowly through the "
        "creaking house, the {costar} holding the oil lamp, real careful footsteps; "
        "(2) a draft makes one wooden door swing slowly shut with a creak — they freeze "
        "back to back; (3) the {costar} whispers in clear English: \"Tell me that was "
        "the wind.\" — the person in Image 1 whispers back: \"...That wasn't the "
        "wind.\"; (4) in the dusty mirror behind them the pale woman appears for one "
        "second, then is gone when they both spin around, eyes wide." + _DUO_A,
        "Continue directly from Video 1 — same three-figure rule; the ghostly woman "
        "appears ONCE more, far down the corridor, standing still for one second only, "
        "then the scene contains only the two friends. When she appears, the two grab "
        "each other's arms and RUN — a realistic panicked sprint through the creaking "
        "house, out the front door, into the moonlit courtyard, where they stop and "
        "double over catching their breath, hands on knees, completely natural human "
        "movement. The {costar} gasps in clear English: \"We are NEVER coming back "
        "here.\" The person from Image 1, half-laughing half-terrified: \"Deal.\" They "
        "look at each other and burst into nervous laughter under the moonlight — a "
        "fun, spooky, shareable close." + _DUO_B,
    ),
    "drama": (
        "A Vietnamese melodrama movie scene, glossy TV-drama style, staged with precise "
        "control: an elegant modern Saigon café in soft natural afternoon window light. "
        "EXACTLY FOUR people appear: the person in Image 1, a young {costar} (their "
        "fiercely loyal best friend), one glamorous seated Vietnamese woman (the "
        "story's scheming 'other woman'), and one waiter far in the background who "
        "never approaches. Sequence, in order: (1) the person in Image 1 and the "
        "{costar} walk in together at a natural pace and stop at the woman's marble "
        "table; (2) the person in Image 1 says in clear English, calm and even: \"I "
        "think you know why I'm here.\" — the seated woman sets down her iced tea and "
        "smirks; (3) the {costar} crosses their arms and says dryly: \"Take your time. "
        "We've got all afternoon.\"; (4) the seated woman rises slowly, still smirking, "
        "smoothing her dress — the standoff holds, three people standing around the "
        "table, tension crackling but nobody touching anyone." + _DUO_A,
        "Continue directly from Video 1 — same four people only, same café. Sequence, "
        "in order: (1) the person from Image 1 calmly picks up the glass of water from "
        "the table with one hand and tips it forward so the water splashes onto the "
        "scheming woman — a real physical splash, the glass staying firmly in hand; "
        "she flinches back with a theatrical gasp, hair and blouse wet (staged drama, "
        "water only, nobody hurt, nobody touched); (2) the person from Image 1 sets "
        "the glass down gently and says in clear English, quiet and final: \"Stay away "
        "from what's mine.\"; (3) the {costar} gives a slow, satisfied nod: \"She "
        "always keeps her word. I'd listen.\"; (4) the two link arms and walk out "
        "together at a natural confident pace, one small hair-flip at the door, while "
        "the scheming woman fumes behind them — an iconic, deliciously dramatic "
        "close." + _DUO_B,
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
