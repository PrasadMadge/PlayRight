from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.google.com/?gws_rd=ssl")

    # Click button:has-text("Accept all")
    page.locator("button:has-text(\"Accept all\")").click()
    page.wait_for_url("https://www.google.com/?gws_rd=ssl")

    # Click [aria-label="Search"]
    page.locator("[aria-label=\"Search\"]").click()

    # Fill [aria-label="Search"]
    page.locator("[aria-label=\"Search\"]").fill("Euro to inr")

    assert page.locator("[aria-label=\"Search\"]").is_visible()
    # Press Enter
    page.locator("[aria-label=\"Search\"]").press("Enter")

    # ---------------------
    context.close()
    browser.close()

#  this call is redundant due to pytest

#
# with sync_playwright() as playwright:
#     test_run(playwright)
