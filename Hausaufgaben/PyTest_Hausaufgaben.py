import pytest

# Übung 1: Basis-Tests mit Parametrisierung

# Ich nutze Parametrisierung, um `count_word_matches` mit mehreren Eingabekombinationen aus `text` und `target`
# sowie den erwarteten Ausgaben zu testen.

# Ich schreibe einen parametrisierten Test, um die Funktion für einfache,
# gemischte und einfache Randfallszenarien zu validieren.

# Implementierung

def count_word_matches(text, target):
#     """
#     Zählt, wie oft ein Zielwort als eigenständiges Wort im Text vorkommt.
#     Die Übereinstimmung erfolgt ohne Berücksichtigung der Groß-/Kleinschreibung,
#     und Wörter sind durch Leerzeichen getrennt.

#  Args:
#      text (str): Eingabetext, in dem gesucht wird.
#      target (str): Das gesuchte Wort.

#  Returns:
#      int: Anzahl der Vorkommen des Zielwortes als eigenständiges Wort.

#     """
    if not text or not target:
        return 0

# Text in Wörter aufteilen und für case-insensitive Vergleich in Kleinbuchstaben umwandeln
    words = text.lower().split()
    target = target.lower()

# Eigenständige Vorkommen des Zielwortes zählen
    return words.count(target)
#----------------------------------------

# Übung 1

# Testfälle:

# 1. `text="The cat sat on the mat"`, `target="cat"` → Erwartet: 1 *(Nur „cat“ zählt, nicht „cat“ in „concatenate“)*
# 2. `text="Dog dog DOG dOg"`, `target="dog"` → Erwartet: 4 *(Groß-/Kleinschreibung ignoriert)*
# 3. `text="Hello world"`, `target="world"` → Erwartet: 1
# 4. `text="hello hello HELLO"`, `target="hello"` → Erwartet: 3
# 5. `text="No matches here"`, `target="yes"` → Erwartet: 0 *(Keine Übereinstimmungen)*
# 6. `text="catcat cat catdog"`, `target="cat"` → Erwartet: 1 *(Nur eigenständiges „cat“ zählt)*
# 7. `text="a a a"`, `target="a"` → Erwartet: 3


@pytest.mark.parametrize("text,target,expected",
    [
        ("The cat sat on the mat", "cat", 1),   #1
        ("Dog dog DOG dOg", "dog", 4),          #2
        ("Hello world", "world", 1),            #3
        ("hello hello HELLO", "hello", 3),      #4
        ("No matches here", "yes", 0),          #5
        ("catcat cat catdog", "cat", 1),        #6
        ("a a a", "a", 3),                      #7
    ]
)

def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected

#---------------------test session 1------------------------------
#collecting ... collected 7 items

# PyTest_Hausaufgaben.py::test_count_word_matches_basic[The cat sat on the mat-cat-1] PASSED [ 14%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[Dog dog DOG dOg-dog-4] PASSED [ 28%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[Hello world-world-1] PASSED [ 42%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[hello hello HELLO-hello-3] PASSED [ 57%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[No matches here-yes-0] PASSED [ 71%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[catcat cat catdog-cat-1] PASSED [ 85%]
# PyTest_Hausaufgaben.py::test_count_word_matches_basic[a a a-a-3] PASSED  [100%]

#----------------------------------------------------

# Übung 2: Testen von Randfällen (Edge Case Testing)

# Ich erstelle ein Fixture, das häufige Randfall-Eingaben bereitstellt,
# und teste die Funktion mit parametrisierten Tests.
# Ich fokussiere auf leere Eingaben, Leerzeichen und Interpunktion.

# Testfälle:

#1. Leerer Text: `text=""`, `target="word"` → Erwartet: 0
#2. Leeres Zielwort: `text="hello world"`, `target=""` → Erwartet: 0
#3. Beides leer: `text=""`, `target=""` → Erwartet: 0
#4. Mehrere Leerzeichen: `text="hello world"`, `target="world"` → Erwartet: 1 *(Zusätzliche Leerzeichen ignoriert)*
#5. Führende/nachgestellte Leerzeichen: `text=" cat "`, `target="cat"` → Erwartet: 1
#6. Satzzeichen nicht als Trennzeichen behandelt: `text="cat,dog cat"`, `target="cat"` → Erwartet: 1
#7. Einzelzeichen: `text="x y z"`, `target="x"` → Erwartet: 1

@pytest.fixture
def edge_cases():
    return [
        ("", "word", 0),                # Text: leer
        ("hello world", "", 0),         # Target: leer
        ("", "", 0),                    # Text & Target: leer
        ("hello   world", "world", 1),  # Leerzeichen mehrfach
        ("  cat  ", "cat", 1),          # Leerzeichen
        ("cat,dog cat", "cat", 1),      # Satzzeichen mit fehlendem Trenner
        ("x y z", "x", 1),              # Einzelzeichen
    ]


@pytest.mark.parametrize("text,target,expected", [
    ("", "word", 0),                #1
    ("hello world", "", 0),         #2
    ("", "", 0),                    #3
    ("hello   world", "world", 1),  #4
    ("  cat  ", "cat", 1),          #5
    ("cat,dog cat", "cat", 1),      #6
    ("x y z", "x", 1),              #7
])
def test_count_word_matches_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected

#----------------test session 2----------------------------------
# collecting ... collected 7 items

# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[-word-0] PASSED [ 14%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[hello world--0] PASSED [ 28%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[--0] PASSED   [ 42%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[hello   world-world-1] PASSED [ 57%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[  cat  -cat-1] PASSED [ 71%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[cat,dog cat-cat-1] PASSED [ 85%]
# PyTest_Hausaufgaben.py::test_count_word_matches_edge_cases[x y z-x-1] PASSED [100%]
#--------------------------------------------------

# Übung 3: Negativtests (Negative Testing)

# Ich teste die Funktion auf ungültige Eingaben wie `None`, Ganzzahlen oder Listen,
# um sicherzustellen, dass sie die entsprechenden Ausnahmen (Exceptions) auslöst.
# Ich verwende ein Fixture, um Testfälle für ungültige Eingaben bereitzustellen.

# Testfälle:

# 1. Text = `None`, Zielwort = `"word"` → Erwartet: 0
# 2. Text = `"hello world"`, Zielwort = `None` → Erwartet: 0
# 3. Text = `123`, Zielwort = `"word"` → Erwartet: AttributeError
# 4. Text = `"hello world"`, Zielwort = `456` → Erwartet: AttributeError
# 5. Text = `["hello", "world"]`, Zielwort = `"world"` → Erwartet: AttributeError
# 6. Text = `"hello world"`, Zielwort = `["world"]` → Erwartet: AttributeError

@pytest.fixture
def invalid_inputs():
    return [
        (None, "word", 0),                              # Text == None -> Funktion gibt 0 zurück
        ("hello world", None, 0),                       # Target == None -> Funktion gibt 0 zurück
        (123, "word", AttributeError),                  # Text: kein String -> AE
        ("hello world", 456, AttributeError),           # Target: kein String -> AE
        (["hello", "world"], "world", AttributeError),  # Text ist Liste -> AE
        ("hello world", ["world"], AttributeError),     # Target ist Liste -> AE
    ]

@pytest.mark.parametrize("text,target,expected",
[
    (None, "word", 0),                                  #1
    ("hello world", None, 0),                           #2
    (123, "word", AttributeError),                      #3
    ("hello world", 456, AttributeError),               #4
    (["hello", "world"], "world", AttributeError),      #5
    ("hello world", ["world"], AttributeError),         #6
])

def test_count_word_matches_invalid_inputs(text, target, expected):
    if expected is AttributeError:
        with pytest.raises(AttributeError):
            count_word_matches(text, target)
    else:
        assert count_word_matches(text, target) == expected

#----------------------test session 3-----------------------
# collecting ... collected 6 items

# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[None-word-0] PASSED [ 16%]
# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[hello world-None-0] PASSED [ 33%]
# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[123-word-AttributeError] PASSED [ 50%]
# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[hello world-456-AttributeError] PASSED [ 66%]
# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[text4-world-AttributeError] PASSED [ 83%]
# PyTest_Hausaufgaben.py::test_count_word_matches_invalid_inputs[hello world-target5-AttributeError] PASSED [100%]

