# Simples Script zum Testen ob Selenium richtig funktioniert:
from selenium import webdriver  # Import the necessary module to control the web browser
import time  # Import the time module for adding delays

# Instantiate the web driver for Chrome
driver = webdriver.Chrome()

# Navigate to the Masterschool website
driver.get("https://www.masterschool.com")

# Wait for 3 seconds to allow the page to load completely
time.sleep(3)

# Print the title of the page to the console
print(driver.title)

# Close the browser and end the WebDriver session
driver.quit()

#============================= test session starts ==============================
# collecting ... collected 1 item
# grocery_mate.py::test_login_grocerymate PASSED                           [100%]Market Mate

