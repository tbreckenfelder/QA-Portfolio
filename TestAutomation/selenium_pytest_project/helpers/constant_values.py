BASE_URL = "https://grocerymate.masterschool.com"

# URLs für die Navigation
LOGIN_URL = f"{BASE_URL}/auth"
SHOP_URL = f"{BASE_URL}/store"
CHECKOUT_URL = f"{BASE_URL}/checkout"

# Standard-Timeout (für explizite Waits)
DEFAULT_WAIT_TIME = 8 # Sekunden

# Benutzerdaten
TEST_USER_EMAIL = "greater18@web.de"
TEST_USER_PASSWORD = "qwertz"
TEST_USER_NAME = "greater18" # Benutzername, der in Bewertungen angezeigt wird

# Produkt-Namen (für die ShopPage.find_product_card Logik)
PRODUCT_CELERY = "Celery"
PRODUCT_GINGER = "Ginger"
PRODUCT_KALE = "Kale"

# # Einheitspreise
PRICE_CELERY = 0.70
PRICE_GINGER= 0.60
PRICE_KALE = 1.00

# Gesamtkosten der Produkte
TWENTYSEVEN_CELERY_SUBTOTAL = 18.90
TWENTY_KALE_SUBTOTAL = 20.00
THIRTYFIVE_GINGER_SUBTOTAL = 21.00

# Versandkosten
SHIPPING_COST_STANDARD = 5.00
SHIPPING_COST_FREE = 0.00    # ab 20 € Wahrenwert

# Versandkosten Schwellenwert
FREE_SHIPPING_THRESHOLD = 20.00 # Gratis Versand ab 20 €

# Produkt-URLs (für die Rating-Tests)
PRODUCT_CELERY_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb479a1"
PRODUCT_GINGER_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb479a6"
PRODUCT_KALE_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb479b5"

PRODUCT_CORONA_EXTRA_NAME = "Corona Extra"
PRODUCT_CORONA_EXTRA_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb47a80"

# Standard-Geburtsdatum für Altersfreigabe (älter als 18)
AGE_CONFIRMATION_DATE = "01-01-2007"

# Erwartete Fehlermeldung
RATING_REQUIRED_ERROR = "Invalid input for the field 'Rating'. Please check your input."