from datetime import date
from urllib.parse import urljoin
import re

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

SPORT_EVENTZ_URL = "https://www.sporteventz.com/en/sport-event.html"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
}


class SportEventzScraper:

    def __init__(self, headless=True):
        self.headless = headless

    def get_team_broadcasts(self, team, sport):
        today = date.today()

        rendered_html = self._get_rendered_schedule()

        events = self._parse_events(rendered_html)

        matching_events = [
            event
            for event in events
            if self._event_matches_team(event, team)
            and self._event_matches_sport(event, sport)
        ]

        return {
            "team": team,
            "sport": sport,
            "date": today.isoformat(),
            "match_found": bool(matching_events),
            "events": matching_events,
        }

    def _get_rendered_schedule(self):
        """
        Load the page with Playwright and inspect the actual rendered DOM.

        We deliberately return the rendered HTML instead of trying to
        construct the schedule from network responses.
        """

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=self.headless)

            page = browser.new_page(user_agent=HEADERS["User-Agent"])

            try:

                page.goto(
                    SPORT_EVENTZ_URL,
                    wait_until="domcontentloaded",
                    timeout=60000,
                )

                # Give the site's JavaScript time to populate the schedule.
                page.wait_for_timeout(15000)

                # --------------------------------------------------
                # Inspect the rendered page
                # --------------------------------------------------

                body_text = page.locator("body").inner_text()

                print("\n================ PAGE TEXT ================\n")
                print(body_text[:5000])

                # --------------------------------------------------
                # Inspect the actual DOM around the requested example
                # --------------------------------------------------

                match_text = "Arsenal vs. Chelsea"

                match_locator = page.get_by_text(
                    match_text,
                    exact=False,
                )

                print(
                    "\nArsenal elements found:",
                    match_locator.count(),
                )

                if match_locator.count() > 0:

                    element = match_locator.first

                    print("\n========== MATCH ELEMENT ==========\n")

                    print(element.evaluate("(el) => el.outerHTML"))

                    print("\n========== PARENT ==========\n")

                    print(element.evaluate("(el) => el.parentElement.outerHTML"))

                    print("\n========== GRANDPARENT ==========\n")

                    print(element.evaluate("""
                            (el) =>
                            el.parentElement
                               .parentElement
                               .outerHTML
                            """))

                    print("\n========== GREAT GRANDPARENT ==========\n")

                    print(element.evaluate("""
                            (el) =>
                            el.parentElement
                               .parentElement
                               .parentElement
                               .outerHTML
                            """))

                # Save the complete rendered HTML so we can inspect it.
                with open(
                    "sporteventz_rendered.html",
                    "w",
                    encoding="utf-8",
                ) as file:

                    file.write(page.content())

                page.screenshot(
                    path="sporteventz_debug.png",
                    full_page=True,
                )

                return page.content()

            finally:
                browser.close()

    def _parse_events(self, html):
        """
        Parse the rendered SportEventz HTML.

        The old parser assumed:
            tr.matchrow

        That selector is not present in the rendered page, so this
        implementation first looks for likely event containers and
        falls back to parsing the rendered text.
        """

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        # ----------------------------------------------------------
        # First attempt: identify containers from actual text.
        # ----------------------------------------------------------

        events = []

        # Find all elements containing a match-like string.
        candidates = soup.find_all(
            string=re.compile(
                r"\s(?:vs\.?|v\.?|@)\s",
                re.IGNORECASE,
            )
        )

        seen = set()

        for text_node in candidates:

            match_name = " ".join(text_node.strip().split())

            if not self._looks_like_match(match_name):
                continue

            # Walk upward through the DOM looking for an event block.
            container = text_node.parent

            for _ in range(6):

                if container is None:
                    break

                container_text = " ".join(
                    container.get_text(
                        " ",
                        strip=True,
                    ).split()
                )

                # An event container normally contains:
                # match + date/time + at least one channel.
                if self._looks_like_match(container_text) and self._contains_datetime(
                    container_text
                ):
                    key = container_text[:500]

                    if key not in seen:

                        event = self._parse_event_container(container)

                        if event:
                            events.append(event)
                            seen.add(key)

                        break

                container = container.parent

        # ----------------------------------------------------------
        # Fallback: parse the visible body text.
        # ----------------------------------------------------------

        if not events:

            print("DOM event-container parsing found no events.")

            print("Falling back to rendered text parser.")

            body = soup.get_text(
                "\n",
                strip=True,
            )

            events = self._parse_text_schedule(body)

        print(
            "Events parsed:",
            len(events),
        )

        return events

    def _parse_event_container(self, container):

        lines = [
            " ".join(line.split())
            for line in container.get_text(
                "\n",
                strip=True,
            ).splitlines()
            if line.strip()
        ]

        match_index = None

        for index, line in enumerate(lines):

            if self._looks_like_match(line):
                match_index = index
                break

        if match_index is None:
            return None

        match_name = lines[match_index]

        event_time = None

        for line in lines[match_index + 1 :]:

            if self._looks_like_datetime(line):
                event_time = line
                break

        broadcasts = []

        for link in container.select("a"):

            channel_name = " ".join(
                link.get_text(
                    " ",
                    strip=True,
                ).split()
            )

            if not channel_name:
                continue

            if self._looks_like_broadcast(channel_name):

                href = link.get("href")

                broadcasts.append(
                    self._build_broadcast(
                        channel_name,
                        link.get("title"),
                        href,
                    )
                )

        # If links did not expose the channels, use text lines.
        if not broadcasts and event_time:

            time_index = lines.index(event_time)

            for line in lines[time_index + 1 :]:

                if self._looks_like_broadcast(line):

                    broadcasts.append(
                        self._build_broadcast(
                            line,
                            None,
                            None,
                        )
                    )

        home_team, away_team = self._extract_participants(match_name)

        competition = self._find_competition(lines)

        return {
            "competition": competition,
            "match": match_name,
            "home_team": home_team,
            "away_team": away_team,
            "time": event_time,
            "broadcasts": self._deduplicate_broadcasts(broadcasts),
            "source": "SportEventz",
        }

    def _parse_text_schedule(self, text):

        lines = [" ".join(line.split()) for line in text.splitlines() if line.strip()]

        events = []

        i = 0

        while i < len(lines):

            if not self._looks_like_match(lines[i]):
                i += 1
                continue

            match_name = lines[i]

            event_time = None

            if i + 1 < len(lines) and self._looks_like_datetime(lines[i + 1]):
                event_time = lines[i + 1]

            if event_time is None:
                i += 1
                continue

            competition = None

            if i > 0:
                competition = lines[i - 1]

            broadcasts = []

            j = i + 2

            while j < len(lines):

                current = lines[j]

                if self._looks_like_match(current):
                    break

                if self._looks_like_competition(current):
                    break

                if self._looks_like_broadcast(current):
                    broadcasts.append(
                        self._build_broadcast(
                            current,
                            None,
                            None,
                        )
                    )

                j += 1

            home_team, away_team = self._extract_participants(match_name)

            events.append(
                {
                    "competition": competition,
                    "match": match_name,
                    "home_team": home_team,
                    "away_team": away_team,
                    "time": event_time,
                    "broadcasts": self._deduplicate_broadcasts(broadcasts),
                    "source": "SportEventz",
                }
            )

            i = j

        return events

    @staticmethod
    def _looks_like_match(text):

        return bool(
            re.search(
                r"\s(?:vs\.?|v\.?|@)\s",
                text,
                re.IGNORECASE,
            )
        )

    @staticmethod
    def _looks_like_datetime(text):

        return bool(
            re.search(
                r"\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),"
                r"\s+\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\b",
                text,
                re.IGNORECASE,
            )
        )

    def _contains_datetime(self, text):

        return self._looks_like_datetime(text)

    @staticmethod
    def _looks_like_competition(text):

        competition_keywords = [
            "premier league",
            "champions league",
            "europa league",
            "conference league",
            "bundesliga",
            "la liga",
            "serie a",
            "ligue 1",
            "ekstraklasa",
            "primeira liga",
            "super lig",
            "superliga",
            "nba",
            "wnba",
            "euroleague",
            "ncaa",
            "mlb",
            "nfl",
            "nhl",
            "atp",
            "wta",
            "grand slam",
        ]

        lower = text.lower()

        return any(keyword in lower for keyword in competition_keywords)

    @staticmethod
    def _looks_like_broadcast(text):

        broadcast_keywords = [
            "sport",
            "dazn",
            "sky",
            "arena",
            "canal",
            "espn",
            "bbc",
            "tnt",
            "bein",
            "eurosport",
            "super",
            "digi",
            "nova",
            "ziggo",
            "spiler",
            "eleven",
            "polsat",
            "tvp",
            "max sport",
            "match",
            "nbc",
            "cbs",
            "abc",
        ]

        lower = text.lower()

        return any(keyword in lower for keyword in broadcast_keywords)

    def _find_competition(self, lines):

        for line in lines:

            if self._looks_like_competition(line):
                return line

        return None

    def _build_broadcast(
        self,
        channel_name,
        title,
        href,
    ):

        display_name = title.strip() if title else channel_name

        channel_url = None

        if href:
            channel_url = urljoin(
                SPORT_EVENTZ_URL,
                href,
            )

        return {
            "channel": channel_name,
            "display_name": display_name,
            "broadcaster": self._extract_broadcaster(display_name),
            "channel_number": self._extract_channel_number(display_name),
            "country": self._extract_country(display_name),
            "source": "SportEventz",
            "url": channel_url,
        }

    def _event_matches_team(self, event, team):

        search_team = self._normalise_text(team)

        home_team = self._normalise_text(event.get("home_team") or "")

        away_team = self._normalise_text(event.get("away_team") or "")

        match_name = self._normalise_text(event.get("match") or "")

        return (
            search_team == home_team
            or search_team == away_team
            or search_team in home_team
            or search_team in away_team
            or search_team in match_name
        )

    def _event_matches_sport(self, event, sport):

        sport = self._normalise_text(sport)

        competition = self._normalise_text(event.get("competition") or "")

        football_keywords = [
            "premier league",
            "champions league",
            "europa league",
            "conference league",
            "bundesliga",
            "la liga",
            "serie a",
            "ligue 1",
            "ekstraklasa",
            "primeira liga",
            "super lig",
            "superliga",
            "football",
        ]

        basketball_keywords = [
            "nba",
            "wnba",
            "euroleague",
            "basketball",
        ]

        tennis_keywords = [
            "atp",
            "wta",
            "tennis",
            "grand slam",
        ]

        keyword_map = {
            "football": football_keywords,
            "soccer": football_keywords,
            "basketball": basketball_keywords,
            "tennis": tennis_keywords,
        }

        keywords = keyword_map.get(
            sport,
            [sport],
        )

        return any(keyword in competition for keyword in keywords)

    @staticmethod
    def _extract_participants(match_name):

        separators = [
            " vs. ",
            " vs ",
            " v. ",
            " v ",
            " - ",
            " @ ",
        ]

        for separator in separators:

            if separator in match_name:

                parts = match_name.split(
                    separator,
                    1,
                )

                if len(parts) == 2:

                    return (
                        parts[0].strip(),
                        parts[1].strip(),
                    )

        return (
            match_name.strip(),
            None,
        )

    @staticmethod
    def _normalise_text(value):

        return " ".join(value.lower().strip().split())

    @staticmethod
    def _extract_broadcaster(channel):

        channel_lower = channel.lower()

        broadcasters = [
            "dazn",
            "espn",
            "sky sports",
            "sky sport",
            "bbc",
            "tnt sports",
            "canal+",
            "canal plus",
            "canal sport",
            "bein sports",
            "eurosport",
            "fox sports",
            "nbc",
            "cbs",
            "abc",
            "paramount+",
            "supersport",
            "digi sport",
            "digisport",
            "nova sport",
            "sportklub",
            "ziggo sport",
            "tvp sport",
            "arena sport",
            "max sport",
            "spiler",
            "polsat sport",
            "eleven sports",
            "m4 sport",
        ]

        for broadcaster in broadcasters:

            if broadcaster in channel_lower:
                return broadcaster

        return None

    @staticmethod
    def _extract_channel_number(channel):

        patterns = [
            r"\bchannel\s*(\d+)\b",
            r"\bch\s*(\d+)\b",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                channel,
                re.IGNORECASE,
            )

            if match:
                return int(match.group(1))

        return None

    @staticmethod
    def _extract_country(channel):

        countries = [
            "Portugal",
            "Spain",
            "France",
            "Germany",
            "Italy",
            "England",
            "Scotland",
            "Wales",
            "Ireland",
            "Netherlands",
            "Belgium",
            "Croatia",
            "Serbia",
            "Romania",
            "Czechia",
            "Czech",
            "Hungary",
            "Albania",
            "Bulgaria",
            "Poland",
            "Austria",
            "Switzerland",
            "Greece",
            "Turkey",
            "Turkiye",
            "USA",
            "Canada",
            "Australia",
            "New Zealand",
            "India",
            "South Africa",
            "Brazil",
            "Argentina",
            "BiH",
            "Slovakia",
        ]

        channel_lower = channel.lower()

        for country in countries:

            if country.lower() in channel_lower:
                return country

        return None

    @staticmethod
    def _deduplicate_broadcasts(broadcasts):

        unique = {}

        for broadcast in broadcasts:

            key = (
                broadcast.get(
                    "channel",
                    "",
                ).lower(),
                broadcast.get("country"),
            )

            if key not in unique:
                unique[key] = broadcast

        return list(unique.values())


def get_team_broadcasts(team, sport):

    scraper = SportEventzScraper()

    return scraper.get_team_broadcasts(
        team,
        sport,
    )


if __name__ == "__main__":

    team = input("Enter team name: ").strip()

    sport = input("Enter sport: ").strip()

    result = get_team_broadcasts(
        team,
        sport,
    )

    print("\nRESULT:\n")
    print(result)
