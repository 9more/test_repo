from bsd import get_event_broadcasts


def display_result(result):

    print("\n" + "=" * 40)
    print("MATCH")
    print("=" * 40)

    if not result["match_found"]:
        print()
        print(f'{result["team1"]} vs {result["team2"]}')
        print()
        print("No match found for today.")
        return

    print()
    print(result["team1"])
    print("vs")
    print(result["team2"])

    print()
    print(f'League: {result["league"]}')
    print(f'Date: {result["date"]}')
    print(f'Kick-off: {result["kickoff"]}')
    print(f'Event ID: {result["event_id"]}')

    print("\n" + "=" * 40)
    print("BROADCASTERS")
    print("=" * 40)

    broadcasters = result["broadcasters"]

    if not broadcasters:
        print("\nNo broadcasters found.")
        return

    current_country = None

    for broadcaster in broadcasters:

        country = broadcaster["country"]
        channel = broadcaster["channel"]

        if country != current_country:
            print()
            print(country)
            current_country = country

        print(f"  • {channel}")

    countries = {broadcaster["country"] for broadcaster in broadcasters}

    channels = {
        (broadcaster["country"], broadcaster["channel"]) for broadcaster in broadcasters
    }

    print("\n" + "=" * 40)
    print("SUMMARY")
    print("=" * 40)

    print()
    print(f"Total countries: {len(countries)}")
    print(f"Total broadcasters: {len(channels)}")


def main():

    team1 = input("Enter first team: ").strip()
    team2 = input("Enter second team: ").strip()

    if not team1 or not team2:
        print("Please enter both team names.")
        return

    try:
        result = get_event_broadcasts(team1, team2)
        display_result(result)

    except KeyError:
        print("BSD_API_KEY is not set in your environment.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
