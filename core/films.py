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
        "key": "royal", "no": "03", "emoji": "🏮",
        "title_th": "ONE NIGHT OF FREEDOM", "title_en": "THE ROYAL ESCAPE",
        "genre_th": "CỔ TRANG", "genre_en": "PERIOD · ROYAL",
        "logline_en": "One royal. One night. No guards... almost.",
        "synopsis": ("A lavish Vietnamese costume-drama escapade — a young royal slips out "
                     "of the imperial palace in disguise for one night at the lantern "
                     "market. Silk robes, golden halls, and stolen freedom."),
        "tags": "CỔ TRANG · PALACE · LANTERN MARKET",
        "c1": "#1A0A06", "c2": "#8A2A1E", "c3": "#F6C55C",
        "prompt": ("A lavish Vietnamese period costume-drama movie scene ('phim cổ trang'): "
                   "night inside a grand Vietnamese imperial palace chamber — carved gilded "
                   "wood, silk drapes, candles with small steady flames. All lanterns and "
                   "surfaces are completely blank with no writing or calligraphy anywhere. "
                   "The person in Image 1, a young royal in exquisite plain silk royal "
                   "robes, paces restlessly, then stops at the window hearing distant "
                   "festival music. They pull a plain dark commoner's cloak over the silk "
                   "robes, look to the camera with a mischievous grin and say in clear "
                   "English: \"The palace can spare me for one night.\" — then slip "
                   "quietly out the door into the lantern-lit night, glancing back once "
                   "with a smile." + _SUFFIX),
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
    "royal": (
        "A lavish Vietnamese period costume-drama movie scene ('phim cổ trang'): night "
        "inside a grand Vietnamese imperial palace chamber — carved gilded wood, silk "
        "drapes, candles with small steady flames that never flare or spark. All "
        "lanterns, banners and surfaces are completely BLANK with no writing or "
        "calligraphy anywhere. EXACTLY TWO people appear in this sequence: the person "
        "in Image 1, a young royal in exquisite plain silk royal robes, and a young "
        "{costar}, their fiercely loyal royal guard in plain dark guard attire. The "
        "royal stares out the window toward distant festival music, restless. The "
        "{costar} steps in carrying a folded plain dark commoner's cloak and says in "
        "clear English, half-smiling: \"If anyone asks — I tried to stop you.\" The "
        "person in Image 1 grins, swinging the cloak over their robes: \"You're the "
        "worst guard in the kingdom. Let's go.\" The two slip out of the chamber "
        "together, hushed and giddy, the guard checking the corridor first." + _DUO_A,
        "Continue directly from Video 1. The two arrive at a bustling Vietnamese "
        "night lantern market just outside the palace walls — dozens of plain unlit-"
        "text silk lanterns glowing warm and steady overhead, Vietnamese market-goers "
        "strolling in the background (they stay in the background and never approach). "
        "The royal, hood down now, wanders wide-eyed between the lantern stalls, "
        "touching nothing yet beaming at everything; the {costar} stays close, "
        "half-vigilant, half-smiling. The royal picks up one small plain paper "
        "lantern with both hands, turns to the {costar} and says in clear English: "
        "\"One night of freedom is worth a thousand thrones.\" The {costar} laughs "
        "quietly: \"Then we'd better not get caught.\" They share a conspiratorial "
        "grin and stroll deeper into the warm glow of the market together — a "
        "charming, cinematic close." + _DUO_B,
    ),
    "noir": (
        "A REALISTIC live-action detective movie scene in old Saigon at night — shot "
        "like real 35mm film footage, absolutely photorealistic: a narrow street of "
        "aged Vietnamese shophouses with peeling paint and worn textures, wet asphalt "
        "after rain reflecting ONLY the actual light sources present — a single bare "
        "bulb over a small phở cart, dim warm light from two shophouse windows, one "
        "distant streetlamp. No fog, no haze, no glow effects, no stylized color wash "
        "— the natural darkness of a real street at 1 a.m., true photographic shadows, "
        "natural skin tones. THE SET IS FIXED: every shopfront shutter, door and gate "
        "in the street is CLOSED and stays closed for the entire video — nothing ever "
        "opens, closes, or changes anywhere in the environment; all shop signs and "
        "surfaces are completely BLANK with no lettering. EXACTLY THREE people exist "
        "in this video: the person in Image 1 and a young {costar} — two detectives "
        "ALREADY WEARING plain worn trench coats AND fedora hats from the very first "
        "frame (the hats stay firmly on through all the running) — plus ONE fleeing "
        "figure seen only briefly and only from behind. The two detectives stand near "
        "the phở cart studying a small unmarked notebook when the figure darts from a "
        "shadowed corner down the street. The {costar} snaps in clear English: "
        "\"There — that's our lead!\" The person in Image 1 is already moving: "
        "\"Don't lose him!\" The two sprint down the street after the figure — "
        "quick, realistic running, real footsteps splashing shallow puddles, coats "
        "moving with real fabric weight, past the same closed shutters." + _DUO_A,
        "Continue directly from Video 1 — the IDENTICAL street: same closed shutters "
        "and doors (still closed, nothing has opened or changed), same phở cart, same "
        "three light sources, photorealistic and naturally dark. Only the two "
        "detectives remain — the fleeing figure has escaped and never appears again. "
        "They slow to a stop where the street bends, breathing hard — the figure is "
        "gone — and there on the wet asphalt under the streetlamp lies a small "
        "dropped brass key. The person from Image 1 crouches, picks it up and turns "
        "it in the light with a slow, knowing smile. The {costar} laughs softly in "
        "clear English: \"The theater locker. It was there all along.\" The person "
        "from Image 1 tips their hat: \"Case closed, partner.\" They shake hands "
        "under the streetlamp and walk back toward the warm bulb of the phở cart — a "
        "grounded, stylish close." + _DUO_B,
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
        "control: an elegant modern Saigon café terrace in soft natural afternoon "
        "window light — the café interior is completely FREE of any text: no menus, no "
        "signs, no chalkboards, no posters, no labels, no wall art with writing of any "
        "kind. EXACTLY THREE people appear in this entire video and NEVER "
        "anyone else — no waiter, no passers-by, no background people at all: (a) the "
        "person in Image 1, dressed in an elegant flowing LONG CREAM-colored dress "
        "(soft ivory/cream tone, ankle-length, refined and expensive-looking) with heels — "
        "NEVER black clothing, NEVER a school uniform, NEVER the clothing from the "
        "reference photo; (b) a young {costar} — the person in Image 1's PARTNER, "
        "who is cheating; (c) one glamorous Vietnamese woman — the story's notorious "
        "'tiểu tam'. Sequence, in order: (1) the {costar} and the glamorous woman sit "
        "cozily together at a marble café table, laughing, her hand resting on the "
        "{costar}'s arm, two glasses of iced tea on the table; (2) the person in "
        "Image 1 walks in, stops dead at the sight — a long, devastating beat as "
        "their expression hardens from shock to icy calm; (3) they walk slowly to the "
        "table and stop DIRECTLY FACING the seated couple — body and face turned "
        "TOWARD the two of them at all times, eyes locked on them, NEVER turning "
        "their back to the couple while confronting them (the camera views the "
        "confrontation from a three-quarter angle so the Image 1 face stays visible "
        "while clearly facing the pair); the {costar} freezes mid-laugh, going pale, "
        "and stammers in clear English: \"...It's — it's not what it looks like.\"; "
        "(4) the glamorous woman just smirks and clings tighter to the {costar}'s "
        "arm; the person in Image 1 stands facing them in dead silence, tension at "
        "maximum." + _DUO_A,
        "Continue directly from Video 1 — the same THREE people only, nobody else "
        "ever appears; the person from Image 1 remains DIRECTLY FACING the seated "
        "couple throughout steps 1-3, body and eyes toward them, never turning away "
        "until the final exit. Sequence, in order: (1) the person from Image 1 says "
        "in clear English, quiet and razor-sharp: \"Funny. It looks exactly like "
        "what it is.\"; (2) they calmly pick up ONE glass of iced tea from the table with one "
        "hand and tip it forward so it splashes over BOTH the {costar} and the "
        "glamorous woman — one real physical splash, the glass staying firmly in "
        "hand; the two flinch back with theatrical gasps, drenched (staged drama, "
        "liquid only, nobody hurt, nobody touched); (3) the person from Image 1 sets "
        "the glass down gently, looks at the pair and delivers the final line in "
        "clear English: \"Keep each other. You deserve it.\"; (4) they turn and walk "
        "out at a natural, unhurried, queenly pace with one small hair-flip — the "
        "camera following their confident exit while the two cheaters sit frozen and "
        "dripping behind them — an iconic, deliciously dramatic close." + _DUO_B,
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
