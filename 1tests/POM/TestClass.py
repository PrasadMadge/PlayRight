import time

from playwright.sync_api import Playwright, sync_playwright, expect
from login_page_elements import LoginPages


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(3000)
    login_page = LoginPages(page)
    expect(login_page.username).to_be_visible()
    expect(login_page.password).to_be_visible()
    # page.locator("[data-test=\"username\"]").fill("standard_user")

    login_page.username.fill("standard_user")
    time.sleep(8000)

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
