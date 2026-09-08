from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.livesoccertv.com"
SCHEDULE_URL = BASE_URL + "/schedules"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0 Safari/537.36"
    )
}


def get_today_date():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def get_schedule_page():
    """Download today's Live Soccer TV schedule page."""
    target_date = get_today_date()
    url = f"{SCHEDULE_URL}/{target_date}/"

    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    return response.text


def get_match_page(match_url):
    """Download an individual Live Soccer TV match page."""
    response = requests.get(match_url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    return response.text


def find_team_matches(html, team):
    """
    Find links in the daily schedule containing the requested team.

    Returns a list of dictionaries containing the displayed fixture,
    match URL and match ID.
    """
    soup = BeautifulSoup(html, "html.parser")

    team = team.strip().lower()
    matches = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        # We only want Live Soccer TV match links.
        if not href.startswith("/match/"):
            continue

        fixture = link.get_text(" ", strip=True)

        if not fixture:
            continue

        # Match the requested team against either side of the fixture.
        fixture_lower = fixture.lower()

        if team not in fixture_lower:
            continue

        match_url = urljoin(BASE_URL, href)

        # Remove the fragment (#...) because it isn't needed
        # to request the match page.
        match_url = match_url.split("#")[0]

        parts = href.split("/")

        match_slug = parts[2] if len(parts) > 2 else None
        match_id = parts[3] if len(parts) > 3 else None

        matches.append(
            {
                "fixture": fixture,
                "match_url": match_url,
                "match_slug": match_slug,
                "match_id": match_id,
            }
        )

    # Remove duplicate match links.
    unique_matches = []
    seen = set()

    for match in matches:
        key = match["match_url"]

        if key not in seen:
            seen.add(key)
            unique_matches.append(match)

    return unique_matches


def inspect_match_page(match_url):
    """
    Download a match page and save it locally for inspection.

    This is intentionally an inspection function for now.
    We will add the broadcaster/channel parser once we confirm
    the exact HTML structure of the match page.
    """
    html = get_match_page(match_url)

    with open("match.html", "w", encoding="utf-8") as file:
        file.write(html)

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(" ", strip=True) if soup.title else None

    return {"title": title, "html_length": len(html), "file": "match.html"}


def get_livesoccertv_events(team):
    """
    Find today's scheduled matches for a team.

    Broadcaster extraction will be added after we inspect
    the individual match-page HTML.
    """
    target_date = get_today_date()
    html = get_schedule_page()

    matches = find_team_matches(html, team)

    events = []

    for match in matches:
        events.append(
            {
                "home_team": None,
                "away_team": None,
                "competition": None,
                "scheduled_time": None,
                "broadcasts": [],
                "match_url": match["match_url"],
                "fixture": match["fixture"],
                "source": "Live Soccer TV",
            }
        )

    return {
        "team": team,
        "date": target_date,
        "match_found": bool(events),
        "events": events,
    }


if __name__ == "__main__":
    team = input("Enter team: ").strip()

    result = get_livesoccertv_events(team)

    print("\nResult:")
    print(result)

    if result["events"]:
        print("\nInspecting first match page...")

        inspection = inspect_match_page(result["events"][0]["match_url"])

        print("Title:", inspection["title"])
        print("HTML length:", inspection["html_length"])
        print("Saved to:", inspection["file"])
    else:
        print("\nNo match found for this team today.")
