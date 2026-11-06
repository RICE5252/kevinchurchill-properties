"""KevinChurchill Properties. Run with: python app.py"""

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from flask import Flask, abort, redirect, render_template, request, url_for

from listings import (
    AREAS,
    HOME_TYPES,
    LISTINGS,
    PRICE_STOPS,
    area_name,
    areas_with_counts,
    box_around,
    filter_listings,
    format_compact,
    format_naira,
    get_listing,
    intent_label,
    parse_search,
    price_compact,
    price_label,
    results_headline,
    similar_to,
)

ROOT = Path(__file__).resolve().parent
ENQUIRIES = ROOT / "enquiries.json"

CONTACT = {
    "phone": "+234 809 442 1180",
    "tel": "+2348094421180",
    "whatsapp": "2348094421180",
    "email": "hello@estatesite.example",
    "hours": "Monday to Saturday, 9:00 to 18:00",
}

app = Flask(__name__)
app.secret_key = "estate-site-sample"


def whatsapp_href(about=None):
    text = (
        f"Hello, I'm asking about {about} on KevinChurchill Properties."
        if about
        else "Hello, I'm asking about a home on KevinChurchill Properties."
    )
    return f"https://wa.me/{CONTACT['whatsapp']}?text={quote(text)}"


def email_href(about=None):
    subject = about or "A home on KevinChurchill Properties"
    return f"mailto:{CONTACT['email']}?subject={quote(subject)}"


def geocode(query):
    url = "https://nominatim.openstreetmap.org/search?" + urlencode(
        {
            "q": f"{query}, Lagos",
            "format": "jsonv2",
            "countrycodes": "ng",
            "limit": 1,
            "viewbox": "3.1,6.72,3.7,6.35",
        }
    )
    req = Request(url, headers={"User-Agent": "EstateSite/1.0 (Lagos home search sample)", "Accept": "application/json"})
    try:
        with urlopen(req, timeout=8) as response:
            rows = json.loads(response.read().decode())
    except (URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None
    if not rows:
        return None
    try:
        lat = float(rows[0]["lat"])
        lng = float(rows[0]["lon"])
    except (KeyError, TypeError, ValueError):
        return None
    if not (6.35 <= lat <= 6.72 and 3.1 <= lng <= 3.7):
        return None
    name = rows[0].get("name") or query
    return {"name": name, "lat": lat, "lng": lng}


def save_enquiry(entry):
    rows = []
    if ENQUIRIES.exists():
        try:
            rows = json.loads(ENQUIRIES.read_text())
        except json.JSONDecodeError:
            rows = []
    rows.append(entry)
    ENQUIRIES.write_text(json.dumps(rows, indent=2))


def card_payload(home):
    return {
        "id": home["id"],
        "title": home["title"],
        "intent": intent_label(home["intent"]),
        "price": price_label(home),
        "meta": f"{home['beds']} bd · {home['baths']} ba · {home['area_sqm']} m² · {home['type']}",
        "street": home["street"],
        "photo": url_for("static", filename=f"photos/{home['photos'][0]}"),
        "url": url_for("listing_page", home_id=home["id"]),
    }


def pin_payload(home):
    payload = card_payload(home)
    payload.update(
        {
            "lat": home["lat"],
            "lng": home["lng"],
            "pill": price_compact(home),
            "type": home["type"],
            "beds": home["beds"],
            "baths": home["baths"],
        }
    )
    return payload


@app.context_processor
def inject():
    return {
        "contact": CONTACT,
        "whatsapp_href": whatsapp_href,
        "email_href": email_href,
        "price_label": price_label,
        "intent_label": intent_label,
        "area_name": area_name,
        "format_naira": format_naira,
        "format_compact": format_compact,
        "areas_all": AREAS,
    }


@app.get("/")
def home_page():
    featured = [home for home in LISTINGS if home["featured"]]
    places = len({home["area_slug"] for home in LISTINGS})
    return render_template(
        "home.html",
        featured=featured,
        areas=areas_with_counts(),
        areas_all=AREAS,
        listing_count=len(LISTINGS),
        place_count=places,
    )


@app.get("/search")
def search_page():
    search = parse_search(request.args)
    place = (request.args.get("place") or "").strip()[:80]
    place_note = ""
    if place and request.args.get("find"):
        hit = geocode(place)
        if hit:
            params = request.args.to_dict()
            params.pop("find", None)
            params["place"] = hit["name"]
            params["area"] = "all"
            params["box"] = box_around(hit["lat"], hit["lng"])
            return redirect(url_for("search_page", **params))
        place_note = "No place matched in Lagos."
    results = filter_listings(LISTINGS, search)
    dirty = any(
        (
            search["area"] != "all",
            search["beds"],
            search["type"] != "all",
            search["min"],
            search["max"],
            search["box"],
        )
    )
    return render_template(
        "search.html",
        q=search,
        place=place,
        place_note=place_note,
        results=results,
        pins=[pin_payload(home) for home in results],
        headline=results_headline(search, len(results)),
        areas=AREAS,
        types=HOME_TYPES,
        stops=PRICE_STOPS[search["intent"]],
        dirty=dirty,
    )


@app.route("/homes/<home_id>", methods=["GET", "POST"])
def listing_page(home_id):
    home = get_listing(home_id)
    if home is None:
        abort(404)
    sent = False
    error = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        note = request.form.get("note", "").strip()
        if not name or not phone:
            error = "Name and phone are required."
        else:
            save_enquiry(
                {
                    "listing_id": home["id"],
                    "name": name,
                    "phone": phone,
                    "note": note,
                    "at": datetime.now(timezone.utc).isoformat(),
                }
            )
            sent = True
    return render_template(
        "listing.html",
        home=home,
        similar=similar_to(home),
        sent=sent,
        error=error,
        pin=pin_payload(home),
    )


@app.get("/saved")
def saved_page():
    return render_template("saved.html", catalog=[card_payload(home) for home in LISTINGS])


@app.get("/contact")
def contact_page():
    return render_template("contact.html")


@app.errorhandler(404)
def missing(_error):
    return render_template("missing.html"), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
