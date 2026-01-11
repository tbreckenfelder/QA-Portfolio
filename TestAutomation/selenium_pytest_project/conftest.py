import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    yield driver

    # Screenshot bei Fehler (setup ODER call)
    if request.node.rep_setup.failed or request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        # Eindeutiger Name inkl. Parametrisierung
        test_name = request.node.nodeid.replace("/", "_").replace("::", "_")
        screenshot_path = f"screenshots/{test_name}.png"

        driver.save_screenshot(screenshot_path)

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
