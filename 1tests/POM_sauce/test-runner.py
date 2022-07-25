from playwright.sync_api import Playwright, sync_playwright
from LoginPage import LoginPage

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    # login_page.username.fill("standard_user")
    # login_page.password.fill("secret_sauce")
    # login_page.login_button.click()

    login_page.login("standard_user", "secret_sauce")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)