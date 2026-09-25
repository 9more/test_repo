import webbrowser
import difflib
from source import sources

valid_keys = sources.keys()

source = input(
    "type 4 letters close match of bradcaster/"
    "e.g pol for Polsat:  "
    "type 4 letters close match of bradcaster/"
    "e.g pol for Polsat: "
).lower()

best_match = difflib.get_close_matches(source, valid_keys, n=1, cutoff=0.4)

if not best_match:
    print("No matching broadcaster found.")
    input("Press Enter to exit...")
    exit()

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
