from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self) -> bool:
        return self.driver.current_url.endswith("/inventory.html")

    def is_inventory_visible(self) -> bool:
        inventory = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        return inventory.is_displayed()
