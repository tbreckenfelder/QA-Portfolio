import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(username, "secret_sauce")

    if expected_success:
        assert inventory_page.is_loaded(), f"Login sollte für {username} erfolgreich sein"
        assert inventory_page.is_inventory_visible(), "Produktliste ist nicht sichtbar"
    else:
        error_text = login_page.get_error_text()
        assert "locked out" in error_text.lower(), f"{username} sollte gesperrt sein"


# ================================================================================ test session starts ================================================================================
# platform darwin -- Python 3.13.0, pytest-9.0.1, pluggy-1.6.0
# rootdir: /Users/thomasbreckenfelder/PycharmProjects/qa-engineering-portfolio1/Hausaufgaben/saucedemo
# collected 6 items
#
# tests/test_login.py ......                                                                                                                                                    [100%]