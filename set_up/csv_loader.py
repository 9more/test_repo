import csv
import pandas as pd

REQUIRED_COLUMNS = [
    "FixtureId",
    "WTEvent",
    "StartTime",
    "EndTime",
    "Broadcaster",
    "Server",
    "Decoder",
    "DataSource",
    "Sport",
    "Competition",
    "Country",
    "Home",
    "Away",
]


def load_schedule(file_path):
    """
    Load a scheduling CSV.

    The website may include additional columns after 'Away',
    such as 'Informatoion' and 'Verified'. These columns are
    not relevant to this application and are ignored.

    Original website row order is preserved.
    """

    print(f"\nLoading: {file_path}")

    rows = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.reader(file)

        header = next(reader)

        # Remove whitespace from column names
        header = [column.strip() for column in header]

        # Find the position of the last column we actually need
        try:
            away_index = header.index("Away")

        except ValueError:

            raise ValueError(
                "'Away' column was not found in the CSV.\n" f"Columns found: {header}"
            )

        # We only need columns through Away
        required_header = header[: away_index + 1]

        if required_header != REQUIRED_COLUMNS:

            raise ValueError(
                "Unexpected CSV column structure.\n"
                f"Expected: {REQUIRED_COLUMNS}\n"
                f"Found:    {required_header}"
            )

        for line_number, row in enumerate(reader, start=2):

            # A row must contain at least all columns
            # through Away.
            if len(row) < len(REQUIRED_COLUMNS):

                raise ValueError(
                    f"Line {line_number} has only "
                    f"{len(row)} fields. "
                    f"Expected at least "
                    f"{len(REQUIRED_COLUMNS)}."
                )

            # Keep only the columns through Away.
            # Everything after Away is irrelevant.
            rows.append(row[: len(REQUIRED_COLUMNS)])

    df = pd.DataFrame(rows, columns=REQUIRED_COLUMNS)

    # Clean the fields that are important for comparison
    text_columns = [
        "Sport",
        "Broadcaster",
        "Server",
        "DataSource",
    ]

    for column in text_columns:

        df[column] = df[column].fillna("").astype(str).str.strip()

    print(f"Loaded {len(df)} rows successfully.")

    print(f"Columns retained: {len(df.columns)}")

    return df
