import json
from bs4 import BeautifulSoup
import requests


def get_channels_from_match_page(match_url):
    """Scrapes a specific LiveSportsOnTV match page and dynamically outputs

    a clean, de-duplicated dictionary of broadcasters and channels.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    broadcaster_channel_map = {}

    try:
        response = requests.get(match_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"❌ Failed to load page. Status code: {response.status_code}")
            return broadcaster_channel_map

        soup = BeautifulSoup(response.text, "html.parser")

        # 1. Locate the master "TV / Streaming" container section on the page
        # We search broadly for the text heading block to ensure we grab its parent context
        tv_section = None
        for heading in soup.find_all(["h2", "h3", "div"]):
            if "TV / Streaming" in heading.get_text():
                # Get the container holding all the channel grids below this header
                tv_section = heading.find_parent() or heading.find_next_sibling()
                break

        # Fallback to the whole page body if a specific parent container boundary wasn't isolated
        target_soup = tv_section if tv_section else soup

        # 2. Track down categorized listing sub-blocks (e.g., 'Streaming', 'TV Channels')
        current_category = "General Broadcast"

        for element in target_soup.find_all(["h3", "h4", "div", "span", "a"]):
            text = element.get_text().strip()
            if not text:
                continue

            # Dynamically update the category context when hitting sub-headings
            if text in ["Streaming", "TV Channels"]:
                current_category = text
                continue

            # 3. Dynamic Text De-duplication Strategy
            # The site outputs tags like 'ESPN2 ESPN2' or 'Fubo Sports Fubo Sports'.
            # We split the string in half to see if it's a repeated layout block.
            words = text.split()
            mid = len(words) // 2
            if mid > 0 and words[:mid] == words[mid:]:
                clean_name = " ".join(words[:mid])  # e.g., 'ESPN2'
            else:
                clean_name = text

            # Filter out boilerplate template sentences and navigation elements
            if (
                any(
                    noise in clean_name.lower()
                    for noise in [
                        "tv / streaming",
                        "use this page",
                        "listings can change",
                        "check back regularly",
                        "how to watch",
                        "sign in",
                    ]
                )
                or len(clean_name) > 30
            ):
                continue

            # 4. Map the cleaned name token straight into our dictionary structure
            # To isolate the Broadcaster (e.g., 'ESPN') from the channel ('ESPN2' or 'ESPN Unlimited')
            provider_key = clean_words_to_provider(clean_name)

            if provider_key not in broadcaster_channel_map:
                broadcaster_channel_map[provider_key] = []

            # Append the unique sub-channel variant if it isn't recorded yet
            if clean_name not in broadcaster_channel_map[provider_key]:
                broadcaster_channel_map[provider_key].append(clean_name)

    except Exception as e:
        print(f"❌ Structural extraction parsing error: {e}")

    return broadcaster_channel_map


def clean_words_to_provider(full_channel_name):
    """Helper to dynamically pull the base provider key from a full channel string

    (e.g., 'Fubo Sports' -> 'Fubo', 'ESPN Unlimited' -> 'ESPN').
    """
    first_word = full_channel_name.split()[0].title()
    # Handle minor edge anomalies safely
    if first_word.lower() in ["tv", "the", "live"]:
        return "Other Broadcasters"
    return first_word


# ==========================================
# TEST EXECUTION
# ==========================================
if __name__ == "__main__":
    example_url = (
        "https://www.livesportsontv.com/match/prairie-view-am-texas-southern-1948807"
    )

    print(f"🔄 Extracting data structure from: {example_url}\n")
    output_dict = get_channels_from_match_page(example_url)

    print("📦 RESULT DICTIONARY:")
    print(json.dumps(output_dict, indent=4))
