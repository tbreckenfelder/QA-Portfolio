from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

# Test-Daten: Hier setzen wir die Bestellsummen, die getestet werden sollen
test_data = [
    (20.00, False),   # Keine Versandkosten bei genau 20 €
    (19.90, True),    # Versandkosten bei 19,90 €
    (33.00, False),   # Keine Versandkosten bei 33 €
]


# Funktion zur Berechnung der Versandkosten auf der Seite
def berechne_versandkosten(warensumme: float) -> bool:
    # Browser starten und Seite öffnen
    driver = webdriver.Chrome()  # Hier Chrome.
    driver.get('https://grocerymate.masterschool.com/checkout')

    # Warensumme eingeben (angenommen, es gibt ein Eingabefeld für die Warensumme)
    warensumme_input = driver.find_element(By.ID, 'warensumme')  # ID anpassen
    warensumme_input.clear()  # Feld leer
    warensumme_input.send_keys(str(warensumme))

    # Submit/Bestellvorgang auslösen, falls notwendig
    submit_button = driver.find_element(By.ID, 'submit_button')  # ID des Buttons anpassen
    submit_button.click()

    # Warten, damit die Seite die Versandkosten berechnet
    time.sleep(3)  # Je nach Seite kann das variieren, hier einfach mal 3 Sekunden warten

    # Versandkostenanzeige abrufen (z. B. als Text)
    versandkosten_anzeige = driver.find_element(By.ID, 'shipping_costs')  # ID anpassen
    versandkosten_text = versandkosten_anzeige.text

    # Überprüfen, ob Versandkosten anfallen (wir nehmen an, es steht "Versandkosten" oder "Keine" im Text)
    versandkosten_fallen_an = "Versandkosten" in versandkosten_text  # Beispieltext

    driver.quit()  # Browser schließen

    return versandkosten_fallen_an

