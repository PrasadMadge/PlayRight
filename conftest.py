import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page) -> None:

    # the below lines are not mandatory hence auto added by playwright in fixtures
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    #
    # # Open new page
    # page = context.new_page()

    page.set_default_timeout(3000)
    yield page
#   we can use return keyword here but yield was used for specific reason
