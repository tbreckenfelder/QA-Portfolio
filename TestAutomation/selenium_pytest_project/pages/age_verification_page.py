from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AgeVerificationPage(BasePage):
    DATE_INPUT = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[@class='modal-content']//button[normalize-space()='Confirm']",
    )
    MODAL = (By.XPATH, "//div[contains(@class,'modal-content')]")

    def enter_birthdate(self, birthdate: str):
        date_input = self.wait_for_visibility(self.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(birthdate)

    def confirm(self):
        self.wait_for_clickable(self.CONFIRM_BUTTON).click()

    def is_modal_visible(self) -> bool:
        return self.is_element_present(self.MODAL)

    def wait_until_modal_disappears(self):
        self.wait_for_invisibility(self.MODAL)
