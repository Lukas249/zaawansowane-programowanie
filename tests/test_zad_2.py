from tasks.zad_2 import fibonacci


def test_0_fibonacci() -> None:
    assert fibonacci(0) == 0


def test_1_fibonacci() -> None:
    assert fibonacci(1) == 1


def test_5_fibonacci() -> None:
    assert fibonacci(5) == 5


def test_10_fibonacci() -> None:
    assert fibonacci(10) == 55


def test_minus_1_fibonacci() -> None:
    assert fibonacci(-1) is None
