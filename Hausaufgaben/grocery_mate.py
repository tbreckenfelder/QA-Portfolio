from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_grocerymate():
    driver = webdriver.Chrome()
    driver.get("https://grocerymate.masterschool.com/auth")
    driver.implicitly_wait(3000)

    # Find the elements
    # email input
    email_el = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    # password input
    password_el = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    # Login Button
    login_btn = driver.find_element(By.CLASS_NAME, "submit-btn")
    time.sleep(4)

    # type email into email field
    email_el.send_keys("wbreckendorfer@web.de")
    time.sleep(4)

    # type password into password field
    password_el.send_keys("qwertz")
    time.sleep(4)

    # click on the login button
    login_btn.click()
    time.sleep(4)

    print(driver.title)
    print(driver.current_url)

#============================= test session starts ==============================
# collecting ... collected 1 item
# grocery_mate.py::test_login_grocerymate PASSED                           [100%]Market Mate