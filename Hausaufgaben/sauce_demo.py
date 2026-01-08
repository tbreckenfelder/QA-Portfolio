from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from product_check import check_product_exists

# Aufgabe 1.1 (Web-Automatisierung mit Selenium)

# URL: https://www.saucedemo.com/
# 1. Login-Automatisierung
#     Automatisiere den Login-Prozess für die Website mit den bereitgestellten Testzugangsdaten.
# 2. Produkt-Such-Verifikation
#     Navigiere nach dem Login zur Produktseite und überprüfe das Vorhandensein bestimmter Produktnamen.

# 1. Auf der Website einloggen
# Navigiere zu website https://www.saucedemo.com/.
# - Finde und interagiere mit dem Login-Formular:

def test_login_sauce_demo():
    driver = webdriver.Chrome()     # startet den browser
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(4)
# Richtiges Element finden
    username = driver.find_element(By.ID,"user-name")        # username input
    password = driver.find_element(By.ID, "password")        # password input
    login_btn = driver.find_element(By.ID, "login-button")      # Login Button
    time.sleep(4)
# type username into username field
    username.send_keys("standard_user")
    time.sleep(4)
# type password into password field
    password.send_keys("secret_sauce")
    time.sleep(4)
# click on the login button
    login_btn.click()
    time.sleep(4)

    check_product_exists(driver, "Sauce Labs Backpack")     # greift auf externen Produktcheck zu

    driver.quit()       # schliesst den Browser

test_login_sauce_demo()

#============================= test session starts ==============================
#collecting ... collected 1 item
#sauce_demo.py::test_login_sauce_demo PASSED                              [100%]
##############################################


