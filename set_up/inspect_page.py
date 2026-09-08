import csv

file_path = "data/downloads/today.csv"

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.reader(file)

    header = next(reader)

    for line_number, row in enumerate(reader, start=2):

        if len(row) != len(header):

            print("\nHEADER")
            print("-" * 80)

            for i, column in enumerate(header):
                print(f"{i}: {column!r}")

            print("\nBAD ROW")
            print("-" * 80)

            for i, value in enumerate(row):
                print(f"{i}: {value!r}")

            print(f"\nLine: {line_number}")

            print(f"Expected fields: {len(header)}")

            print(f"Actual fields: {len(row)}")

            break
