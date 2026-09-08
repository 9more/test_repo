from config import OUTPUT_DIR, RESULT_FILE

FILTERED_FILE = OUTPUT_DIR / "filtered.csv"


def create_filtered_report(df):
    """
    Create filtered.csv.

    Contains:
        - All relevant schedule rows
        - Tennis + InFront removed
        - No Status column
    """

    report = df.copy()

    # Remove Status if it exists
    if "Status" in report.columns:
        report = report.drop(columns=["Status"])

    return report


def create_changes_report(df):
    """
    Create changes.csv.

    Contains:
        - All relevant schedule rows
        - Status column
    """

    return df.copy()


def write_reports(df, filtered_path=FILTERED_FILE, changes_path=RESULT_FILE):
    """
    Write both output files.

    filtered.csv
        Complete filtered schedule
        No Status column

    changes.csv
        Complete filtered schedule
        Status column included
    """

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------
    # FILTERED CSV
    # -----------------------------------------

    filtered = create_filtered_report(df)

    filtered.to_csv(filtered_path, index=False)

    # -----------------------------------------
    # CHANGES CSV
    # -----------------------------------------

    changes = create_changes_report(df)

    changes.to_csv(changes_path, index=False)

    # -----------------------------------------
    # Summary
    # -----------------------------------------

    print("\nOutput summary")
    print("-" * 50)

    print(f"Filtered rows: {len(filtered)}")

    print(f"Changes rows:  {len(changes)}")

    if "Status" in changes.columns:

        print(f"Switches:      " f"{(changes['Status'] == 'switch').sum()}")

        print(f"Check channel: " f"{(changes['Status'] == 'check channel').sum()}")

    print(f"\nFiltered file: {filtered_path}")

    print(f"Changes file:  {changes_path}")

    return {"filtered": filtered_path, "changes": changes_path}
