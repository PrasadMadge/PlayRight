import pytest


@pytest.mark.regression
def test_login12(set_up) -> None:
    page = set_up

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

#
# with sync_playwright() as playwright:
#     test_login(playwright)
