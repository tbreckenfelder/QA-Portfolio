import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import date

def get_birthdate_for_age(age: int) -> str:
    today = date.today()
    try:
        birthdate = today.replace(year=today.year - age)
    except ValueError:
        birthdate = today.replace(month=2, day=28, year=today.year - age)
    return birthdate.strftime("%d-%m-%Y")

@pytest.mark.parametrize(
    "age, should_be_allowed",
    [
        (17, False),
        (18, True),
        (19, True),
    ],
)
def test_age_check(age, should_be_allowed):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://grocerymate.masterschool.com/store")

        # Storage löschen → Modal kommt sicher wieder
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        driver.refresh()

        date_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
            )
        )

        date_input.send_keys(get_birthdate_for_age(age))

        confirm_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='modal-content']//button[normalize-space()='Confirm']")
            )
        )
        confirm_button.click()

        if should_be_allowed:
            # Modal muss verschwinden
            wait.until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'modal-content')]")
                )
            )
        else:
            # Modal muss sichtbar bleiben
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'modal-content')]")
                )
            )

    finally:
        driver.quit()
