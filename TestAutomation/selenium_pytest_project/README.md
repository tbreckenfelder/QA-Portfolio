## Age Verification UI Tests (Python + Selenium + Pytest)

Automatisierte UI-Tests für die **Age Verification (18+)** der Website:

https://grocerymate.masterschool.com/store

Getestet wird der Zugriff für Nutzer im Alter von **17, 18 und 19** Jahren.

---
## Tech Stack

- **Python 3.9+**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver**
- **Page Object Model (POM)**

---

## Projektstruktur

p## 📁 Projektstruktur

project-root/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── age_verification_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_age_verification.py
├── screenshots/
│   └── (Screenshots werden hier gespeichert)
├── requirements.txt
└── README.md

---

## 🧩 Architektur

- **`pages/`**: Page Objects, kapseln Locators & UI-Aktionen  
- **`tests/`**: Testlogik und Assertions, parametrisiert  
- **`conftest.py`**: WebDriver Fixture + Screenshots bei Fehlern  

Vorteile: gut wartbar, wiederverwendbar, stabil.

---

## Getestete Szenarien

| Alter | Erwartetes Ergebnis |
|-------|-----------------|
| 17    | Zugriff verweigert |
| 18    | Zugriff erlaubt |
| 19    | Zugriff erlaubt |

Parametrisierung in Pytest:

```
@pytest.mark.parametrize(
    "age, should_be_allowed",
    [
        (17, False),
        (18, True),
        (19, True),
    ],
)
```
___
## Screenshots bei Fehlern

- Bei jedem Testfehler (Setup oder Call)
- Ein Screenshot pro Parametrisierung
- Automatisch gespeichert unter:
```
screenshots/

└── test_age_verification[17-False].png
```
___
## Setup (Python)
### Repository klonen
```
git clone <repository-url>
cd project-root
```
### Virtuelle Umgebung
- python -m venv venv
- source venv/bin/activate   # macOS / Linux
- venv\Scripts\activate      # Windows

### Abhängigkeiten installieren
```
pip install -r requirements.txt
```

### ChromeDriver
- Google Chrome muss installiert sein
- ChromeDriver im PATH oder automatisch via Selenium Manager
___
### Tests ausführen
- Alle Tests
```
- pytest
```
### Mit ausführlicher Ausgabe
```
pytest -v
```

### Nur Age Verification
```
pytest tests/test_age_verification.py
```
___
### Wichtige Details
### WebDriver Fixture

- Neuer Browser pro Test
- Automatisches driver.quit()
- Screenshot bei Fehlern (Setup oder Assertion)

### Storage Cleanup
```
window.localStorage.clear()
window.sessionStorage.clear()
```
→ garantiert Modal bei jedem Testlauf
___
- BasePage Konzept

```BasePage``` kapselt:
- Waits (sichtbar, klickbar, verschwunden)
- Storage-Handling
- JS-Hilfsfunktionen

Alle Pages erben davon → Tests bleiben schlank.
___
### Autor
Automatisierte Tests & Architektur: Thomas Breckenfelder
