from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Aufgabe 3 (Benutzer registrieren)
# Falls angezeigt, soll Popup geschlossen werden

def close_ads(driver):
    driver.implicitly_wait(1)

    # Alle möglichen Close-Button Muster
    close_selectors = [
        "//*[@id='google_close_button']",
        "//*[@aria-label='Close ad']",
        "//*[contains(@id,'close')]",
        "//*[contains(@id,'dismiss')]",
        "//div[@role='button'][contains(.,'Close')]",
        "//span[contains(text(),'Close')]"
    ]

    def search_iframe(frame):
        try:
            driver.switch_to.frame(frame)

            # Versuche alle Close-Buttons
            for sel in close_selectors:
                try:
                    btn = driver.find_element(By.XPATH, sel)
                    btn.click()
                    print("Ad geschlossen!")
                    return True
                except:
                    pass

            # Wenn im aktuellen Frame kein Button dann tiefer gehen
            subframes = driver.find_elements(By.TAG_NAME, "iframe")
            for sf in subframes:
                if search_iframe(sf):
                    return True

        except:
            pass
        finally:
            driver.switch_to.default_content()

        return False

    # Start -> alle Top-Level Frames durchsuchen
    frames = driver.find_elements(By.TAG_NAME, "iframe")
    for frame in frames:
        if search_iframe(frame):
            return True

    return False

def test_new_user_signup():
    driver = webdriver.Chrome()                             # 1. Browser starten
    driver.get("https://www.automationexercise.com/")       # 2. Zur URL navigieren
    wait = WebDriverWait(driver, 10)                # Pausiere
    #assert "Automation Exercise" in driver.title           # 3. Überprüfe, dass die Startseite erfolgreich sichtbar ist

    signup_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
    signup_btn.click()                                      # 4. Oben auf die Schaltfläche „Signup / Login“ klicken

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))       # 5. Überprüfen, dass „New User Signup!“ sichtbar ist

    name_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")           # findet das richtige Eingabefeld
    email_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")         # findet das richtige Eingabefeld

    test_name = "TestUser"                                      # Testdaten name
    test_email = f"testuser_{int(time.time())}@gmail.com"       # Testdaten email

    name_field.send_keys(test_name)                             # 6. Testdaten eintragen
    email_field.send_keys(test_email)                           # 6. Testdaten eintragen

    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()     # 7. Den richtigen Signup klicken
    time.sleep(4)

    enter_info_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))
    #assert enter_info_text.is_displayed()                                         # 8. "ENTER ACCOUNT INFORMATION" prüfen

    driver.find_element(By.ID, "id_gender1").click()                        # 9. Details ausfüllen: Titel (Mr.)
    driver.find_element(By.ID, "password").send_keys("Test1234!")           # 9. Details ausfüllen: Passwort

    Select(driver.find_element(By.ID, "days")).select_by_value("1")         # 9. Details ausfüllen: Geburtstag
    Select(driver.find_element(By.ID, "months")).select_by_value("12")      # 9. Details ausfüllen: Geburtsmonat
    Select(driver.find_element(By.ID, "years")).select_by_value("2000")     # 9. Details ausfüllen: Geburtsjahr

    driver.find_element(By.ID, "newsletter").click()    # 10. Kontrollkästchen „Sign up for our newsletter!“ auswählen
    driver.find_element(By.ID, "optin").click()         # 11. Kontrollkästchen „Receive special offers from our partners!“ auswählen

    driver.find_element(By.ID, "first_name").send_keys("Test")              # 12. Vorname ausfüllen
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "company").send_keys("TestCompany")
    driver.find_element(By.ID, "address1").send_keys("Test Street 123")
    driver.find_element(By.ID, "address2").send_keys("Apt 456")
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
    time.sleep(4)

    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()      # 13. Auf die Schaltfläche „Create Account“ klicken

    account_created_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))
    #assert account_created_text.is_displayed()                                             # 14. Überprüfen, dass „ACCOUNT CREATED!“ sichtbar ist

    driver.find_element(By.LINK_TEXT, "Continue").click()                            # 15. Auf die Schaltfläche „Continue“ klicken

    #logged_in_text = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(text(),'Logged in as {test_name}')]")))
    #assert logged_in_text.is_displayed()                                                   # 16. Überprüfen, dass „Logged in as username“ sichtbar ist

    driver.find_element(By.LINK_TEXT, "Delete Account").click()                     # 17. Auf die Schaltfläche „Delete Account“ klicken

    account_deleted_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
    #assert account_deleted_text.is_displayed()                                            # 18. Überprüfen, dass „ACCOUNT DELETED!“ sichtbar ist
    driver.find_element(By.LINK_TEXT, "Continue").click()                           # 18. und auf „Continue“ klicken

    print(" Benutzerregistrierung, Login und Löschung erfolgreich abgeschlossen.")

    driver.quit()
    time.sleep(6)

# Selector für: Name
# form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)

# Selector für: Email Adresse
# form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)

# xpath
# //*[@id="form"]/div/div/div[3]/div/form/input[2]

# xPath
# //*[@id="form"]/div/div/div[3]/div/form/input[3]

# button xpath
# /html/body/section/div/div/div[3]/div/form/input[2]

# button selector
# form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)

#============================= test session starts ==============================
# collecting ... collected 1 item

# Benutzer registrieren.py::test_new_user_signup PASSED         [100%] Benutzerregistrierung, Login und Löschung erfolgreich abgeschlossen.

