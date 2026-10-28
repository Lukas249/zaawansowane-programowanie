from tasks.zad_1 import is_palindrome


def test_is_palindrome() -> None:
    assert is_palindrome("kajak") is True


def test_is_palindrome_with_spaces_and_upper_char() -> None:
    assert is_palindrome("Kobyła ma mały bok") is True


def test_is_not_palindrome() -> None:
    assert is_palindrome("python") is False


def test_is_not_palindrome_empty_string() -> None:
    assert is_palindrome("") is False


def test_is_palindrome_one_char() -> None:
    assert is_palindrome("A") is True
