from config import MORNING, NIGHT
from downloader import download_schedule
from csv_loader import load_schedule
from comparator import compare_morning, compare_night
from reporter import write_reports


def run_morning():
    """
    Run the morning schedule comparison.

    Morning:
        Download today's schedule
        Compare broadcaster changes on each server
        Generate actionable report
    """

    print("\n" + "=" * 60)
    print("STARTING MORNING RUN")
    print("=" * 60)

    files = download_schedule(MORNING)

    today_df = load_schedule(files["today"])

    result = compare_morning(today_df)

    report_path = write_reports(result)

    print("\nMorning run completed.")
    print(f"Report: {report_path}")


def run_night():
    """
    Run the night schedule comparison.

    Night:
        Download today's schedule
        Download tomorrow's schedule
        Compare tomorrow against today
        Generate actionable report
    """

    print("\n" + "=" * 60)
    print("STARTING NIGHT RUN")
    print("=" * 60)

    files = download_schedule(NIGHT)

    today_df = load_schedule(files["today"])

    tomorrow_df = load_schedule(files["tomorrow"])

    result = compare_night(today_df, tomorrow_df)

    report_path = write_reports(result)

    print("\nNight run completed.")
    print(f"Report: {report_path}")


def main():
    """
    Entry point for the scheduler comparison tool.
    """

    print("\nDAILY SET UP")
    print("-------------")
    print("1. Morning")
    print("2. Night")

    choice = input("\nSelect run (1/2): ").strip()

    if choice == "1":

        run_morning()

    elif choice == "2":

        run_night()

    else:

        print("\nInvalid selection. " "Please choose 1 or 2.")


if __name__ == "__main__":
    main()
