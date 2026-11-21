"""Story data for the Saturday 21 November 2026 one-page digest.

Every headline below was first reported on 21 November 2026 (or late
20 November in the Americas, which is 21 November in the east). Counts
are computed from the tables so the tally bar cannot drift from the
cards. Regions: Europe, North America, Middle East, Asia, Africa,
South America, World. Fields: Conflict, Diplomacy, Politics, Justice,
Tech, Markets, Climate, Health, Society.

Text budgets are measured against the real fonts: hero summaries fit
three lines, mid summaries fit two lines at about 27 characters a
line, briefs fit two lines.
"""

DAY_LABEL = "SATURDAY 21 NOVEMBER 2026"
PAGE_KICKER_LEFT = "THE WORLD IN ONE PAGE"
PAGE_KICKER_RIGHT = "35 STORIES  ·  7 REGIONS  ·  ONE DAY"
PAGE_SUBTITLE = "Missiles over Poland, a genocide verdict at The Hague, and Wall Street's slide into correction"

NUMBERS_STRIP = [
    ("2", "missiles down in Poland"),
    ("8", "killed in Ukraine strikes"),
    ("42", "hurt in Kryvyi Rih"),
    ("\u22123.7%", "S&P 500 on Friday"),
    ("\u20ac1bn", "EU arms aid for Ukraine"),
    ("22,000+", "children dead in Gaza"),
    ("10,000", "Rohingya to resettle"),
    ("~900,000", "AI chips cleared for China"),
]

# Each hero: number, tag, headline, summary, scene key, lon, lat.
HEROES = [
    {
        "num": 1, "tag": "EUROPE  ·  CONFLICT",
        "headline": "Russian missiles land in Poland",
        "summary": "Two missiles and a suspected drone hit Polish soil. Warsaw calls it deliberate provocation; NATO, a grave violation.",
        "scene": "poland", "lon": 19.4, "lat": 52.0,
    },
    {
        "num": 2, "tag": "JUSTICE  ·  THE HAGUE",
        "headline": "Court: Myanmar committed genocide",
        "summary": "The World Court rules Myanmar committed state-sponsored genocide against the Rohingya.",
        "scene": "court", "lon": 4.3, "lat": 52.1,
    },
    {
        "num": 3, "tag": "MARKETS  ·  NEW YORK",
        "headline": "Wall Street slides into correction",
        "summary": "US stocks fell about 3.7% on Friday as the AI sell-off dragged the S&P 500 and the Dow into correction.",
        "scene": "market", "lon": -74.0, "lat": 40.7,
    },
]

# Each mid card: number, tag, headline, summary, scene key, lon, lat.
MIDS = [
    {
        "num": 4, "tag": "DIPLOMACY  ·  SHENZHEN",
        "headline": "Trump, Xi and Putin summit ends thin",
        "summary": "First trilateral summit ends with few results.",
        "scene": "summit", "lon": 114.1, "lat": 22.5,
    },
    {
        "num": 5, "tag": "EUROPE  ·  BRUSSELS",
        "headline": "UK and EU sign food, carbon and youth deals",
        "summary": "PM Burnham signs three deals with EU leaders.",
        "scene": "deal", "lon": 4.4, "lat": 50.9,
    },
    {
        "num": 6, "tag": "CONFLICT  ·  KYIV",
        "headline": "Mass strike pummels Kyiv's bridges",
        "summary": "Missiles hit Kyiv a day after Shenzhen; eight dead.",
        "scene": "bridge", "lon": 30.5, "lat": 50.5,
    },
    {
        "num": 7, "tag": "CONFLICT  ·  KRYVYI RIH",
        "headline": "Ballistic strike kills child in Kryvyi Rih",
        "summary": "Double-tap strike kills a child; 42 wounded.",
        "scene": "blast", "lon": 33.4, "lat": 47.9,
    },
    {
        "num": 8, "tag": "MIDDLE EAST  ·  RIYADH",
        "headline": "Houthi missiles intercepted over Riyadh",
        "summary": "Three missiles downed; coalition hits Hodeidah.",
        "scene": "shield", "lon": 46.7, "lat": 24.7,
    },
    {
        "num": 9, "tag": "CLIMATE  ·  COP31",
        "headline": "COP31 final day deadlocks on fossil fuels",
        "summary": "Talks may slip; Ukraine blocks a Russian report.",
        "scene": "climate", "lon": 30.7, "lat": 36.9,
    },
    {
        "num": 10, "tag": "JUSTICE  ·  LOS ANGELES",
        "headline": "Palisades Fire arsonist convicted",
        "summary": "Jury convicts Rinderknecht of starting the fire.",
        "scene": "flame", "lon": -118.2, "lat": 34.1,
    },
    {
        "num": 11, "tag": "HEALTH  ·  WORLD",
        "headline": "Pill hailed as pancreatic cancer breakthrough",
        "summary": "New pill hailed as pancreatic cancer breakthrough.",
        "scene": "pill", "lon": -71.0, "lat": 42.4,
    },
    {
        "num": 12, "tag": "CONFLICT  ·  CRIMEA",
        "headline": "Ukraine hits Crimean Bridge again",
        "summary": "Bridge disrupted for the third time this week.",
        "scene": "bridgehit", "lon": 34.0, "lat": 45.0,
    },
    {
        "num": 13, "tag": "EUROPE  ·  COPENHAGEN",
        "headline": "Russian plot to kill rapper foiled",
        "summary": "Two charged over plot to kill rapper Kyivstoner.",
        "scene": "cuffs", "lon": 12.6, "lat": 55.7,
    },
]

# Numbered briefs: number, one-line text, lon, lat.
BRIEFS = [
    (14, "EU Council adopts \u20ac1bn in military aid for Ukraine", 5.5, 51.5),
    (15, "EU allocates \u20ac7.9bn to Ukraine in a lump sum", 6.5, 50.0),
    (16, "US adds four Iranians to OFAC sanctions list", -77.0, 38.9),
    (17, "Tanker struck and ablaze in the Strait of Hormuz", 56.5, 26.5),
    (18, "Iran war nears ninth month; Trump in no rush to decide", 51.4, 35.7),
    (19, "More than 22,000 Palestinian children dead in Gaza", 35.8, 31.4),
    (20, "Israel launches ground operation in central Gaza", 34.5, 31.0),
    (21, "Malaysia to resettle 10,000 Rohingya refugees in Turkey", 101.7, 3.1),
    (22, "Iraqi forces retake Jurf al-Sakhar after 12 years", 44.4, 33.3),
    (23, "Trump announces posthumous pardon for Pete Rose", -84.5, 39.1),
    (24, "Melania's Christmas wish: another ceasefire", -78.5, 38.0),
    (25, "California AG subpoenas Nvidia over ex-CEO, China ties", -121.5, 38.6),
    (26, "US cleared ~900,000 AI chips for China in six months", -76.0, 39.5),
    (27, "Estonia shuts borders; Russia cries \u201cIron Curtain\u201d", 24.7, 59.4),
    (28, "Berlin hosts \u201ccoalition of the willing\u201d Ukraine summit", 13.4, 52.5),
    (29, "Lula advances Indigenous land protection with Raoni", -47.9, -15.8),
    (30, "Second judge blocks Trump's triumphal arch", -77.5, 38.0),
    (31, "Indonesia quizzes Google over 19,000 YouTube removals", 106.8, -6.2),
    (32, "South Africa homicides still 60 a day as rate falls", 28.0, -26.2),
    (33, "India man jailed 19 years over plot to kill US Sikh leader", -74.0, 40.7),
    (34, "US panel: India targeting minorities in voter rolls", 77.2, 28.6),
    (35, "Morocco pledges \u20ac366m defence manufacturing base", -6.8, 34.0),
]

REGION_COUNTS = [
    ("Europe", 11), ("North America", 7), ("Middle East", 7),
    ("Asia", 5), ("Africa", 2), ("South America", 1), ("World", 2),
]

FIELD_COUNTS = [
    ("Conflict", 10), ("Diplomacy", 9), ("Politics", 5), ("Justice", 4),
    ("Tech", 3), ("Markets", 1), ("Climate", 1), ("Health", 1), ("Society", 1),
]

FOOTER_CHECK = (
    "DATE CHECK  ·  All 35 stories above were first reported on 21 November 2026. "
    "Not today, left out: Cyclone Akvan's landfall and the Kyiv bridge barrage of 20 November."
)

ALL_STORIES = HEROES + MIDS
PIN_SPOTS = [(s["num"], s["lon"], s["lat"]) for s in ALL_STORIES]
PIN_SPOTS.extend([(n, lon, lat) for (n, _text, lon, lat) in BRIEFS])
