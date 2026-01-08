## **Die Software**

--- 
Webshop: https://grocerymate.masterschool.com/
Webshop: https://grocerymate.masterschool.com/auth

Mit folgenden Basisfunktionen:

- Registrierung und Anmeldung
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Produktkategorisierung
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabwicklung: Rechnungs- und Lieferadresse eingeben, Zahlungsart auswählen, Gesamtbetrag berechnen

## **Neue Funktionen**

---

## **1. Product Rating System**

Nutzer sollen Produkte anhand eines 5-Sterne-Systems bewerten.

**Vage formulierte** Anforderung:
* Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Konkret formulierte** Anforderung:
* Wenn der Kauf des Produkts abgeschlossen ist, sollen Bewertungen zwischen 1 und 5 abgegeben werden können. 
Die abgegebene Bewertung soll allen Nutzern angezeigt werden, wenn der Artikel im Shop erneut angezeigt wird.
Der Nutzer darf eine abgegebene Bewertung löschen oder ändern. Das Feedbackfeld soll ein Pflichtfeld sein. 
Die Anzahl der Zeichen soll auf 50 Zeichen begrenzt sein.

---

## **2. Altersverifikation für alkoholische Produkte**

Alkoholische Produkte erfordern eine Altersverifikation. 

**Vage formulierte** Anforderung:
* Alkoholische Produkte erfordern eine Altersverifikation. 
Beim Aufrufen der Kategorie soll ein Modal erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

**Konkret formulierte** Anforderung:
* Nach Eingabe des Geburtstages TT/MM/JJJJ im Modal erfolgt die Altersberechnung. 
Nur wenn das errechnete Alter ≥ 18 Jahre ist, darf der Zugriff auf alkoholische Produkte erlaubt werden. 
Wenn das errechnete Alter von 18J unterschritten ist, wird der Zugriff auf alkoholische Getränke nicht erlaubt, 
andere Kategorien sind weiter im Zugriff. Falscheingaben lösen eine Fehlermeldung aus.

---

## **3. Änderungen der Versandkosten**

Für Bestellungen über einem bestimmten Wert entfallen die Versandkosten. Für Bestellungen unter diesem Wert fallen Versandkosten an.

**Vage formulierte** Anforderung:
* Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

**Konkret formulierte** Anforderung:
* Die Versandkosten entfallen ab einem Bestellwert von >= 20 €. 
Ist der Bestellwert < 20 €, so fällt eine Versandkostenpauschale an.