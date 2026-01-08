from selenium.webdriver.common.by import By

# Aufgabe 1.2 (Web-Automatisierung mit Selenium)
# Bestimmtes Produkt überprüfen**
#   - Nachdem ich mich eingeloggt habe, finde und überprüfe ich das Vorhandensein des folgenden Produkts:
#       - Produktname: "Sauce Labs Backpack".
#   - Ich stelle sicher (assert), dass der Produktname auf der Seite angezeigt wird.


def check_product_exists(driver, product_name="Sauce Labs Backpack"):

# Prüft, ob der Produktname "Sauce Labs Backpack" vorhanden ist.

    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [p.text for p in product_elements]

    print("Gefundene Produkte:", product_names)

    assert product_name in product_names, f"Produkt '{product_name}' ist NICHT vorhanden!"
    print(f" Produkt '{product_name}' ist vorhanden")

#============================= test session starts ==============================
# collecting ... collected 1 item
# sauce_demo.py::test_login_sauce_demo PASSED                              [100%]Gefundene Produkte: ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
# Produkt 'Sauce Labs Backpack' ist vorhanden