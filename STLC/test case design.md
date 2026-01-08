### **1. Produktbewertungssystem**

**Test Design Techniques:** Boundary Value Analysis (BVA)

### **Testfälle:**
**1. Grenzwertanalyse / Boundary Value Analysis:**
- Testfall: Bewertung mit kleinstmöglichem Wert.
- Eingabe: 1 Stern.
- Erwartetes Ergebnis: 1 Stern wird angezeigt.

**2. Grenzwertanalyse / Boundary Value Analysis:**
- Testfall: Eingabe von Bewertungstext.
- Eingabe: Lobender Text.
- Erwartetes Ergebnis: Texteingabe wird angezeigt.

**3. Grenzwertanalyse / Boundary Value Analysis:**
- Testfall: Bewertung mit Sternen wird nicht abgegeben.
- Eingabe: 0 Sterne.
- Erwartetes Ergebnis: Fehlermeldung. Keine Veränderung des Counters.

---

### **2. Altersverifikation für alkoholische Produkte**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP)

### **Testfälle:**
**4. Grenzwertanalyse / Boundary Value Analysis:**
- Testfall: Überprüfung der Kontoerstellung für einen Benutzer, der genau 18 Jahre alt ist.
- Eingabe: Geburtsdatum = (Heute 18 Jahre)
- Erwartetes Ergebnis: Kontoerstellung erfolgreich.

**5. Grenzwertanalyse: / Boundary Value Analysis**
- Testfall: Überprüfung der Kontoerstellung für einen Benutzer, der knapp unter 18 Jahre alt ist.
- Eingabe: Geburtsdatum = (Heute: 18 Jahre + 1 Tag)
- Erwartetes Ergebnis: Fehlermeldung „Sie müssen mindestens 18 Jahre alt sein, um ein Konto zu erstellen.“

**6. Äquivalenzklassenanalyse / Equivalence Partitioning:**
- Testfall: Überprüfung der Kontoerstellung für Benutzer unter 18 Jahren.
- Eingabe: Geburtsdatum = (Heute 17 Jahre)
- Erwartetes Ergebnis: Fehlermeldung wird angezeigt.


---
### **3. Änderungen der Versandkosten**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP)

### **Testfälle:**
**7. Grenzwertanalyse / Boundary Value Analysis:**
- Testfall: Warensumme liegt genau auf der Grenze
- Eingabe: 20 €
- Erwartetes Ergebnis: Es fallen **keine** Versandkosten an. 

**8. Grenzwertanalyse: / Boundary Value Analysis**
- Testfall: Warensumme liegt wenig unter der Grenze
- Eingabe: 19.90 € 
- Erwartetes Ergebnis: Es fallen Versandkosten an.

**9. Äquivalenzklassenanalyse / Equivalence Partitioning:**
- Testfall: Warensumme liegt stark über der Grenze
- Eingabe: 33 €
- Erwartetes Ergebnis: Es fallen **keine** Versandkosten an.
---