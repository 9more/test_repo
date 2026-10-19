import webbrowser
import re
from rapidfuzz import process, fuzz
from pathlib import Path
import pandas as pd

HOME_DIR = Path.home()
DATA_DIR = HOME_DIR / "Downloads" / "source_file.csv"
pattern = r"[ -/,\s]"

df = pd.read_csv(DATA_DIR)

df["Broadcaster"] = (
    df["Broadcaster"].astype(str).str.lower().str.replace(pattern, "", regex=True)
)
user_input = input("Input broadcaster's name: ")

while True:

    cleaned_input = re.sub(pattern, "", user_input.lower().strip())

    print(f"Searching for: {cleaned_input}")

    results = process.extract(
        cleaned_input,
        df["Broadcaster"],
        scorer=fuzz.partial_ratio,
        score_cutoff=50,
        limit=5,
    )
    if results:
        matched_text, score, row_index = results[0]

        print(f"Match found: '{matched_text}' " f"(Confidence: {score:.1f}%)")

        print(
            f"Server: {df.loc[row_index, 'Server']} ; Decoder: {df.loc[row_index, 'Decoder']}"
        )
        print(score)

        guide_link = df.loc[row_index, "URL"]

        print(f"Opening: {guide_link}")

        webbrowser.open(guide_link)

    else:
        print("No broadcaster match found.")

    user_input = input("input another broadcaster to check guide or press q to quit: ")
    if user_input == "q":
        break
