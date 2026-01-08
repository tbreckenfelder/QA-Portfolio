from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import date
import time
def get_exactly_18_birthdate():
    today = date.today()
    try:
        birthdate = today.replace(year=today.year - 18)
    except ValueError:
        # Sonderfall: 29. Februar
        birthdate = today.replace(month=2, day=28, year=today.year - 18)
    return birthdate.strftime("%d-%m-%Y")
def test_exactly_18():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)
    try:
        # 1. Website öffnen
        driver.get("https://grocerymate.masterschool.com/store")
        # 2. Date input field finden
        date_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
            )
        )
        # 3. Geburtsdatum für exakt 18 Jahre berechnen
        birthdate_18 = get_exactly_18_birthdate()
        print(f"Testing birthdate: {birthdate_18}")
        date_input.send_keys(birthdate_18)
        # 4. Confirm-Button anklicken
        confirm_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='modal-content']//button[normalize-space()='Confirm']")
            )
        )
        confirm_button.click()
        # 5. Warten, bis das Modal verschwindet (Zugriff erlaubt)
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'modal-content')]")
            )
        )
        time.sleep(3)
    finally:
        driver.quit()
    if __name__ == "__main__":
        test_exactly_18()