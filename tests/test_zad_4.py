from tasks.zad_4 import calculate_discount

import pytest


def test_calculate_discount_100_20() -> None:
    assert calculate_discount(100, 0.2) == 80.0


def test_calculate_discount_50_0() -> None:
    assert calculate_discount(50, 0) == 50


def test_calculate_discount_200_1() -> None:
    assert calculate_discount(200, 1) == 0.0


def test_calculate_discount_100_minus_10() -> None:
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test_calculate_discount_100_15() -> None:
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)
