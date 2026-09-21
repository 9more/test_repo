import webbrowser
import difflib

sources = {
    "allente": "https://www.allente.se/tv-guide/",
    "eurosport": "https://www.home3.ee/tv-kava/telekanalid/eurosport-2/",
    "supersport": "https://supersport.com/tv-guide",
    "canalsport": "https://www.canalplussport.cz/tv-program",
    "polsat": "https://www.polsat.pl/program-tv/",
    "israel": "192.168.81.120",
    "digi": "https://www.digisport.ro/program-tv/digisport-1",
    "live": "https://www.livesoccertv.com/schedules/",
    "livesports": "https://www.livesportsontv.com/schedules/",
    "sport": "https://www.sport.tvp.pl/tv-guide",
    "espn": "https://www.espn.com/watch/schedule/_/type/upcoming/categoryId/60459870-f8fc-3b3a-a6b9-d8af4bf19223/country/us/redirected/true",
<<<<<<< HEAD
    "russia": "https://matchtv.ru/tvguide",
    "virgin": "https://www.tvguide.co.uk",
    "live_source": "https://www.livesoccertv.com/schedules/",
    "sport_event": "https://sporteventz.com/en/",
=======
    "match": "https://matchtv.ru/tvguide",
    "uklisting": "https://www.tvguide.co.uk",
    "live_source": "https://www.livesoccertv.com/schedules/",
    "sport_event": "https://sporteventz.com/en/",
    "virgin": "https://www.virginmediatelevision.ie",
    "khltv": "https://www.khl.ru/tv/",
>>>>>>> feature
}

valid_keys = sources.keys()

source = input(
<<<<<<< HEAD
    "type 4 letters close match of bradcaster/" "e.g pol for Polsat:  "
=======
    "type 4 letters close match of bradcaster/" "e.g pol for Polsat: "
>>>>>>> feature
).lower()

best_match = difflib.get_close_matches(source, valid_keys, n=1, cutoff=0.4)

<<<<<<< HEAD
=======
if not best_match:
    print("No matching broadcaster found.")
    input("Press Enter to exit...")
    exit()

>>>>>>> feature
if best_match[0] == "israel":
    num = int(input("input stb number....  "))
    end_ip = sources[best_match[0]][-3:]
    end_ip_update = str(int(end_ip) + num)
    ip_address = sources[best_match[0]].replace(end_ip, end_ip_update)
    print(ip_address)
    webbrowser.open(f"http://{ip_address}")

else:
    matched_key = best_match[0]
    print(matched_key)
    webbrowser.open(sources[matched_key])
