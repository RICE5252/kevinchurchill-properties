"""Sample Lagos homes. Edit this file to change the board."""

AREAS = [
    {"slug": "ikoyi", "name": "Ikoyi", "line": "Crescents, embassies, old trees."},
    {"slug": "victoria-island", "name": "Victoria Island", "line": "Lagoon flats above the offices."},
    {"slug": "lekki-phase-1", "name": "Lekki Phase 1", "line": "Admiralty and the quiet closes."},
    {"slug": "banana-island", "name": "Banana Island", "line": "Waterfront, gated, very few streets."},
    {"slug": "eko-atlantic", "name": "Eko Atlantic", "line": "A new city on the sea wall."},
    {"slug": "oniru", "name": "Oniru", "line": "Between the Island and Lekki."},
    {"slug": "ikeja-gra", "name": "Ikeja GRA", "line": "Mainland houses with gardens."},
    {"slug": "yaba", "name": "Yaba", "line": "Flats near campus and the railway."},
    {"slug": "magodo", "name": "Magodo", "line": "Family duplexes, phase by phase."},
    {"slug": "ajah", "name": "Ajah", "line": "Newer estates east of Lekki."},
]

HOME_TYPES = ["Duplex", "Apartment", "Terrace", "Bungalow", "Penthouse"]

PRICE_STOPS = {
    "buy": [0, 200_000_000, 400_000_000, 700_000_000, 1_000_000_000, 2_000_000_000, 5_000_000_000],
    "rent": [0, 5_000_000, 12_000_000, 25_000_000, 50_000_000],
    "shortlet": [0, 100_000, 200_000, 400_000],
}

INTENTS = ("buy", "rent", "shortlet")
SORTS = ("featured", "price-asc", "price-desc")

LISTINGS = [
    {
        "id": "glover-duplex",
        "title": "Four-bedroom duplex on Glover Road",
        "intent": "buy",
        "price": 1_150_000_000,
        "area_slug": "ikoyi",
        "street": "Along Glover Road",
        "beds": 4,
        "baths": 5,
        "area_sqm": 420,
        "type": "Duplex",
        "lat": 6.4542,
        "lng": 3.4368,
        "photos": ["ikoyi.jpg", "kitchen.jpg", "flat.jpg"],
        "summary": "Set back from the crescent behind a limestone screen and a single palm. The ground floor is one room long enough for a table of twelve; the study faces the garden.",
        "year": 2021,
        "parking": 4,
        "title_doc": "Governor's Consent",
        "service_charge": "₦8.5m / year",
        "furnishing": "Unfurnished",
        "listed": "2026-03-02",
        "featured": True,
    },
    {
        "id": "banana-waterfront",
        "title": "Five-bedroom house on the lagoon",
        "intent": "buy",
        "price": 4_800_000_000,
        "area_slug": "banana-island",
        "street": "Lagoon front, Banana Island",
        "beds": 5,
        "baths": 6,
        "area_sqm": 780,
        "type": "Duplex",
        "lat": 6.4678,
        "lng": 3.4462,
        "photos": ["banana.jpg", "flat.jpg", "suite.jpg"],
        "summary": "A low house between the drive and the water, with a pool court on the lagoon side. Built for a household that uses the ground floor, not just the driveway.",
        "year": 2019,
        "parking": 6,
        "title_doc": "Certificate of Occupancy",
        "service_charge": "Estate levy, on request",
        "furnishing": "Part furnished",
        "listed": "2026-02-14",
        "featured": True,
    },
    {
        "id": "admiralty-terrace",
        "title": "Four-bedroom terrace off Admiralty",
        "intent": "buy",
        "price": 420_000_000,
        "area_slug": "lekki-phase-1",
        "street": "Off Admiralty Way",
        "beds": 4,
        "baths": 4,
        "area_sqm": 280,
        "type": "Terrace",
        "lat": 6.4488,
        "lng": 3.4702,
        "photos": ["lekki.jpg", "kitchen.jpg", "suite.jpg"],
        "summary": "Clay render, a narrow garden, and a gate that does not face the express. The service charge is posted with the listing, not added after you have already driven over.",
        "year": 2023,
        "parking": 2,
        "title_doc": "Governor's Consent",
        "service_charge": "₦2.4m / year",
        "furnishing": "Unfurnished",
        "listed": "2026-04-08",
        "featured": False,
    },
    {
        "id": "eko-penthouse",
        "title": "Penthouse on the Eko Atlantic sea wall",
        "intent": "buy",
        "price": 980_000_000,
        "area_slug": "eko-atlantic",
        "street": "Eko Atlantic",
        "beds": 3,
        "baths": 4,
        "area_sqm": 310,
        "type": "Penthouse",
        "lat": 6.4136,
        "lng": 3.4124,
        "photos": ["eko.jpg", "flat.jpg", "kitchen.jpg"],
        "summary": "One floor in a glass tower, Atlantic to the south. The service charge is real, and so is the sea wall. A city apartment, not a compound.",
        "year": 2024,
        "parking": 2,
        "title_doc": "Governor's Consent",
        "service_charge": "₦6m / year",
        "furnishing": "Unfurnished",
        "listed": "2026-01-20",
        "featured": True,
    },
    {
        "id": "ikeja-bungalow",
        "title": "Five-bedroom bungalow in the GRA",
        "intent": "buy",
        "price": 350_000_000,
        "area_slug": "ikeja-gra",
        "street": "Ikeja GRA",
        "beds": 5,
        "baths": 5,
        "area_sqm": 460,
        "type": "Bungalow",
        "lat": 6.5785,
        "lng": 3.3518,
        "photos": ["ikeja.jpg", "kitchen.jpg", "flat.jpg"],
        "summary": "A renovated bungalow with a veranda deep enough to sit out rain, and a garden that is already mature. Mainland living, without the usual apology.",
        "year": 1978,
        "parking": 4,
        "title_doc": "Certificate of Occupancy",
        "service_charge": "None",
        "furnishing": "Unfurnished",
        "listed": "2026-03-18",
        "featured": False,
    },
    {
        "id": "oniru-court",
        "title": "Courtyard duplex in Oniru",
        "intent": "buy",
        "price": 610_000_000,
        "area_slug": "oniru",
        "street": "Oniru",
        "beds": 4,
        "baths": 5,
        "area_sqm": 340,
        "type": "Duplex",
        "lat": 6.4315,
        "lng": 3.4558,
        "photos": ["oniru.jpg", "suite.jpg", "kitchen.jpg"],
        "summary": "Four bedrooms around a small pool, timber screens instead of a fortress wall. Ten minutes to the Island, and the gate is not on a through-road.",
        "year": 2022,
        "parking": 3,
        "title_doc": "Governor's Consent",
        "service_charge": "₦3.1m / year",
        "furnishing": "Unfurnished",
        "listed": "2026-04-01",
        "featured": False,
    },
    {
        "id": "magodo-phase-2",
        "title": "Family duplex in Magodo Phase 2",
        "intent": "buy",
        "price": 280_000_000,
        "area_slug": "magodo",
        "street": "Magodo Phase 2",
        "beds": 4,
        "baths": 4,
        "area_sqm": 255,
        "type": "Duplex",
        "lat": 6.6148,
        "lng": 3.3784,
        "photos": ["magodo.jpg", "kitchen.jpg", "flat.jpg"],
        "summary": "Cream render, a proper compound, room for two cars inside the gate. The sort of house people actually move into, not a show unit.",
        "year": 2016,
        "parking": 3,
        "title_doc": "Governor's Consent",
        "service_charge": "Estate due, modest",
        "furnishing": "Unfurnished",
        "listed": "2026-02-28",
        "featured": False,
    },
    {
        "id": "ajah-duplex",
        "title": "New four-bedroom duplex in Ajah",
        "intent": "buy",
        "price": 165_000_000,
        "area_slug": "ajah",
        "street": "Ajah, east of Lekki",
        "beds": 4,
        "baths": 4,
        "area_sqm": 230,
        "type": "Duplex",
        "lat": 6.4695,
        "lng": 3.5784,
        "photos": ["ajah.jpg", "kitchen.jpg", "flat.jpg"],
        "summary": "Sand-coloured render in a quiet estate, a short drive to the Lekki express. Smaller money than the Island, with the title shown as Governor's Consent.",
        "year": 2025,
        "parking": 2,
        "title_doc": "Governor's Consent",
        "service_charge": "₦800k / year",
        "furnishing": "Unfurnished",
        "listed": "2026-04-16",
        "featured": False,
    },
    {
        "id": "vi-lagoon-flat",
        "title": "Three-bedroom flat above the lagoon",
        "intent": "rent",
        "price": 42_000_000,
        "area_slug": "victoria-island",
        "street": "Victoria Island",
        "beds": 3,
        "baths": 3,
        "area_sqm": 175,
        "type": "Apartment",
        "lat": 6.4288,
        "lng": 3.4216,
        "photos": ["vi.jpg", "flat.jpg", "kitchen.jpg"],
        "summary": "A high floor, lagoon in the glass, travertine underfoot. Rent is yearly, the Lagos way, and the service charge is separate from the rent.",
        "year": 2018,
        "parking": 2,
        "title_doc": "Lease",
        "service_charge": "₦4.2m / year",
        "furnishing": "Part furnished",
        "listed": "2026-03-22",
        "featured": False,
    },
    {
        "id": "yaba-two-bed",
        "title": "Two-bedroom near Hughes Avenue",
        "intent": "rent",
        "price": 4_500_000,
        "area_slug": "yaba",
        "street": "Hughes Avenue, Yaba",
        "beds": 2,
        "baths": 2,
        "area_sqm": 92,
        "type": "Apartment",
        "lat": 6.5094,
        "lng": 3.3708,
        "photos": ["yaba.jpg", "kitchen.jpg", "flat.jpg"],
        "summary": "Timber floors, trees in the window, close to campus and the railway. For rent by the year, and priced like Yaba rather than like the Island.",
        "year": 2012,
        "parking": 1,
        "title_doc": "Lease",
        "service_charge": "Included",
        "furnishing": "Unfurnished",
        "listed": "2026-04-11",
        "featured": False,
    },
    {
        "id": "osborne-flat",
        "title": "Three-bedroom on Osborne",
        "intent": "rent",
        "price": 22_000_000,
        "area_slug": "ikoyi",
        "street": "Osborne, Ikoyi",
        "beds": 3,
        "baths": 3,
        "area_sqm": 165,
        "type": "Apartment",
        "lat": 6.4491,
        "lng": 3.4284,
        "photos": ["flat.jpg", "kitchen.jpg", "suite.jpg"],
        "summary": "An older Ikoyi block opened up: olive walls, oak, morning light. Quieter than a new tower, and the rent shows it.",
        "year": 2004,
        "parking": 2,
        "title_doc": "Lease",
        "service_charge": "₦3.6m / year",
        "furnishing": "Unfurnished",
        "listed": "2026-03-09",
        "featured": False,
    },
    {
        "id": "lekki-suite",
        "title": "Furnished one-bedroom near Admiralty",
        "intent": "shortlet",
        "price": 240_000,
        "area_slug": "lekki-phase-1",
        "street": "Close to Admiralty, Lekki Phase 1",
        "beds": 1,
        "baths": 1,
        "area_sqm": 48,
        "type": "Apartment",
        "lat": 6.4412,
        "lng": 3.4815,
        "photos": ["suite.jpg", "vi.jpg", "kitchen.jpg"],
        "summary": "Linen, a cane chair, and a week in Lagos rather than a year. Power and cleaning are included in the nightly rate. No caution fee.",
        "year": 2020,
        "parking": 1,
        "title_doc": "Short stay",
        "service_charge": "Included",
        "furnishing": "Furnished",
        "listed": "2026-04-19",
        "featured": False,
    },
]


def area_name(slug):
    for area in AREAS:
        if area["slug"] == slug:
            return area["name"]
    return "Lagos"


def get_listing(home_id):
    return next((home for home in LISTINGS if home["id"] == home_id), None)


def format_naira(amount):
    return "₦{:,.0f}".format(amount)


def format_compact(amount):
    def trim(value):
        digits = f"{value:.0f}" if value >= 10 else f"{value:.1f}"
        return digits[:-2] if digits.endswith(".0") else digits

    if amount >= 1_000_000_000:
        return f"₦{trim(amount / 1_000_000_000)}b"
    if amount >= 1_000_000:
        return f"₦{trim(amount / 1_000_000)}m"
    if amount >= 1_000:
        return f"₦{trim(amount / 1_000)}k"
    return f"₦{amount:.0f}"


def price_label(home):
    amount = format_naira(home["price"])
    if home["intent"] == "rent":
        return f"{amount} / year"
    if home["intent"] == "shortlet":
        return f"{amount} / night"
    return amount


def price_compact(home):
    amount = format_compact(home["price"])
    if home["intent"] == "rent":
        return f"{amount}/yr"
    if home["intent"] == "shortlet":
        return f"{amount}/nt"
    return amount


def intent_label(intent):
    if intent == "buy":
        return "For sale"
    if intent == "rent":
        return "For rent"
    return "Short-let"


def intent_phrase(intent):
    if intent == "buy":
        return "for sale"
    if intent == "rent":
        return "for rent"
    return "for a short stay"


def similar_to(home):
    others = [
        item
        for item in LISTINGS
        if item["id"] != home["id"] and (item["area_slug"] == home["area_slug"] or item["intent"] == home["intent"])
    ]
    others.sort(key=lambda item: item["area_slug"] == home["area_slug"], reverse=True)
    return others[:3]


def areas_with_counts():
    rows = []
    for area in AREAS:
        homes = [home for home in LISTINGS if home["area_slug"] == area["slug"]]
        if not homes:
            continue
        rows.append({**area, "count": len(homes), "photo": homes[0]["photos"][0]})
    return rows


def _number(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return 0
    return number if number > 0 else 0


def parse_box(value):
    if not value or not isinstance(value, str):
        return ""
    parts = value.split(",")
    if len(parts) != 4:
        return ""
    try:
        south, west, north, east = (float(part) for part in parts)
    except ValueError:
        return ""
    if not (north > south and east > west):
        return ""
    if south < 5.5 or north > 7.5 or west < 2.5 or east > 4.8:
        return ""
    return ",".join(f"{part:.5f}" for part in (south, west, north, east))


def box_around(lat, lng, km=3.5):
    import math

    lat_pad = km / 111
    lng_pad = km / (111 * max(0.2, math.cos(math.radians(lat))))
    return ",".join(f"{part:.5f}" for part in (lat - lat_pad, lng - lng_pad, lat + lat_pad, lng + lng_pad))


def parse_search(args):
    intent = args.get("intent") if args.get("intent") in INTENTS else "buy"
    area = args.get("area") or "all"
    if area != "all" and area not in {item["slug"] for item in AREAS}:
        area = "all"
    sort = args.get("sort") if args.get("sort") in SORTS else "featured"
    home_type = args.get("type") or "all"
    if home_type != "all" and home_type not in HOME_TYPES:
        home_type = "all"
    beds = min(6, int(_number(args.get("beds"))))
    return {
        "intent": intent,
        "area": area,
        "beds": beds,
        "type": home_type,
        "min": int(_number(args.get("min"))),
        "max": int(_number(args.get("max"))),
        "sort": sort,
        "box": parse_box(args.get("box")),
    }


def filter_listings(homes, search):
    matched = []
    for home in homes:
        if home["intent"] != search["intent"]:
            continue
        if search["area"] != "all" and home["area_slug"] != search["area"]:
            continue
        if search["beds"] and home["beds"] < search["beds"]:
            continue
        if search["type"] != "all" and home["type"] != search["type"]:
            continue
        if search["min"] and home["price"] < search["min"]:
            continue
        if search["max"] and home["price"] > search["max"]:
            continue
        if search["box"]:
            south, west, north, east = (float(part) for part in search["box"].split(","))
            if home["lat"] < south or home["lat"] > north or home["lng"] < west or home["lng"] > east:
                continue
        matched.append(home)
    if search["sort"] == "price-asc":
        matched.sort(key=lambda home: home["price"])
    elif search["sort"] == "price-desc":
        matched.sort(key=lambda home: home["price"], reverse=True)
    else:
        matched.sort(key=lambda home: (home["featured"], home["listed"]), reverse=True)
    return matched


def results_headline(search, count):
    noun = "home" if count == 1 else "homes"
    phrase = intent_phrase(search["intent"])
    if search["box"]:
        return f"{count} {noun} {phrase} on this map"
    where = "Lagos" if search["area"] == "all" else area_name(search["area"])
    return f"{count} {noun} {phrase} in {where}"
