from tasks.zad_6 import word_frequencies


def test_word_frequencies_6_words() -> None:
    assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}


def test_word_frequencies_duplicated_words() -> None:
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty_text() -> None:
    assert word_frequencies("") == {}


def test_word_frequencies_duplicated_words_3_times() -> None:
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_correct_handle_dots_comma() -> None:
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2, "kot": 1, "kota": 1, "a": 1, "ale": 1}
