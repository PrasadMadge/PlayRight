from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    # default wait
    page.set_default_timeout(3000)

    # explict wait
    page.wait_for_selector("[data-test='username ']", timeout=9000)

    page.locator("[data-test='username']").fill("standard_user")
    page.locator("")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
