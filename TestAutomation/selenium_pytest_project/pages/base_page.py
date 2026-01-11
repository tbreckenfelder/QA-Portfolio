from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Gemeinsame Basis für alle Page Objects
    """
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Generic find / wait helpers ----------

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_invisibility(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def is_element_present(self, locator) -> bool:
        return len(self.driver.find_elements(*locator)) > 0

    # ---------- Browser / JS helpers ----------

    def clear_storage(self):
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        self.driver.refresh()

    def execute_js(self, script: str):
        return self.driver.execute_script(script)
