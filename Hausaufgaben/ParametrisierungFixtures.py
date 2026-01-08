import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

## Aufgabe 2 (**Parametrisierung und Fixtures**)

# Ich erweitere nun mein Login-Skript, um **Parametrisierung** einzuschließen
# und eine **Driver-Fixture** zu erstellen. Ich stelle sicher, dass ich **alle Benutzernamen**,
# die auf [https://www.saucedemo.com](https://www.saucedemo.com/) verfügbar sind, teste.

# Liste aller verfügbaren Nutzer von https://www.saucedemo.com

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

USERNAMES = [
    ("standard_user", True),
    ("locked_out_user", False),
    ("problem_user", True),
    ("performance_glitch_user", True),
    ("error_user", True),
    ("visual_user", True),
]

@pytest.mark.parametrize("username, expected_success", USERNAMES)
def test_login_users(driver, username, expected_success):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    if expected_success:
        # Nach dem Login soll Produktliste sichtbar sein
        assert driver.current_url.endswith("/inventory.html")
    else:
        # Fehlgeschlagener Login
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "locked out" in error_msg.lower()
