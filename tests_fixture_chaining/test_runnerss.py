from playwright.sync_api import Playwright, sync_playwright
from test_python_package.tests_POM_sauce.LoginPage import LoginPage
import pytest


# to run use pytest -m "fixture_chaining" --headed

@pytest.mark.fixture_chaining
def test_run_fixture_normal(set_up) -> None:
    # Open new page
    page = set_up

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    # login_page.username.fill("standard_user")
    # login_page.password.fill("secret_sauce")
    # login_page.login_button.click()

    login_page.login("standard_user", "secret_sauce")


# with sync_playwright() as playwright:
#     test_run(playwright)

@pytest.mark.fixture_chaining
def test_run_fixture_chaining(login_fixture) -> None:
    # Open new page
    page = login_fixture
