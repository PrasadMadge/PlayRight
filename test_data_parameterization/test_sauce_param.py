import pytest
from playwright.sync_api import expect


# to run pytest -m "params" --headed


@pytest.mark.params
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                ("locked_out_user", "secret_sauce"),
                                                pytest.param("wrong_user", "secret_sauce", marks=pytest.mark.xfail)])
def test_data_parameter(page, username, password) -> None:
    # page = set_up

    # Go to https://www.google.com/?gws_rd=ssl
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(3000)
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    expect(page.locator(".app_logo")).to_be_visible()


@pytest.mark.params
@pytest.mark.parametrize("username", ["standard_user",
                                      "locked_out_user",
                                      pytest.param("wrong_user")])
@pytest.mark.parametrize("password", ["secret_sauce",
                                      "secret_sauce",
                                      pytest.param("secret_sauce", marks=pytest.mark.xfail)])
def test_data_stack_parameter(page, username, password) -> None:
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(3000)
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    expect(page.locator(".app_logo")).to_be_visible()


#
# with sync_playwright() as playwright:
#     test_login(playwright)
