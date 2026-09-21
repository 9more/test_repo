from config import DOWNLOAD_DIR, MORNING, NIGHT
from browser import open_browser, close_browser


def select_day(page, day):
    """
    Select Today or Tomorrow.
    """

    if day == "today":
        button = page.get_by_test_id("today-btn")

    elif day == "tomorrow":
        button = page.get_by_test_id("tomorrow-btn")

    else:
        raise ValueError("day must be 'today' or 'tomorrow'")

    button.click()

    # Allow the table to refresh
    page.wait_for_timeout(2000)

    print(f"Selected: {day}")


def download_csv(page, filename):
    """
    Download the currently displayed schedule.
    """

    with page.expect_download() as download_info:
        page.get_by_test_id("csv-btn").click()

    download = download_info.value

    destination = DOWNLOAD_DIR / filename

    download.save_as(destination)

    print(f"Downloaded: {destination}")

    return destination


def download_schedule(shift):
    """
    Download the schedules required for the shift.

    Morning:
        Today only

    Night:
        Today + Tomorrow
    """

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    playwright, browser, page = open_browser()

    try:

        # ====================================================
        # MORNING SHIFT
        # ====================================================

        if shift == MORNING:

            select_day(page, "today")

            today_file = download_csv(page, "today.csv")

            return {"today": today_file}

        # ====================================================
        # NIGHT SHIFT
        # ====================================================

        elif shift == NIGHT:

            select_day(page, "today")

            today_file = download_csv(page, "today.csv")

            select_day(page, "tomorrow")

            tomorrow_file = download_csv(page, "tomorrow.csv")

            return {"today": today_file, "tomorrow": tomorrow_file}

        else:

            raise ValueError(
                f"Unknown shift: {shift}. " f"Use '{MORNING}' or '{NIGHT}'."
            )

    finally:

        close_browser(playwright, browser)


if __name__ == "__main__":

    print("Testing MORNING shift...\n")

    morning_files = download_schedule(MORNING)

    print("\nMorning files:")
    print(morning_files)

    print("\n" + "=" * 50)

    print("\nTesting NIGHT shift...\n")

    night_files = download_schedule(NIGHT)

    print("\nNight files:")
    print(night_files)
