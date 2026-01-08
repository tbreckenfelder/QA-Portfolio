**Task 1**
---

1. Schreiben Sie den XPath-Ausdruck, um das Haupt-Element **h1** zu finden.
- //h1[@id="mainTitle"]
---
2. Schreiben Sie den XPath-Ausdruck, um den Navigationslink **About Us** auszuwählen.
- //nav//a[text()="About Us"]
---
3. Schreiben Sie den XPath-Ausdruck, um den Dropdown-Link **Graphic Design** auszuwählen.
- //a[text()="Graphic Design"]
---
4. Schreiben Sie den XPath-Ausdruck, um den Namen des Teammitglieds **Jane Smith** auszuwählen.
- //h4[text()="Jane Smith"]
---
5. Schreiben Sie den XPath-Ausdruck, um die Beschreibung (innerhalb des Absatzes) von **SEO Services** auszuwählen.
- //section[@id="services"]//div[@class="service-item"][h3[text()="SEO Services"]]/p
---
6. Schreiben Sie einen XPath-Ausdruck, um alle Service-Elemente im Abschnitt **„Our Services“ auszuwählen**.
- //section[@id="services"]//div[@class="service-item"]
---
7. Wie lautet der XPath-Ausdruck, um das **email input field** im Kontaktformular auszuwählen?
- //form[@id="contactForm"]//input[@id="email"]
---
8. Wie würden Sie einen XPath-Ausdruck schreiben, um das **entire contact form** auszuwählen?
- //form[@id="contactForm"]
---
9. Geben Sie den XPath-Ausdruck an, um das **footer paragraph element** auszuwählen.
- //footer/p
---
10. Wie lautet der XPath-Ausdruck, um den Namen des **first team member's** (`<h4>`) auszuwählen?
- //div[@class="team"]/ul/li[1]/h4
---
11. Wie kann man die Beschreibung des **second service** mithilfe von XPath auswählen?
- //section[@id="services"]/div[@class="service-list"]/div[@class="service-item"][2]/p
---
12. Welcher XPath-Ausdruck wählt die **Überschrift** des Abschnitts „Kontakt“ (`<h2>`-Element) aus?
- //section[@id="contact"]/h2
---
13. Schreiben Sie einen XPath-Ausdruck, um **all links** im Dropdown-Menü unter dem Navigationspunkt „Services“ auszuwählen.
- //section[@id="services"]//div[@class="service-item"]/(h3 | p)
---
14. Welcher XPath-Ausdruck wählt **das erste `<li>`-Element** im Abschnitt „Unser Team“ aus?
- //div[@class="team"]/ul/li[1]
---
15. Geben Sie den XPath-Ausdruck an, um die **Schaltfläche „Send Message“** im Kontaktformular zu finden.
- //form[@id="contactForm"]//input[@type="submit" and @value="Send Message"]
---