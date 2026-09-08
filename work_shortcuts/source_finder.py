from datetime import datetime
from urllib.parse import urljoin
import re

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.livesoccertv.com"
SCHEDULE_URL = f"{BASE_URL}/schedules"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0 Safari/537.36"
    )
}


def get_today_date():
    """Return today's date as YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")


def request_page(url):
    """Download a page from Live Soccer TV."""
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    return response.text


def get_schedule_page(target_date=None):
    """Download a date-specific Live Soccer TV schedule."""
    target_date = target_date or get_today_date()
    url = f"{SCHEDULE_URL}/{target_date}/"
    return request_page(url)


def clean_text(value):
    """Normalize whitespace."""
    return re.sub(r"\s+", " ", value or "").strip()


def parse_schedule_date(date_text, target_date):
    """
    Convert text such as 'Sep 6' into YYYY-MM-DD.

    Returns None if the text cannot be parsed.
    """
    if not date_text:
        return None

    date_text = clean_text(date_text)

    try:
        year = datetime.strptime(target_date, "%Y-%m-%d").year
        parsed = datetime.strptime(f"{date_text} {year}", "%b %d %Y")
        return parsed.strftime("%Y-%m-%d")
    except ValueError:
        return None


def find_team_matches(html, team, target_date):
    """
    Find matches for the requested team on target_date.

    The important difference from the previous version is that
    the date is checked before a match is accepted.
    """
    soup = BeautifulSoup(html, "html.parser")
    team = clean_text(team).lower()

    matches = []
    seen = set()

    for link in soup.find_all("a", href=True):
        href = link.get("href", "")

        if not href.startswith("/match/"):
            continue

        fixture_text = clean_text(link.get_text(" ", strip=True))

        if not fixture_text:
            continue

        if team not in fixture_text.lower():
            continue

        # The schedule puts the date/time and match link in the
        # same small container. Check the nearest parent first.
        container = link.parent

        if container is None:
            continue

        date_text = None
        time_text = None

        date_span = container.find("span", class_="ts")

        if date_span:
            date_text = clean_text(date_span.get_text(" ", strip=True))

        # The displayed time is commonly the text before the match
        # link. We use a regex as a fallback.
        container_text = clean_text(container.get_text(" ", strip=True))

        time_match = re.search(r"\b\d{1,2}:\d{2}\b", container_text)

        if time_match:
            time_text = time_match.group(0)

        event_date = parse_schedule_date(date_text, target_date)

        # If the row explicitly contains another date, reject it.
        if event_date and event_date != target_date:
            continue

        # If there is no explicit date in this row, retain it for now.
        # The match page will be used as the final date validation.
        match_url = urljoin(BASE_URL, href.split("#")[0])

        if match_url in seen:
            continue

        seen.add(match_url)

        parts = href.strip("/").split("/")

        matches.append(
            {
                "fixture": fixture_text,
                "match_url": match_url,
                "match_slug": parts[1] if len(parts) > 1 else None,
                "match_id": parts[2] if len(parts) > 2 else None,
                "date": event_date,
                "scheduled_time": time_text,
            }
        )

    return matches


def extract_match_teams(soup):
    """
    Extract the teams from the match page heading.

    Example:
        Arsenal vs Chelsea stream and TV schedule

    Returns:
        ('Arsenal', 'Chelsea')
    """
    heading = soup.find("h1")

    if not heading:
        return None, None

    text = clean_text(heading.get_text(" ", strip=True))

    match = re.search(
        r"^(.+?)\s+vs\s+(.+?)(?:\s+(?:stream|TV|schedule|Live|Channel)|$)",
        text,
        flags=re.IGNORECASE,
    )

    if not match:
        return None, None

    return (clean_text(match.group(1)), clean_text(match.group(2)))


def extract_match_date_time(soup):
    """
    Extract the scheduled date/time from the match page.

    Example page text:
        Sep 6, 2026 11:30
    """
    page_text = clean_text(soup.get_text(" ", strip=True))

    pattern = re.compile(
        r"\b("
        r"Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
        r")\s+(\d{1,2}),\s+(\d{4})\s+"
        r"(\d{1,2}:\d{2})\b"
    )

    match = pattern.search(page_text)

    if not match:
        return None, None

    month, day, year, time = match.groups()

    try:
        dt = datetime.strptime(f"{month} {day} {year} {time}", "%b %d %Y %H:%M")

        return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M")
    except ValueError:
        return None, None


def extract_competition(soup):
    """
    Extract the competition from the match page.

    The competition normally appears as a link immediately before
    the match title.
    """
    heading = soup.find("h1")

    if not heading:
        return None

    # Look for a nearby link whose text resembles a competition.
    for parent in heading.parents:
        links = parent.find_all("a", href=True)

        for link in links:
            text = clean_text(link.get_text(" ", strip=True))

            if text in {
                "Premier League",
                "UEFA Champions League",
                "UEFA Europa League",
                "UEFA Conference League",
                "FA Cup",
                "Carabao Cup",
                "La Liga",
                "Serie A",
                "Bundesliga",
                "Ligue 1",
            }:
                return text

        # Don't search indefinitely.
        if parent.name == "body":
            break

    return None


def extract_channel_number(channel_text):
    """
    Extract a channel number only when it is explicitly present.

    Examples that could be detected:
        Sky Sports Main Event (401)
        Channel 401
        Ch 401

    Otherwise returns None.

    We deliberately do NOT invent channel numbers because they
    can vary by provider, country and platform.
    """
    text = clean_text(channel_text)

    patterns = [
        r"\bchannel\s+(\d{1,5})\b",
        r"\bch\.?\s*(\d{1,5})\b",
        r"\((\d{1,5})\)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)

        if match:
            return match.group(1)

    return None


def parse_broadcast_row(row):
    """
    Parse one international-coverage row.

    Live Soccer TV presents rows approximately as:

        Country | Channel 1 | Channel 2 | Channel 3

    We use the first text segment as the country and the linked
    channel names as the broadcast services.
    """
    text = clean_text(row.get_text(" ", strip=True))

    if not text:
        return []

    links = row.find_all("a", href=True)

    if not links:
        return []

    # Country is generally the text immediately before the first
    # channel link.
    first_link = links[0]

    country = None

    for node in first_link.previous_siblings:
        sibling_text = clean_text(
            node.get_text(" ", strip=True) if hasattr(node, "get_text") else str(node)
        )

        if sibling_text:
            country = sibling_text.strip(" |:-")
            break

    if not country:
        # Fallback: derive country from the row text before the first
        # channel name.
        first_channel = clean_text(first_link.get_text(" ", strip=True))

        if first_channel and first_channel in text:
            country = text.split(first_channel, 1)[0].strip(" |:-")

    broadcasts = []

    for link in links:
        channel = clean_text(link.get_text(" ", strip=True))

        if not channel:
            continue

        broadcasts.append(
            {
                "channel": channel,
                "channel_number": extract_channel_number(channel),
                "country": country,
                "source": "Live Soccer TV",
            }
        )

    return broadcasts


def extract_international_broadcasts(soup):
    """
    Extract global/international broadcast listings.

    The match page contains an 'International Coverage' section.
    We locate that heading and inspect the content until the next
    major section.
    """
    broadcasts = []

    heading = None

    for tag in soup.find_all(["h2", "h3"]):
        text = clean_text(tag.get_text(" ", strip=True)).lower()

        if "international coverage" in text:
            heading = tag
            break

    if not heading:
        return broadcasts

    # Find the nearest useful container holding the coverage rows.
    container = heading.parent

    # Walk upward a little if the parent only contains the heading.
    for _ in range(4):
        if container is None:
            break

        candidate_links = container.find_all("a", href=True)

        if len(candidate_links) >= 2:
            break

        container = container.parent

    if container is None:
        return broadcasts

    # Coverage is normally represented by rows such as <div> or <tr>.
    # We inspect elements whose text contains links.
    possible_rows = container.find_all(["tr", "div", "li"])

    for row in possible_rows:
        row_text = clean_text(row.get_text(" ", strip=True))

        if not row_text:
            continue

        # Skip nested containers that are too large.
        links = row.find_all("a", href=True)

        if not links or len(links) > 20:
            continue

        # International rows generally have at least one country name
        # plus one or more channel links.
        row_broadcasts = parse_broadcast_row(row)

        for item in row_broadcasts:
            broadcasts.append(item)

    # Remove duplicates.
    unique = []
    seen = set()

    for item in broadcasts:
        key = (item["country"], item["channel"], item["channel_number"])

        if key not in seen:
            seen.add(key)
            unique.append(item)

    return unique


def extract_live_broadcasts(soup):
    """
    Extract the main 'Live Broadcasts' section.

    These entries are useful because they identify the local TV/
    streaming services for the match.
    """
    broadcasts = []

    heading = None

    for tag in soup.find_all(["h2", "h3"]):
        text = clean_text(tag.get_text(" ", strip=True)).lower()

        if "live broadcasts" in text:
            heading = tag
            break

    if not heading:
        return broadcasts

    # Start from the heading and inspect the following elements.
    for element in heading.find_all_next(["a", "p", "div", "li"]):
        text = clean_text(element.get_text(" ", strip=True))

        if not text:
            continue

        # Stop when the next major section begins.
        if element.name in {"h2", "h3"} and element is not heading:
            break

        links = element.find_all("a", href=True)

        for link in links:
            channel = clean_text(link.get_text(" ", strip=True))

            if not channel:
                continue

            # Ignore navigation links.
            if channel.lower() in {
                "arsenal",
                "chelsea",
                "table",
                "h2h",
                "international tv",
            }:
                continue

            broadcasts.append(
                {
                    "channel": channel,
                    "channel_number": extract_channel_number(channel),
                    "country": None,
                    "source": "Live Soccer TV",
                }
            )

    unique = []
    seen = set()

    for item in broadcasts:
        key = (item["country"], item["channel"], item["channel_number"])

        if key not in seen:
            seen.add(key)
            unique.append(item)

    return unique


def get_match_details(match):
    """Download and parse one individual match page."""
    html = request_page(match["match_url"])
    soup = BeautifulSoup(html, "html.parser")

    home_team, away_team = extract_match_teams(soup)
    event_date, event_time = extract_match_date_time(soup)

    broadcasts = extract_international_broadcasts(soup)

    # Add the main/local broadcast section too.
    local_broadcasts = extract_live_broadcasts(soup)

    all_broadcasts = broadcasts + local_broadcasts

    # Deduplicate.
    unique_broadcasts = []
    seen = set()

    for item in all_broadcasts:
        key = (item["country"], item["channel"], item["channel_number"])

        if key not in seen:
            seen.add(key)
            unique_broadcasts.append(item)

    return {
        "home_team": home_team,
        "away_team": away_team,
        "competition": extract_competition(soup),
        "scheduled_date": event_date,
        "scheduled_time": event_time or match.get("scheduled_time"),
        "broadcasts": unique_broadcasts,
        "match_url": match["match_url"],
        "source": "Live Soccer TV",
    }


def get_livesoccertv_events(team):
    """
    Public Live Soccer TV function.

    Only `team` is required. Today's date is determined internally.
    """
    target_date = get_today_date()
    schedule_html = get_schedule_page(target_date)

    matches = find_team_matches(schedule_html, team, target_date)

    events = []

    for match in matches:
        details = get_match_details(match)

        # Final date validation using the individual match page.
        if details["scheduled_date"] != target_date:
            continue

        events.append(details)

    return {
        "team": team,
        "date": target_date,
        "match_found": bool(events),
        "events": events,
    }


if __name__ == "__main__":
    team = input("Enter team: ").strip()

    if not team:
        raise SystemExit("Team name cannot be empty.")

    result = get_livesoccertv_events(team)

    print("\nResult:")
    print(result)

    print("\nEvents found:", len(result["events"]))

    for event in result["events"]:
        print("\n" + "=" * 80)
        print(f'{event["home_team"]} vs {event["away_team"]}')
        print("Competition:", event["competition"])
        print("Date:", event["scheduled_date"])
        print("Time:", event["scheduled_time"])
        print("Match URL:", event["match_url"])

        print("\nBroadcasts:")

        for broadcast in event["broadcasts"]:
            print(
                f'  - {broadcast["country"] or "Unknown region"} | '
                f'{broadcast["channel"]} | '
                f'Channel number: {broadcast["channel_number"]}'
            )
