## **Testfall 1: Produktbewertungssystem**
Nach dem erfolgreichen Kaufprozess möchte ich jetzt 3 Produkte - die ich als meine Favoriten gespeichert habe – 
bewerten. Ich wurde jeweils auf die Startseite des Shops zurück geleitet.

Aufruf von Shop https://grocerymate.masterschool.com/
Erstelle neuen account:
Full name: wbreckendorfer / 
email: wbreckendorfer@web.de / 
PW: qwertz /
Status: erfolgreich eingeloggt (PopUp: erfolgreich eingeloggt)

Ich möchte eine 1 Sternebewertung abgeben und einen Bewertungstext hinzufügen.

| Step | Aktion                                  | Erwartetes Ergebnis                         | OK/NOK  | URL                                             | Link to issue                                                         |
|------|-----------------------------------------|---------------------------------------------|---------|-------------------------------------------------|-----------------------------------------------------------------------|
| 1    | Klicke auf Button: Favoriten (Herz)     | 3 soeben gekaufte Produkte werden angezeigt | OK      | https://grocerymate.masterschool.com/store/favs |                                                                       |
| 2    | Klicke auf den Artikel "Ginger"         | Artikel wird angezeigt                      | OK      |                                                 |                                                                       |
| 3a   | Klicke auf 1 Stern                      | Stern wird hellblau angezeigt               | ok      |                                                 |                                                                       |
| 3b   | Gebe "Very fresh quality, love it!" ein |                                             |         |                                                 |                                                                       |
| 3c   | Drücke Button "Send"                    | Zurück zum Artikel                          | OK      |                                                 |                                                                       |
| 4    | Prüfe Sterne                            | Bewertungsanzahl erhöht um 1 (count 7)      | OK      |                                                 |                                                                       |
| 5    | Prüfe Bewertungstext                    | Text wird unter meinem Namen angezeigt      | **NOK** | i.A.                                            | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a4 |


---
## **Testfall 2: Produktbewertungssystem**

Ich möchte eine 5 Sternebewertung und einen Bewertungstext hinzufügen.

| Step | Aktion                                  | Erwartetes Ergebnis                         | OK/NOK    | URL                                             | Link to issue                                                         |
|------|-----------------------------------------|---------------------------------------------|-----------|-------------------------------------------------|-----------------------------------------------------------------------|
| 1    | Klicke auf Button: Favoriten (Herz)     | 3 soeben gekaufte Produkte werden angezeigt | OK        | https://grocerymate.masterschool.com/store/favs |                                                                       |
| 2    | Klicke auf den Artikel "Garlic"         | Artikel wird angezeigt                      | OK        |                                                 |                                                                       |
| 3a   | Klicke auf 5 Sterne                     | 5 Sterne werden hellblau angezeigt          | ok        |                                                 |                                                                       |
| 3b   | Gebe "Very fresh quality, love it!" ein |                                             |           |                                                 |                                                                       |
| 3c   | Drücke Button "Send"                    | Zurück zum Artikel                          | OK        |                                                 |                                                                       |
| 4    | Prüfe Sterne                            | Bewertungsanzahl erhöht um 1 (count 11)     | OK        |                                                 |                                                                       |
| 5    | Prüfe Bewertungstext                    | Text wird unter meinem Namen angezeigt      | ***NOK*** | TBD                                             | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a8 |

---
## **Testfall 3: Produktbewertungssystem**

Ich möchte *keine* Sternebewertung abgeben und einen Bewertungstext hinzufügen.

| Step | Aktion                                                         | Erwartetes Ergebnis                         | OK/NOK    | URL                                             | Link to issue |
|------|----------------------------------------------------------------|---------------------------------------------|-----------|-------------------------------------------------|---------------|
| 1    | Klicke auf Button: Favoriten (Herz)                            | 3 soeben gekaufte Produkte werden angezeigt | OK        | https://grocerymate.masterschool.com/store/favs |               |
| 2    | Klicke auf den Artikel "Cauliflower"                           | Artikel wird angezeigt                      | OK        |                                                 |               |
| 3a   | Gebe "Ein Cauli war super, der andere war schon angewelkt" ein | Übernimmt Eingaben                          | OK        |                                                 |               |
| 3b   | Drücke Button "Send"                                           | Gibt kurz Fehlermeldung aus                 | OK        |                                                 |               |
| 3c   | Klicke auf 3 Sterne                                            | Übernimmt Eingabe                           | OK        |                                                 |               |
| 4    | Drücke Button "Send"                                           | Übernimmt Eingabe                           | OK        |                                                 |               |
| 5    | Prüfe Sterne                                                   | Bewertungsanzahl erhöht um 1 (Count 6)      | OK        |                                                 |               |
| 6    | Prüfe Bewertungstext                                           | Text wird unter meinem Namen angezeigt      | ***NOK*** | TBD                                             |               |

---

## **Testfall 4: Altersverifikation für alkoholische Getränke**

Aufruf von Shop https://grocerymate.masterschool.com/
Erstelle neuen account:
Full name: exact19 / 
email: exact19@web.de / 
PW: qwertz /
Status1: erfolgreich registriert (PopUp: Registrierung erfolgreich)
Status2: erfolgreich eingeloggt

Ich überprüfe die Kontoerstellung für einen Benutzer, der **genau 18 Jahre** alt ist.

| Step | Aktion                             | Erwartetes Ergebnis      | OK/NOK | URL                                            | Link to issue |
|------|------------------------------------|--------------------------|--------|------------------------------------------------|---------------|
| 1    | Klicke auf Shop (Home)             | Site Shop wird angezeigt | OK     | https://grocerymate.masterschool.com/store     |               |
| 2a   | Gebe Geb. Datum ein: "27-11-2006"  |                          |        |                                                |               |
| 2b   | Klicke auf "confirm"               |                          | OK     |                                                |               |
| 3    | Klicke auf die Kategorie "Alcohol" | Access                   | OK     |                                                |               |


---

## **Testfall 5: Altersverifikation für alkoholische Getränke**

Aufruf von Shop https://grocerymate.masterschool.com/
Erstelle neuen account:
Full name: justunder18 / 
email: justunder18@web.de / 
PW: qwertz /
Status1: erfolgreich registriert (PopUp: Registrierung erfolgreich)
Status2: erfolgreich eingeloggt

Ich überprüfe die Kontoerstellung für einen Benutzer, der **knapp unter 18 Jahre** alt ist.


| Step | Aktion                             | Erwartetes Ergebnis                | OK/NOK | URL                                          | Link to issue |
|------|------------------------------------|------------------------------------|--------|----------------------------------------------|---------------|
| 1    | Klicke auf Shop                    | Alters Verifikation wird angezeigt | OK     | https://grocerymate.masterschool.com/store   |               |
| 2a   | Gebe Geb. Datum ein: "28-11-2007"  |                                    |        |                                              |               |
| 2b   | Klicke auf "confirm"               | Anzeige: "You are underage"        | OK     |                                              |               |
| 3    | Klicke auf die Kategorie "Alcohol" | Anzeige: "No products found"       | OK     |                                              |               |


---
## **Testfall 6: Altersverifikation für alkoholische Getränke**

Erstelle neuen account:
Full name: under18 / 
email: under18@web.de / 
PW: qwertz /
Status1: erfolgreich registriert (PopUp: Registrierung erfolgreich)
Status2: erfolgreich eingeloggt

Ich überprüfe die Kontoerstellung für einen Benutzer, der **unter 18 Jahre** alt ist.

| Step | Aktion                                              | Erwartetes Ergebnis                | OK/NOK | URL                                          | Link to issue |
|------|-----------------------------------------------------|------------------------------------|--------|----------------------------------------------|---------------|
| 1    | Klicke auf Shop                                     | Alters Verifikation wird angezeigt | OK     | https://grocerymate.masterschool.com/store   |               |
| 2a   | Gebe Geb. Datum ein: "27-11-2008"                   |                                    |        |                                              |               |
| 2b   | Klicke auf "confirm"                                | Anzeige: "You are underage"        | OK     |                                              |               |
| 3    | Klicke auf die Kategorie "Alcohol"                  | Anzeige: "No products found"       | OK     |                                              |               |

---

## **Testfall 7: Änderungen der Versandkosten**

Login: exact19

Ich überprüfe die Versandkosten, wenn die Warensumme genau **auf** der Grenze 20€ liegt.
Zusätzlich prüfe ich die Versandkosten, wenn die Menge auf unter 20€ verringert wird.

| Step | Aktion                                             | Erwartetes Ergebnis     | OK/NOK    | URL | Link to issue |
|------|----------------------------------------------------|-------------------------|-----------|-----|---------------|
| 1    | Klicke auf Artikel: "Gala Apples" 1x "Add to Cart" |                         |           |     |               |
| 2    | Klicke auf Button: "+" 9x                          | Zeigt Versandkosten: 0€ | OK        |     |               |
| 3    | Klicke auf Button "-" 3x                           | Zeigt Versandkosten: 0€ | ***NOK*** |     | TBD           |


Bild3: Warenkorb mit 0€ Versandkosten
Bild4: Warenkorb unter 20€

---

## **Testfall 8: Änderungen der Versandkosten**

Login: exact19

Ich überprüfe die Versandkosten, wenn die Warensumme geringfügig **unter** der Grenze 20€ liegt.

| Step | Aktion                                            | Erwartetes Ergebnis               | OK/NOK | URL | Link to issue |
|------|---------------------------------------------------|-----------------------------------|--------|-----|---------------|
| 1    | Klicke auf Category: Fresh Vegetables             |                                   |        |     |               |
| 2a   | Klicke auf Button: 9x up "Gala Apples"            | Count 9                           | OK     |     |               |
| 2a   | Klicke auf Button: "Add to Cart"  "Gala Apples"   | Add to Cart                       | OK     |     |               |
| 3    | Klicke auf Button: "Add to Cart" 1x "Galia Melon" | Add to Cart                       | OK     |     |               |
| 2b   | Klicke auf "Warenkorb"                            | 19.80€ + 5€                       | OK     |     |               |
| 3    | Klicke auf "Warenkorb"                            | Zeigt für Summe: 5€ Versandkosten | OK     |     |               |

Bild3: Warenkorb mit 5€ Versandkosten

---

## **Testfall 9: Änderungen der Versandkosten**

Login: exact19

Ich überprüfe die Versandkosten, wenn die Warensumme geringfügig **über** der Grenze 20€ liegt.

| Step | Aktion                             | Erwartetes Ergebnis               | OK/NOK | URL | Link to issue |
|------|------------------------------------|-----------------------------------|--------|-----|---------------|
| 1    | Klicke auf Artikel: "Corona Extra" |                                   |        |     |               |
| 2a   | Klicke auf Button: "Add to Cart"   | Add to Cart                       | OK     |     |               |
| 2b   | Klicke auf Button: "Add to Cart"   | Add to Cart                       | OK     |     |               |
| 3    | Klicke auf "Warenkorb"             | Zeigt für Summe: 0€ Versandkosten | OK     |     |               |

Bild3: Warenkorb mit 0€ Versandkosten

---


