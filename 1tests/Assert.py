# 2 types
# assert using expect function
# assert using assert keyword
# Difference , expect applies implict wait before failing
# Assert does not waits and fails right away


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.google.com/?gws_rd=ssl")

    # correct locator to practise
    # button:has-text(\"Accept all\")

    # Fails after 5 seconds of implicit wait
    expect(page.locator("intentionally wrong locator")).to_be_visible()

    # Fails right away
    assert page.locator("intentionally wrong locator").is_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
