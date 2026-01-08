## **Testplan & Testfalldesign**

Dieser Testplan beschreibt die Teststrategie, Methoden und Testfälle eines Grocery-Stores.

**Testobjekt (zu testendes System):**

**Webshop: https://grocerymate.masterschool.com/**

---
## **1. Produktanalyse**

**Zielsetzung: Was ist das Ziel des Produkts?**

- Das Hauptziel des Produkts ist den Einkauf online einfacher und schneller zu machen. 
- Es soll den Alltag der Kunden erleichtern und Zeit sparen, indem dieser die Kunden täglich zuverlässig mit frischen Lebensmitteln beliefert. 
- Der Shop soll einen bequemen, schnellen und stressfreien Lebensmitteleinkauf ermöglichen. 
- Weitere Features sollen die Nutzerzahlen erhöhen, die Bestellfrequenz verbessern und den Einmalkunden zum Wiederholer machen.

**Zielgruppe (Stakeholder): Wer nutzt das Produkt? Wer sind die relevanten Stakeholder auf Nutzerseite?**

Das Produkt richtet sich z.B. an Personas wie:
- (Berufstätige Mutter): Die gestresst durch lange Arbeitszeiten und Haushalt selten Gelegenheit hat, ein Geschäft zu regulären Öffnungszeiten aufzusuchen.
- (Der digitale Native): Autoloser Stadtbewohner, der schwierige Parkplatzsituationen vorfindet und keinen Supermarktstress mag.
- (Das nachhaltige Paar): Ballungsraumbewohner mit besonderem Wunsch nach Bio-Produkten mit regionaler Herkunft und großem nachhaltigem Sortiment ohne Verpackung. 
- (PreAdults): Jugendliche, die noch <18 Jahre sind, den "Erwachsenen"-Lifestyle nachahmen durch das Bestellen von Snacks (Chips) und Getränken (Cola) ohne elterliche Aufsicht.

Im Test wähle ich z.B. ein Produkt, welches die Zielgruppe PreAdults gerne kauft und lege es in den Warenkorb. 
Ich füge evtl. noch ein weiteres Produkt hinzu. Im Warenkorb gehe ich zur Kasse und zahle mit meiner Karte. 
Dann werde ich aufgefordert eine Bewertung abzugeben und bewerte ein Produkt mit einem Stern und ein Weiteres mit 5 Sternen 
und füge jeweils einen kleinen Kommentar hinzu. Im Anschluss rufe ich den gekauften Artikel wieder auf und prüfe, 
ob meine beiden Bewertungen und Kommentare sichtbar und bei den richtigen Artikeln erscheinen. 
Für die Prüfung dieser Funktionen habe ich mich für die BVA Methoden entschieden.


**Hardware- und Software-Spezifikationen:** Es werden Geräte mit Standardkonfigurationen verwendet.

**Hardware-Anforderungen:**

- Geräte: PCs, Laptops, Smartphones, Tablets
- Mindestanforderungen: 4 GB RAM, 2-GHz-Prozessor

**Software-Anforderungen:**

- Betriebssysteme: Windows, macOS, Android, iOS
- Browser: Chrome, Firefox, Safari, Edge
- Abhängigkeiten: Backend-Dienste, Werbedienste von Drittanbietern, Zahlungsanbieter

Welche Funktionen bietet das Produkt?

**Bestehende Funktionen:**
- Registrierung und Anmeldung
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Produktkategorisierung
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabwicklung: Rechnungs- und Lieferadresse eingeben, Zahlungsmethode auswählen, Gesamtbetrag berechnen

**Geplante Funktionen:**
- Produktbewertungssystem
- Altersverifizierung für alkoholische Getränke
- Änderungen der Versandkosten
---

## **2. Entwurf der Teststrategie**
**Testumfang: (Testumfang)**

**Im Umfang enthalten:**

- Altersbeschränkung für die Kontoerstellung
- Alterseingabe- und Freigabeprozess
- Hinzufügen von Produkten zum Warenkorb
- Berechnung und Änderung der Versandkosten
- Product Rating System
- Altersverifikation für alkoholische Produkte

**Nicht im Umfang enthalten:**

- Backend-Datenbankoperationen
- UI-Funktionen
- Security Tests
- Nicht-funktionale Tests

**Geplante Testarten:**

- Funktionstests
- Regressionstests
- Usability-Tests

**Risiken, Probleme und Gegenmaßnahmen:**

**Entwicklungsverzögerungen**
- Gegenmaßnahme: Pufferzeit einplanen

**Fehlende Testdaten**
- Gegenmaßnahme: Testdaten (Mock-Daten) erstellen

**Ressourcenengpässe**

- Gegenmaßnahme: Ersatzpersonal identifizieren und einplanen

**Testlogistik (Testverantwortlichkeiten):**

- Testmanager: Thomas Breckenfelder
- QA-Ingenieur (Funktion & Regression): Thomas Breckenfelder
- QA-Ingenieur (Usability): Thomas Breckenfelder
- Endnutzer für UAT (Benutzerakzeptanztest): PB

---

## **3. Definition der Testziele**
**Ziele:**

- **Funktionalität:** Sicherstellen, dass neue Funktionen wie vorgesehen funktionieren.


**Erwartete Ergebnisse:**

- Hinzugefügte Funktionen verhalten sich gemäß der Spezifikation.

- Fehlerhafte Benutzereingaben werden entsprechend angezeigt.

---

## **4. Definition der Testkriterien**
**Abbruchkriterien:**

- **Alle geplanten Tests** wurden ausgeführt.

- **Ausführungsrate**: 100 % aller Testfälle wurden ausgeführt.

- **Erfolgsrate**: Mindestens 90 % der ausgeführten Testfälle wurden bestanden.

- Alle kritischen und hoch priorisierten Fehler wurden behoben.

- Der Benutzerakzeptanztest (UAT) wurde abgeschlossen und freigegeben.

**Abbruchkriterien:**

- Kritische Fehler, die die Fortsetzung der Tests verhindern (Schweregrad 1).

- Ausfall der Testumgebung (Server, Datenbankzugriff).

- Fehlende Ressourcen (Tools, Hardware, Personal).

**Fortsetzungskriterien:**

- Freigabe erteilt.
- Die benötigten Tools und das Personal sind wieder verfügbar.

- Die erforderlichen Testdaten wurden erstellt, korrigiert oder aktualisiert.

---

## **5. Ressourcenplanung**

- **Personal**: QA-Team, Entwicklungsteam, Endbenutzer für UAT
- **Hardware:** PCs, Laptops, Tablets, Smartphones
- **Software:** Gängige Browser (Chrome, Firefox, Safari, Edge), Betriebssysteme (Windows, macOS, Android, iOS)

- **Infrastruktur:** Testumgebungen, Automatisierungstools
---

## **6. Testumgebung planen**
**Testgeräte**: Realgeräte mit echten Betriebssystemen und Browsern zur realitätsnahen Simulation
- **Hardware1:** MacBook Air 13“/16GB/256GB
- Betriebssystem: Sequoia 15.6.1
- Browser: Chrome für Mac

**Umgebungen:**
- Entwicklung (DEV)
- TEST (Test)
- Abnahme (ACC - Acceptance)

---

## **7. Zeitplan und Aufwandsschätzung**


| Aktivität                                        | Startdatum | Enddatum  | Umgebung | Verantwortlich | Geplanter Aufwand |
|--------------------------------------------------|------------|-----------| -------- |----------------|-------------------|
| Testplanung                                      | 06.11.2025 | 11.11.2025 | Alle     | TB             | 7 Stunden         |
| Testfalldesign                                   | 12.11.2025 | 12.11.2025 | Alle     | TB             | 7 Stunden         |
| Unittest (nur Erweiterungen)                     | 13.11.2025 | 13.11.2025 | TEST     | TB             | 7 Stunden         |
| Integrationstest (Zusammenspiel der neuen Module) | 14.11.2025 | 14.11.2025| TEST     | TB             | 5 Stunden         |
| Systemtest                                       | 17.11.2025 | 17.11.2025 | TEST     | TB             | 7 Stunden         |
| Teil-Regressions-Test (von Änderungen betroffen) | 18.11.2025 | 18.11.2025 | ACC      | TB             | 3 Stunden         |
| Abnahmetest (UAT)                                | 18.11.2025 | 18.11.2025 | TEST     | PB             | 2 Stunden         |
| Dokumentation                                    | 19.11.2025 | 19.11.2025 | ACC      | TB             | 2 Stunden         |

------------------------------------

## **8. Testergebnisse festlegen**

Dokumente/Tools, die zur Unterstützung der Testaktivitäten im Projekt erstellt werden müssen:

- Testplan / test plan (GitHub)
- Testfälle und Testskripte / test case design (GitHub)
- Testdaten / functional test execution (GitHub)
- Testberichte / test reporting (GitHub)
- Fehlerberichte (GitHub)
- Abnahmedokument für Benutzertests (GitHub)
  (Ende)