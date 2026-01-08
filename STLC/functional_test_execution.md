# 1. Produktbewertungssystem
---
# Testfall 1 - Bewertung mit kleinstmöglichem Wert

    import unittest

    def submit_rating(stars: int) -> int:
        """
        Beispiel-Funktion: verarbeitet die Bewertung.
        Gibt die Anzahl der Sterne zurück, die angezeigt werden sollen.
        Akzeptierte Werte: 1 bis 5 Sterne.
        """
        if stars < 1:
            raise ValueError("Bewertung muss mindestens 1 Stern sein.")
        if stars > 5:
            raise ValueError("Bewertung darf höchstens 5 Sterne sein.")
        return stars

    class TestRatingBoundaryValue(unittest.TestCase):

        def test_minimum_star_rating(self):
            """
            Grenzwertanalyse: Bewertung mit kleinstmöglichem Wert.
            Eingabe: 1 Stern
            Erwartetes Ergebnis: 1 Stern wird angezeigt.
            """
            stars_input = 1
            displayed_stars = submit_rating(stars_input)
            self.assertEqual(displayed_stars, 1, "Bei Eingabe von 1 Stern sollte genau 1 Stern angezeigt werden.")

    if __name__ == "__main__":
        unittest.main()

- test_product_review.py::TestRatingBoundaryValue::test_minimum_star_rating PASSED [100%]        
---
# Testfall 2 - Eingabe von Bewertungstext
        import unittest

        def submit_review(text: str) -> str:
        """
        Beispiel-Funktion: verarbeitet die Texteingabe einer Bewertung.
        Gibt den Text zurück, der angezeigt werden soll.
        """
            if not text:
                raise ValueError("Der Bewertungstext darf nicht leer sein.")
            return text


        class TestReviewText(unittest.TestCase):

        def test_lobender_text(self):
            """
            Grenzwertanalyse: Eingabe von Bewertungstext.
            Eingabe: lobender Text
            Erwartetes Ergebnis: Texteingabe wird angezeigt.
            """
            review_text = "Das Produkt ist großartig und ich bin sehr zufrieden!"
            displayed_text = submit_review(review_text)
            self.assertEqual(
                displayed_text,
                review_text,
                "Der eingegebene Bewertungstext sollte korrekt angezeigt werden.")


        if __name__ == "__main__":
        unittest.main()

- test_product_review.py::TestRatingBoundaryValue::test_minimum_star_rating PASSED [100%]
---
# Testfall 3 - Bewertung mit Stern(en) wird nicht abgegeben
        import unittest

        def submit_rating(stars: int, current_counter: int) -> int:
        """
        Beispiel-Funktion: verarbeitet die Sternebewertung.
        - Bei 0 Sternen: Fehlermeldung, Counter bleibt unverändert.
        - Bei 1-5 Sternen: Counter wird auf die eingegebenen Sterne gesetzt.
           """
            if stars < 1:
                raise ValueError("Fehlermeldung: Sie müssen mindestens 1 Stern vergeben.")
            if stars > 5:
                raise ValueError("Bewertung darf höchstens 5 Sterne sein.")
            return stars  # Counter aktualisiert


        class TestRatingZeroStars(unittest.TestCase):

        def test_zero_star_rating(self):
            """
            Grenzwertanalyse: Bewertung mit 0 Sternen.
            Erwartetes Ergebnis: Fehlermeldung, Counter bleibt unverändert.
            """
            current_counter = 3  # Beispiel: bisher 3 Sterne

        with self.assertRaises(ValueError) as context:
            submit_rating(0, current_counter)

        self.assertIn(
            "Fehlermeldung",
            str(context.exception),
            "Bei 0 Sternen sollte eine Fehlermeldung angezeigt werden.")

        # Counter darf unverändert bleiben
        self.assertEqual(
            current_counter,
            3, "Der Counter darf sich nicht verändern, wenn 0 Sterne eingegeben werden.")


        if __name__ == "__main__":
            unittest.main()

- test_product_review.py::TestRatingBoundaryValue::test_minimum_star_rating PASSED [100%]
---
# 2. Altersverifikation für alkoholische Produkte
---
# Testfall 4 - genau 18J

        import unittest
        from datetime import date


        def can_create_account(birthdate: date) -> bool:
        """Beispielfunktion: gibt True zurück, wenn Benutzer >= 18 Jahre alt ist."""
            today = date.today()
            age = today.year - birthdate.year

        """Wenn Geburtsdatum dieses Jahr noch nicht erreicht → ein Jahr abziehen"""
            if (today.month, today.day) < (birthdate.month, birthdate.day):
                age -= 1
            return age >= 18


        class TestAccountCreationBoundary(unittest.TestCase):

        def test_exact_18_years_old(self):
            """Benutzer ist heute genau 18 Jahre alt -> Kontoerstellung erlaubt."""

            today = date.today()
            birthdate_18 = date(today.year - 18, today.month, today.day)

            result = can_create_account(birthdate_18)

            self.assertTrue(
                result,
                     "Ein Benutzer, der heute genau 18 Jahre alt wird, sollte ein Konto erstellen können.")


        if __name__ == "__main__":
            unittest.main()


- test_age_verification.py::TestAccountCreationBoundary::test_under_18_by_one_day PASSED [ 50%]
- test_age_verification.py::TestAccountCreationEquivalence::test_under_18_equivalence_class PASSED [100%]

---
# Testfall 5 - knapp unter 18J
        import unittest
        from datetime import date, timedelta


        def can_create_account(birthdate: date) -> bool:
        """Beispielfunktion: gibt True zurück, wenn Benutzer >= 18 Jahre alt ist."""
            today = date.today()
            age = today.year - birthdate.year

        """Wenn Geburtsdatum dieses Jahr noch nicht erreicht → ein Jahr abziehen"""
            if (today.month, today.day) < (birthdate.month, birthdate.day):
             age -= 1

            return age >= 18


        class TestAccountCreationBoundary(unittest.TestCase):

        def test_under_18_by_one_day(self):
            """
            Benutzer ist knapp unter 18 (wird erst morgen 18).
            Erwartet: Konto darf NICHT erstellt werden.
             """

            today = date.today()

        # Geburtstagsdatum = heute - 18 Jahre + 1 Tag (also morgen 18)
            birthdate_under_18 = date(today.year - 18, today.month, today.day) + timedelta(days=1)

        result = can_create_account(birthdate_under_18)

        self.assertFalse(
            result,
            "Ein Benutzer, der erst morgen 18 wird, darf kein Konto erstellen.")


        if __name__ == "__main__":
     unittest.main()

- test_age_verification.py::TestAccountCreationBoundary::test_under_18_by_one_day PASSED [ 50%]
- test_age_verification.py::TestAccountCreationEquivalence::test_under_18_equivalence_class PASSED [100%]

---
# Testfall 6 - unter 18J
        import unittest
        from datetime import date


        def can_create_account(birthdate: date) -> bool:
        """Beispielfunktion: gibt True zurück, wenn Benutzer >= 18 Jahre alt ist."""
        today = date.today()
        age = today.year - birthdate.year

        # Wenn Geburtsdatum dieses Jahr noch nicht erreicht → ein Jahr abziehen
            if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        return age >= 18


        class TestAccountCreationEquivalence(unittest.TestCase):

        def test_under_18_equivalence_class(self):
            """
        Äquivalenzklassenanalyse:
        Benutzer unter 18 Jahren (repräsentatives Beispiel: 17 Jahre alt).
        Erwartet: Kontoerstellung NICHT erlaubt.
            """

            today = date.today()

        # Benutzer ist genau 17 Jahre alt
            birthdate_17 = date(today.year - 17, today.month, today.day)

        result = can_create_account(birthdate_17)

        self.assertFalse(
            result,
            "Ein Benutzer, der 17 Jahre alt ist, darf kein Konto erstellen.")


        if __name__ == "__main__":
            unittest.main()

- test_age_verification.py::TestAccountCreationBoundary::test_under_18_by_one_day PASSED [ 50%]
- test_age_verification.py::TestAccountCreationEquivalence::test_under_18_equivalence_class PASSED [100%]

---

# 3. Änderungen der Versandkosten
---
# Testfall 7 - Warensumme liegt genau auf der Grenze
        import unittest

    def calculate_shipping(total_amount: float) -> float:
        """
        Beispiel-Funktion: Berechnet die Versandkosten.
        - Ab 20 €: keine Versandkosten
        - Unter 20 €: Versandkosten 5 €
        """
        if total_amount >= 20:
            return 0.0
        return 5.0


    class TestShippingBoundaryValue(unittest.TestCase):

        def test_shipping_cost_at_threshold(self):
            """
            Grenzwertanalyse: Warensumme genau auf der Grenze.
            Eingabe: 20 €
            Erwartetes Ergebnis: Es fallen keine Versandkosten an.
            """
            total = 20.0
            shipping_cost = calculate_shipping(total)
            self.assertEqual(
                shipping_cost,
                0.0,
                "Bei einer Warensumme von 20 € dürfen keine Versandkosten anfallen.")


    if __name__ == "__main__":
        unittest.main()

- test_product_review.py::TestShippingBoundaryValue::test_shipping_cost_at_threshold PASSED [100%]
---
# Testfall 8 - Warensumme liegt knapp unter Grenze
        import unittest

    def calculate_shipping(total_amount: float) -> float:
        """
        Beispiel-Funktion: Berechnet die Versandkosten.
        - Ab 20 €: keine Versandkosten
        - Unter 20 €: Versandkosten 5 €
        """
        if total_amount >= 20:
            return 0.0
        return 5.0


    class TestShippingBoundaryValue(unittest.TestCase):

        def test_shipping_cost_just_below_threshold(self):
            """
            Grenzwertanalyse: Warensumme leicht unter der Grenze.
            Eingabe: 19.90 €
            Erwartetes Ergebnis: Es fallen Versandkosten an.
            """
            total = 19.90
            shipping_cost = calculate_shipping(total)
            self.assertEqual(
                shipping_cost,
                5.0,
                "Bei einer Warensumme von 19,90 € müssen Versandkosten von 5 € berechnet werden.")


    if __name__ == "__main__":
        unittest.main()

- test_product_review.py::TestShippingBoundaryValue::test_shipping_cost_just_below_threshold PASSED [100%]
---
# Testfall 9 - Warensumme liegt stark über der Grenze
    import unittest

    def calculate_shipping(total_amount: float) -> float:
        """
        Berechnet die Versandkosten.
        - Ab 20 €: keine Versandkosten
        - Unter 20 €: Versandkosten 5 €
     """
        if total_amount >= 20:
            return 0.0
        return 5.0


    class TestShippingAboveThreshold(unittest.TestCase):

        def test_shipping_cost_for_33_euro(self):
            """
            Grenzwertanalyse: Warensumme = 33 €
            Erwartetes Ergebnis: Es fallen keine Versandkosten an.
            """
            total = 33.0
            shipping_cost = calculate_shipping(total)
            self.assertEqual(
                shipping_cost,
                0.0,
                "Bei einer Warensumme von 33 € dürfen keine Versandkosten anfallen.")


    if __name__ == "__main__":
        unittest.main()

- test_product_review.py::TestShippingAboveThreshold::test_shipping_cost_for_33_euro PASSED [100%]
---