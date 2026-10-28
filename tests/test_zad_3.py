from tasks.zad_3 import count_vowels


def test_count_vowels_python() -> None:
    assert count_vowels("Python") == 2


def test_count_vowels_AEIOUY() -> None:
    assert count_vowels("AEIOUY") == 6


def test_count_vowels_bcd() -> None:
    assert count_vowels("bcd") == 0


def test_count_vowels_empty() -> None:
    assert count_vowels("") == 0


def test_count_vowels_long_text() -> None:
    assert count_vowels("Próba żółwia") == 4
