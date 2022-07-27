
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
