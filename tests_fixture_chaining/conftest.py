import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import page

from tests_fixture_chaining.LoginPage import LoginPage


@pytest.fixture
def set_up(page):
    # the below lines are not mandatory hence auto added by playwright in fixtures
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    #
    # # Open new page
    # page = context.new_page()

    page.set_default_timeout(3000)
    yield page
    page.close()


#   we can use return keyword here but yield was used for specific reason

@pytest.fixture
def login_fixture(set_up):
    page = set_up
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    # login_page.username.fill("standard_user")
    # login_page.password.fill("secret_sauce")
    # login_page.login_button.click()

    login_page.login("standard_user", "secret_sauce")
    return page
