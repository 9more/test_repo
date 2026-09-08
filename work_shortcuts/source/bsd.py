import os
from datetime import datetime, timezone
from difflib import SequenceMatcher

import requests
from dotenv import load_dotenv

from country import COUNTRY_CODES

load_dotenv()

BASE_URL = "https://sports.bzzoiro.com/api/v2"


def get_headers():
    return {"Authorization": f"Token {os.environ['BSD_API_KEY']}"}


def get_today():
    """Return today's UTC date as YYYY-MM-DD."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def team_name_matches(user_input, api_name):
    """Check whether a user-supplied team name reasonably matches an API name."""
    if not api_name:
        return False

    user_input = user_input.lower().strip()
    api_name = api_name.lower().strip()

    if user_input == api_name:
        return True

    if user_input in api_name or api_name in user_input:
        return True

    score = SequenceMatcher(None, user_input, api_name).ratio()

    return score >= 0.6


def get_team_events(team_name):
    """Retrieve today's events involving a team."""
    today = get_today()

    response = requests.get(
        f"{BASE_URL}/events/",
        headers=get_headers(),
        params={
            "team_name": team_name,
            "date_from": today,
            "date_to": today,
            "limit": 200,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json().get("results", [])


def find_event(team1, team2):
    """
    Find today's event involving both supplied teams.
    """

    events = get_team_events(team1)

    for event in events:
        home_team = event.get("home_team", "")
        away_team = event.get("away_team", "")

        team1_matches = team_name_matches(team1, home_team) or team_name_matches(
            team1, away_team
        )

        team2_matches = team_name_matches(team2, home_team) or team_name_matches(
            team2, away_team
        )

        if team1_matches and team2_matches:
            return event

    return None


def get_broadcasts(event_id):
    """Retrieve broadcast records belonging to a specific event."""

    response = requests.get(
        f"{BASE_URL}/events/{event_id}/broadcasts/",
        headers=get_headers(),
        params={
            "limit": 200,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json().get("results", [])


def clean_broadcasts(broadcasts):
    """
    Reduce raw BSD broadcast records to the fields required
    by the application and remove duplicates.
    """

    cleaned = []
    seen = set()

    for broadcast in broadcasts:
        country_code = broadcast.get("country_code")
        channel = broadcast.get("channel_name")

        if not country_code or not channel:
            continue

        country = COUNTRY_CODES.get(country_code, country_code)

        key = (country, channel)

        if key in seen:
            continue

        seen.add(key)

        cleaned.append(
            {
                "country": country,
                "channel": channel,
            }
        )

    return sorted(cleaned, key=lambda item: (item["country"], item["channel"]))


def get_event_broadcasts(team1, team2):
    """
    Find today's match between two teams and return
    the event's global broadcasters.
    """

    event = find_event(team1, team2)

    if not event:
        return {
            "team1": team1,
            "team2": team2,
            "league": None,
            "date": get_today(),
            "kickoff": None,
            "event_id": None,
            "match_found": False,
            "broadcasters": [],
        }

    event_id = event["id"]

    broadcasts = get_broadcasts(event_id)

    cleaned_broadcasts = clean_broadcasts(broadcasts)

    event_date = event.get("event_date")

    date = None
    kickoff = None

    if event_date:
        parsed_date = datetime.fromisoformat(event_date.replace("Z", "+00:00"))

        date = parsed_date.strftime("%-d %B %Y")
        kickoff = parsed_date.strftime("%H:%M UTC")

    league = None

    if broadcasts:
        league = broadcasts[0].get("league_name")

    return {
        "team1": event.get("home_team"),
        "team2": event.get("away_team"),
        "league": league,
        "date": date,
        "kickoff": kickoff,
        "event_id": event_id,
        "match_found": True,
        "broadcasters": cleaned_broadcasts,
    }
