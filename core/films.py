"""The Premiere Pictures film catalog — 6 movie-scene themes, prompts as data.

Each guest stars INSIDE a real movie scene (not behind-the-scenes): action,
adventure, dance, romance, sci-fi, noir — built to showcase Seedance's motion
generation. 15s solo or 30s with an AI co-star. `c1/c2/c3` drive each poster's
gradient (dark -> mid -> glow).
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
    _RULES + " Use the face in Image 1 as the only and exclusive face reference — keep the "
    "facial features and facial structure exactly the same as the reference image. Pace the "
    "dialogue so the final line is completely finished by second 12, then hold a natural "
    "closing beat — never cut off mid-sentence or mid-action. 15 seconds."
)

FILMS = [
    {
        "key": "action", "no": "01", "emoji": "💥",
        "title_th": "ROOFTOP SHOWDOWN", "title_en": "ACTION BLOCKBUSTER",
        "genre_th": "ACTION", "genre_en": "ACTION · THRILLER",
        "logline_en": "One rooftop. No way out. Bring it.",
        "synopsis": ("A night-rain rooftop showdown straight out of a blockbuster — you face "
                     "down masked pursuers with fast, precise martial-arts moves and walk away "
                     "the hero. Pure action-movie adrenaline."),
        "tags": "MARTIAL ARTS · ROOFTOP · HERO",
        "c1": "#0A0E2A", "c2": "#C8321E", "c3": "#F6C55C",
        "prompt": ("A cinematic action-movie scene: a city rooftop at night in light rain, "
                   "neon glow from the skyline below. The person in Image 1, in a sleek plain "
                   "jacket, turns as two masked figures rush in. In fluid, realistic "
                   "martial-arts choreography they sidestep, block a strike, answer with a "
                   "sharp spinning kick and a clean sweep — each move carrying real weight and "
                   "momentum — until the masked figures stumble back and flee into the dark. "
                   "The hero straightens up in the rain, exhales, looks to camera and says in "
                   "clear English: \"Is that all you've got?\" — then walks toward the skyline "
                   "as the rain glitters." + _SUFFIX),
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
                   "sunlight through the canopy, mist over mossy stone. The person in Image 1, "
                   "in rugged plain explorer gear, sprints through a crumbling corridor as "
                   "stone dust falls, vaults a fallen pillar with real athletic effort, grabs "
                   "a hanging vine and swings across a deep chasm, landing in a controlled "
                   "roll. They rise before a stone altar, lift a small golden idol into a "
                   "beam of sunlight, grin at the camera and say in clear English: \"Told you "
                   "the map was real.\" — holding the idol up as the light flares." + _SUFFIX),
    },
    {
        "key": "goldenage", "no": "03", "emoji": "🎞️",
        "title_th": "THE LAST WALTZ", "title_en": "GOLDEN AGE CINEMA",
        "genre_th": "ROMANCE", "genre_en": "ROMANCE · CLASSIC",
        "logline_en": "A waltz the silver screen never forgot.",
        "synopsis": ("A timeless classic-Hollywood romance scene — a candlelit grand ballroom, "
                     "elegant black-tie, and a sweeping waltz with graceful turns and a "
                     "show-stopping finish."),
        "tags": "BALLROOM · WALTZ · TIMELESS",
        "c1": "#1A140A", "c2": "#8A6A2A", "c3": "#F6E08A",
        "prompt": ("A classic-Hollywood romance movie scene in warm golden light: a grand "
                   "candlelit ballroom with chandeliers and marble floors. The person in "
                   "Image 1, in timeless elegant black-tie evening wear, glides alone across "
                   "the floor in a graceful waltz — smooth turns, poised arms, real dancer's "
                   "balance and footwork — as elegantly dressed guests watch admiringly from "
                   "the candlelight. They finish with a slow, elegant spin into a poised final "
                   "pose, look warmly to the camera and say in clear English: \"Some nights "
                   "belong to the silver screen.\" — as the chandeliers glow." + _SUFFIX),
    },
    {
        "key": "dance", "no": "04", "emoji": "🕺",
        "title_th": "OWN THE FLOOR", "title_en": "DANCE FEVER",
        "genre_th": "DANCE", "genre_en": "DANCE · MUSICAL",
        "logline_en": "The floor clears. The beat drops. You own it.",
        "synopsis": ("A high-energy dance-movie scene — the crowd circles up, the beat drops, "
                     "and you tear through a sharp street-dance routine: spins, footwork, a "
                     "freeze that brings the house down."),
        "tags": "STREET DANCE · BATTLE · FREEZE",
        "c1": "#14082A", "c2": "#7A2AB0", "c3": "#57E0F0",
        "prompt": ("A cinematic dance-movie scene: an underground dance floor with warm "
                   "practical lights and a cheering circle of dancers. An original, hard-"
                   "hitting instrumental beat drops and the person in Image 1, in stylish "
                   "plain streetwear, takes the floor — ripping through a sharp, realistic "
                   "street-dance routine: crisp footwork, a smooth spin, a controlled "
                   "shoulder freeze — every move on the beat with real dancer's balance and "
                   "momentum. The circle erupts; the dancer rises, flashes a confident grin "
                   "to camera and says in clear English: \"That's how it's done.\" — as the "
                   "crowd cheers around them." + _SUFFIX),
    },
    {
        "key": "noir", "no": "05", "emoji": "🕵️",
        "title_th": "MIDNIGHT NOIR", "title_en": "FILM NOIR",
        "genre_th": "MYSTERY", "genre_en": "MYSTERY · CLASSIC NOIR",
        "logline_en": "One clue. One chase. Case closed.",
        "synopsis": ("A moody 1940s noir scene in rich cinematic color — rain-slicked streets, a fleeing shadow, a "
                     "sharp chase through the alleys, and the clue that closes the case with "
                     "timeless style."),
        "tags": "DETECTIVE · RAIN · CHASE",
        "c1": "#0A0A0C", "c2": "#2E2E36", "c3": "#D8D8E0",
        "prompt": ("A moody 1940s film-noir movie scene in rich, realistic cinematic color — "
                   "deep blue night tones with warm amber lamplight, natural skin tones, wet "
                   "streets reflecting the glow (NOT black-and-white, no desaturated or "
                   "artificial filter look): a rain-slicked city street at night, lamplight "
                   "cutting through mist. The "
                   "person in Image 1, a noir detective in a plain trench coat and fedora, "
                   "spots a shadowy figure dart from a doorway — and gives chase: a quick, "
                   "realistic pursuit through the rain, splashing through puddles, rounding a "
                   "corner with natural momentum. The figure vanishes, but a small dropped "
                   "notebook lies in the lamplight. The detective picks it up, reads it with "
                   "a slow knowing smile, tips their hat to the camera and says in clear "
                   "English: \"Case closed.\" — then strolls into the mist." + _SUFFIX),
    },
]

FILM_BY_KEY = {f["key"]: f for f in FILMS}


# ---- 30-second two-character version ----
# Visitor = Image 1 (real face). Companion = AI-generated of the chosen gender
# ({costar} = "woman"/"man") described in the prompt (the endpoint allows only one
# real face). Two 15s sequences stitched to 30s; seq B is generated FROM seq A's
# video (reference_video / extend) so the companion + setting don't drift.
_DUO_A = (
    " Cinematic, filmic lighting with rich depth of field. Both people are clearly visible "
    "and share the frame. The person from Image 1 keeps the exact face, hair and look of "
    "Image 1 the whole time — use the face in Image 1 as the only and exclusive face "
    "reference." + _RULES + " End on a satisfying, natural beat — never cut off mid-action. "
    "15 seconds."
)
_DUO_B = (
    " Continue as ONE unbroken film from Video 1 — the exact same two people (the person "
    "from Image 1 keeps the Image 1 face), same hair, same outfits, same world and lighting."
    + _RULES + " Bring the story to a satisfying, natural close — a clear, feel-good final "
    "beat, never an abrupt mid-action cut. 15 seconds."
)

# Each theme is a 30s two-character MOVIE SCENE with a real arc: seq A sets up
# the stakes, seq B pays it off. Dialogue is genuine back-and-forth.
DUO = {
    "action": (
        "A cinematic action-movie scene: a city rooftop at night in light rain, neon glow "
        "from the skyline below. The person in Image 1 and a young {costar}, both heroes in "
        "sleek plain jackets, stand back to back as four masked figures circle them. The "
        "{costar} says in clear English: \"Four against two — hardly fair.\" The person in "
        "Image 1 smirks: \"For them.\" The masked figures rush in and the two heroes explode "
        "into fluid, realistic martial-arts choreography — sidesteps, blocks, a spinning "
        "kick, a clean sweep — every move carrying real weight, balance and momentum." + _DUO_A,
        "Continue directly from Video 1. The two heroes fight in perfect sync — the {costar} "
        "ducks as the person from Image 1 delivers a sharp kick over them, then they counter "
        "side by side until the last masked figures stumble back and flee into the dark. Rain "
        "glitters as the two catch their breath. The {costar} laughs in clear English: "
        "\"You're getting faster.\" The person from Image 1 grins: \"You're getting slower.\" "
        "They bump fists and walk toward the glowing skyline together — a cool, triumphant "
        "close." + _DUO_B,
    ),
    "adventure": (
        "A cinematic adventure-movie scene: ancient jungle temple ruins, sunlight shafting "
        "through the canopy, mist over mossy stone. The person in Image 1 and a young "
        "{costar}, both explorers in rugged plain gear, study a stone map on an altar as the "
        "ground begins to rumble. The {costar} looks up in alarm and says in clear English: "
        "\"The floor's giving way — run!\" The person in Image 1 grabs the golden idol from "
        "the altar: \"Go, go, GO!\" They sprint through the crumbling corridor together, "
        "vaulting fallen pillars as stone dust rains down — real athletic effort and "
        "momentum." + _DUO_A,
        "Continue directly from Video 1. The two explorers reach a deep chasm; the person "
        "from Image 1 grabs a hanging vine, the {costar} holds on, and they swing across "
        "together, landing in a controlled roll as the corridor collapses behind them in a "
        "cloud of dust. Safe in a shaft of sunlight, they catch their breath and start "
        "laughing. The {costar} says in clear English: \"Next time, YOU read the warnings.\" "
        "The person from Image 1 holds up the gleaming golden idol: \"Next time... we bring "
        "a bigger bag.\" They grin and walk out into the light — a classic adventure "
        "close." + _DUO_B,
    ),
    "goldenage": (
        "A classic-Hollywood romance movie scene in warm golden light: a grand candlelit "
        "ballroom with chandeliers and marble floors, elegantly dressed guests at the edges. "
        "The person in Image 1 and a young {costar}, both in timeless elegant black-tie "
        "evening wear, meet at the center of the floor. The {costar} offers a hand and says "
        "in clear English: \"They're all watching, you know.\" The person in Image 1 takes "
        "it with a warm smile: \"Then let's give them something to remember.\" Gentle "
        "original orchestral music rises and they sweep into a graceful, flowing waltz — "
        "real dancer's frame, balance and footwork, turning elegantly across the marble." + _DUO_A,
        "Continue directly from Video 1. The waltz builds — sweeping turns across the "
        "candlelit floor, a graceful underarm spin, the guests watching enchanted — every "
        "step with real dancer's poise and momentum. The music swells and they finish with "
        "a gentle, elegant dip and a poised recovery, holding the final pose as the guests "
        "applaud warmly. The {costar} says softly in clear English: \"Told you they'd "
        "remember.\" The person from Image 1 smiles: \"So will I.\" They share a warm look "
        "under the chandeliers — a timeless, romantic close." + _DUO_B,
    ),
    "dance": (
        "A cinematic dance-movie scene: an underground dance floor with warm practical "
        "lights and a cheering circle of dancers. An original, hard-hitting instrumental "
        "beat drops. The person in Image 1 and a young {costar}, both in stylish plain "
        "streetwear, step into the circle facing each other. The {costar} spreads their "
        "arms with a grin and says in clear English: \"Show me what you've got!\" The "
        "person in Image 1 smiles: \"Try to keep up.\" — and rips into a sharp, realistic "
        "street-dance combo: crisp footwork, a smooth spin, a clean freeze — every move on "
        "the beat with real dancer's balance." + _DUO_A,
        "Continue directly from Video 1. The {costar} answers with their own fiery combo, "
        "then the two dance TOGETHER — a synchronized burst of footwork and spins, "
        "perfectly on the beat, trading moves and mirroring each other with real momentum "
        "and control as the circle goes wild. They hit a final freeze side by side, hold "
        "it, then break into laughter. The {costar} says in clear English: \"Okay — we "
        "OWN this floor.\" The person from Image 1 high-fives them: \"Every night.\" The "
        "crowd cheers around them — an electric, joyful close." + _DUO_B,
    ),
    "noir": (
        "A moody 1940s film-noir movie scene in rich, realistic cinematic color — deep "
        "blue night tones with warm amber lamplight, natural skin tones, wet streets "
        "reflecting the glow (NOT black-and-white, no desaturated or artificial filter "
        "look): a rain-slicked "
        "city street at night, lamplight cutting through mist. The person in Image 1 and a "
        "young {costar}, two noir detectives in plain trench coats and fedoras, study a "
        "small notebook under a streetlamp. Suddenly a shadowy figure darts from a doorway. "
        "The {costar} snaps in clear English: \"There — that's our lead!\" The person in "
        "Image 1 is already moving: \"Cut through the alley!\" The two give chase through "
        "the rain — a quick, realistic pursuit, splashing through puddles, coats flaring "
        "as they round the corner with natural momentum." + _DUO_A,
        "Continue directly from Video 1. The two detectives corner the empty alley — the "
        "figure is gone, but a small key glints on the wet cobblestones under the lamplight. "
        "The person from Image 1 picks it up and holds it to the light with a slow, knowing "
        "smile. The {costar} laughs softly in clear English: \"The theater locker. It was "
        "there all along.\" The person from Image 1 tips their hat: \"Case closed, "
        "partner.\" They shake hands in the glow of the streetlamp and stroll off side by "
        "side into the mist — a stylish, timeless close." + _DUO_B,
    ),
}


def duo_prompts(film_key: str, costar_gender: str):
    """Return (sequence_a, sequence_b) for the 30s version with the AI companion's
    gender filled in. costar_gender is 'woman' or 'man'."""
    pair = DUO.get(film_key)
    if not pair:
        return None
    return tuple(p.replace("{costar}", costar_gender) for p in pair)
