from playwright.sync_api import sync_playwright

from config import WEBSITE_URL, BROWSER_PROFILE_DIR


def open_browser():

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_PROFILE_DIR), headless=False, accept_downloads=True
    )

    if browser.pages:
        page = browser.pages[0]
    else:
        page = browser.new_page()

    page.goto(WEBSITE_URL, wait_until="domcontentloaded")

    return playwright, browser, page


def close_browser(playwright, browser):
    """
    Close the browser and Playwright cleanly.
    """

    browser.close()
    playwright.stop()
