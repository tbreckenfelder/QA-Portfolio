from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    # Elemente
    def _username_field(self):
        return self.driver.find_element(By.ID, "user-name")

    def _password_field(self):
        return self.driver.find_element(By.ID, "password")

    def _login_button(self):
        return self.driver.find_element(By.ID, "login-button")

    def _error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

    # Aktionen
    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self._username_field().send_keys(username)
        self._password_field().send_keys(password)
        self._login_button().click()

    # Status
    def get_error_text(self):
        return self._error_message().text
