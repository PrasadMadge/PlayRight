class LoginPages:

    def __init__(self, page):
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

