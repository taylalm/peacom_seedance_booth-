"""The Premiere Pictures film catalog — 3 cinema themes, prompts as data.

Each guest stars in a 15s (solo) or 30s (with an AI co-star) English-spoken
film-and-production themed clip. Marketing can tune everything here without
touching app code. `c1/c2/c3` drive each poster's gradient (dark -> mid -> glow).
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
    "life. Present the ENTIRE clip as a single continuous full-frame shot from one camera: no "
    "split-screen, no grids, tiles, collage or picture-in-picture. Natural realistic human "
    "movement with visible weight and effort, smooth animation, no flickering."
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
        "title_th": "STUNT UNIT", "title_en": "ACTION BLOCKBUSTER",
        "genre_th": "ACTION", "genre_en": "ACTION · ON SET",
        "logline_en": "Lights. Camera. Adrenaline.",
        "synopsis": ("You're the action star on a big-budget film set — wind machines, camera "
                     "cranes, a rooftop chase scene. You nail the hero stunt in one take and "
                     "the crew erupts. A high-octane movie-set moment."),
        "tags": "STUNT · FILM SET · ONE TAKE",
        "c1": "#0A0E2A", "c2": "#C8321E", "c3": "#F6C55C",
        "prompt": ("The person in Image 1 is the lead action star on a big-budget film set — a "
                   "dramatic rooftop scene at dusk with camera cranes, wind machines and crew "
                   "at the edges of frame. A director calls \"Action!\" and the star sprints "
                   "across the rooftop, vaults a low barrier with real athletic effort and "
                   "lands a controlled hero slide, holding the finish as the wind whips their "
                   "jacket. The director calls \"Cut!\" and the crew applauds warmly; the star "
                   "looks to camera, catches their breath and says in clear English: \"And "
                   "THAT is how we make movies.\"" + _SUFFIX),
    },
    {
        "key": "redcarpet", "no": "02", "emoji": "✨",
        "title_th": "OPENING NIGHT", "title_en": "RED CARPET PREMIERE",
        "genre_th": "GLAMOUR", "genre_en": "GLAMOUR · PREMIERE",
        "logline_en": "Your film. Your night. Your carpet.",
        "synopsis": ("You arrive at the glamorous premiere of your own film — stepping from a "
                     "classic car onto the red carpet, camera flashes sparkling, fans waving. "
                     "A movie-star entrance from start to finish."),
        "tags": "PREMIERE · FLASHBULBS · GLAMOUR",
        "c1": "#2A0A14", "c2": "#A01838", "c3": "#F6C55C",
        "prompt": ("Night outside a grand cinema at a film premiere. The person in Image 1, "
                   "dressed in elegant plain formal wear, steps out of a classic black car "
                   "onto a long red carpet as camera flashes sparkle and fans wave behind "
                   "velvet ropes. They walk the carpet with easy movie-star confidence, pause "
                   "at a plain elegant backdrop, give a graceful wave and say to an "
                   "interviewer's microphone in clear English: \"This film means everything "
                   "to me — enjoy the show.\" They flash a warm smile and continue toward the "
                   "glowing theater doors." + _SUFFIX),
    },
    {
        "key": "goldenage", "no": "03", "emoji": "🎞️",
        "title_th": "SILVER SCREEN", "title_en": "GOLDEN AGE CINEMA",
        "genre_th": "CLASSIC", "genre_en": "CLASSIC · TIMELESS",
        "logline_en": "Step into the silver screen.",
        "synopsis": ("You're a classic movie star on a vintage Hollywood soundstage — warm "
                     "key lights, an old film camera rolling, timeless black-tie elegance. A "
                     "graceful scene straight from cinema's golden age."),
        "tags": "VINTAGE · SOUNDSTAGE · ELEGANCE",
        "c1": "#1A140A", "c2": "#8A6A2A", "c3": "#F6E08A",
        "prompt": ("A vintage 1950s Hollywood soundstage bathed in warm golden key light — an "
                   "old film camera on a wooden tripod, soft spotlights, art-deco set pieces. "
                   "The person in Image 1, dressed in timeless elegant black-tie evening wear, "
                   "stands in the spotlight like a classic movie star. They deliver a graceful "
                   "slow turn toward the lens, tip their head with old-Hollywood charm and say "
                   "in clear English: \"They don't make them like this anymore.\" The director "
                   "calls \"Cut — beautiful!\" and the small crew applauds as the star smiles "
                   "under the warm lights." + _SUFFIX),
    },
    {
        "key": "director", "no": "04", "emoji": "🎬",
        "title_th": "FINAL CUT", "title_en": "THE DIRECTOR'S CHAIR",
        "genre_th": "DIRECTOR", "genre_en": "DIRECTOR · ON SET",
        "logline_en": "Today, the set answers to you.",
        "synopsis": ("You're the director on a bustling soundstage — crew everywhere, lights "
                     "rigging up, a camera crane sweeping. You call the shot, the set springs "
                     "to life, and the take is perfect. Pure filmmaker energy."),
        "tags": "DIRECTOR · SOUNDSTAGE · THAT'S A WRAP",
        "c1": "#101014", "c2": "#37343E", "c3": "#F6C55C",
        "prompt": ("The person in Image 1 is a film director on a bustling movie soundstage — "
                   "crew adjusting big studio lights, a camera crane sweeping overhead, set "
                   "pieces everywhere. Wearing a stylish plain jacket and headphones around "
                   "their neck, they rise from a classic director's chair, raise a hand and "
                   "call in clear English: \"Quiet on set — and... action!\" The set springs "
                   "to life around them; they watch intently, then break into a proud smile, "
                   "and call: \"Cut! Perfect — that's a wrap.\" The crew applauds warmly as "
                   "the director takes a happy little bow." + _SUFFIX),
    },
    {
        "key": "scifi", "no": "05", "emoji": "🚀",
        "title_th": "STARBOUND", "title_en": "SCI-FI EPIC",
        "genre_th": "SCI-FI", "genre_en": "SCI-FI · SPACE",
        "logline_en": "Strap in. The galaxy is rolling.",
        "synopsis": ("You're the star pilot of a gleaming starship — a luminous bridge, a "
                     "sweeping nebula outside the viewport, a heroic course set for a "
                     "breathtaking alien dawn. Big-screen space adventure."),
        "tags": "STARSHIP · NEBULA · HERO PILOT",
        "c1": "#060A24", "c2": "#1E3CA8", "c3": "#57E0F0",
        "prompt": ("The person in Image 1 is the star pilot of a gleaming starship in a "
                   "cinematic space epic — a sleek bridge bathed in soft blue light, a vast "
                   "luminous nebula drifting past the viewport. Wearing a plain futuristic "
                   "flight suit, they settle into the pilot seat, grip the controls with calm "
                   "confidence and say in clear English: \"Setting course — hold on tight.\" "
                   "The ship glides forward through shimmering stardust as light sweeps "
                   "across their face; they watch a breathtaking alien sunrise crest over a "
                   "ringed planet, smile and say: \"Now THAT is worth the trip.\"" + _SUFFIX),
    },
    {
        "key": "noir", "no": "06", "emoji": "🕵️",
        "title_th": "MIDNIGHT NOIR", "title_en": "FILM NOIR",
        "genre_th": "MYSTERY", "genre_en": "MYSTERY · CLASSIC NOIR",
        "logline_en": "One clue. One night. One legend.",
        "synopsis": ("You're the detective in a moody 1940s film noir — rain-slicked streets, "
                     "a trench coat, dramatic lamplight shadows. You piece the mystery "
                     "together and close the case with timeless style."),
        "tags": "DETECTIVE · RAIN · LAMPLIGHT",
        "c1": "#0A0A0C", "c2": "#2E2E36", "c3": "#D8D8E0",
        "prompt": ("A moody 1940s film-noir scene in stylish black-and-white: a rain-slicked "
                   "city street at night, dramatic lamplight cutting through mist. The person "
                   "in Image 1 is a classic noir detective in a plain trench coat and fedora, "
                   "standing under a streetlamp studying a small notebook. Rain glitters in "
                   "the light as they look up slowly, narrow their eyes with a knowing smile "
                   "and say in clear English: \"Of course... it was there all along.\" They "
                   "snap the notebook shut, tip their hat to the camera and say: \"Case "
                   "closed.\" then stroll off into the misty light." + _SUFFIX),
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

# Each theme is a 30s two-character short with a real arc: seq A sets up the
# stakes, seq B pays it off. Dialogue is written as genuine back-and-forth.
DUO = {
    "action": (
        "A big-budget film set: a dramatic rooftop scene at dusk with camera cranes, wind "
        "machines and crew at the edges of frame. The person in Image 1 and a young {costar}, "
        "both lead action stars in plain rugged stunt wardrobe, take their marks side by side. "
        "The {costar} says in clear English: \"Last shot of the day — ready for the big one?\" "
        "The person in Image 1 nods with a grin: \"On 'action', we fly.\" The director calls "
        "\"Action!\" and the two sprint across the rooftop together in one smooth athletic "
        "take, vaulting a low barrier in perfect sync." + _DUO_A,
        "Continue directly from Video 1. The two stars land their final move together — a "
        "controlled slide into frame, holding the hero pose as the wind whips around them. "
        "The director calls \"Cut — that's the one!\" and the crew applauds warmly. The two "
        "catch their breath and burst out laughing. The {costar} says in clear English: \"One "
        "take. We got it in ONE take!\" The person from Image 1 high-fives them: \"That's "
        "movie magic.\" They walk off set together, still grinning, as the crew resets the "
        "lights — a warm, triumphant close." + _DUO_B,
    ),
    "redcarpet": (
        "Night outside a grand cinema at a glamorous film premiere. A classic black car "
        "pulls up to the red carpet; the person in Image 1 steps out in elegant plain formal "
        "wear, then offers a hand to a young {costar} in equally elegant plain formal wear — "
        "their co-star in the film. Camera flashes sparkle; fans wave behind velvet ropes. "
        "The {costar} takes in the scene and says in clear English: \"Can you believe this is "
        "OUR film?\" The person in Image 1 smiles: \"We made this together — let's enjoy every "
        "second.\" They walk the carpet side by side, waving graciously." + _DUO_A,
        "Continue directly from Video 1. The two co-stars pause at a plain elegant backdrop "
        "for photos, striking a poised, friendly pose as flashes sparkle. An interviewer "
        "offers a microphone; the {costar} leans in and says in clear English: \"Working with "
        "this one was the best part.\" The person from Image 1 laughs warmly: \"Right back at "
        "you — this film means everything to us.\" They share a proud smile, link arms and "
        "walk together through the glowing theater doors as the doors swing open to warm "
        "light — a grand, glamorous close." + _DUO_B,
    ),
    "goldenage": (
        "A vintage 1950s Hollywood soundstage in warm golden key light — an old film camera "
        "on a wooden tripod, soft spotlights, art-deco set pieces. The person in Image 1 and "
        "a young {costar}, both classic movie stars in timeless elegant black-tie evening "
        "wear, take the stage as a director calls \"Rolling... action.\" The {costar} offers "
        "a hand and says in clear English: \"Shall we give them a scene to remember?\" The "
        "person in Image 1 takes it with old-Hollywood charm: \"Follow my lead.\" Gentle "
        "original orchestral music rises and they glide into a graceful, unhurried ballroom "
        "dance under the spotlight." + _DUO_A,
        "Continue directly from Video 1. The dance sweeps gracefully on across the soundstage, "
        "the two stars turning smoothly in the warm spotlight, the old camera tracking them. "
        "They finish with an elegant final pose — a gentle dip and a poised recovery. The "
        "director calls \"Cut — that's a wrap!\" and the small crew applauds. The two laugh "
        "softly, take a playful little bow toward the crew, and stroll off the set together "
        "under the golden lights — a warm, timeless close." + _DUO_B,
    ),
    "director": (
        "A bustling movie soundstage — big studio lights rigging up, a camera crane sweeping "
        "overhead, crew moving set pieces. The person in Image 1 is the film director in a "
        "stylish plain jacket, and a young {costar} is their trusted cinematographer with a "
        "camera rig. The {costar} frames a shot with their hands and says in clear English: "
        "\"If we shoot it from here, it'll be legendary.\" The person in Image 1 studies the "
        "angle, nods with a grin: \"That's why you're the best — places, everyone!\" They "
        "take positions as the set springs to life." + _DUO_A,
        "Continue directly from Video 1. The person from Image 1 raises a hand and calls "
        "\"Action!\" — the crane glides, the lights bloom, and the {costar} tracks a smooth "
        "sweeping shot as the director watches, spellbound. The person from Image 1 calls "
        "\"Cut!\" and the whole crew applauds. The {costar} lowers the camera and says in "
        "clear English: \"That's the best shot we've ever made.\" The person from Image 1 "
        "laughs proudly: \"THAT is movie magic — that's a wrap!\" They share a happy "
        "high-five as the crew celebrates around them — a joyful, triumphant close." + _DUO_B,
    ),
    "scifi": (
        "A cinematic space epic: the sleek bridge of a gleaming starship bathed in soft blue "
        "light, a vast luminous nebula drifting past the viewport. The person in Image 1 and "
        "a young {costar}, both star pilots in plain futuristic flight suits, settle into the "
        "twin pilot seats. The {costar} runs a hand over the controls and says in clear "
        "English: \"No one's ever flown through that nebula.\" The person in Image 1 grips "
        "the controls with a calm smile: \"Then let's be the first.\" The ship glides forward "
        "into the shimmering stardust as light sweeps across their faces." + _DUO_A,
        "Continue directly from Video 1. The starship sails gracefully through glowing bands "
        "of stardust, colors washing over the bridge, the two pilots flying in smooth "
        "coordination. They emerge into clear space just as a breathtaking alien sunrise "
        "crests over a ringed planet, filling the viewport with golden light. The {costar} "
        "whispers in clear English: \"It's beautiful...\" The person from Image 1 smiles: "
        "\"And we made it here together.\" They share a triumphant fist-bump and watch the "
        "sunrise side by side — a wondrous, uplifting close." + _DUO_B,
    ),
    "noir": (
        "A moody 1940s film-noir scene in stylish black-and-white: a rain-slicked city "
        "street at night, dramatic lamplight cutting through mist. The person in Image 1 and "
        "a young {costar}, two classic noir detectives in plain trench coats and fedoras, "
        "stand under a streetlamp studying a small notebook together, rain glittering in the "
        "light. The {costar} taps the page and says in clear English: \"Every clue points to "
        "the old theater.\" The person in Image 1 narrows their eyes with a knowing smile: "
        "\"Then the show's about to end.\" They turn up their collars and stride off through "
        "the rain together." + _DUO_A,
        "Continue directly from Video 1. The two detectives arrive at the grand doors of an "
        "old theater; the person from Image 1 finds a small key tucked above the door frame "
        "and holds it up — the missing piece. The {costar} laughs softly in clear English: "
        "\"It was there all along. You never miss.\" The person from Image 1 tips their hat "
        "with a wry smile: \"Case closed, partner.\" They shake hands under the marquee "
        "lights and stroll off side by side into the misty lamplight — a stylish, satisfying "
        "close." + _DUO_B,
    ),
}


def duo_prompts(film_key: str, costar_gender: str):
    """Return (sequence_a, sequence_b) for the 30s version with the AI companion's
    gender filled in. costar_gender is 'woman' or 'man'."""
    pair = DUO.get(film_key)
    if not pair:
        return None
    return tuple(p.replace("{costar}", costar_gender) for p in pair)
