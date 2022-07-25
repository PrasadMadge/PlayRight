from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
