from tasks.zad_5 import flatten_list


def test_flatten_list_1d() -> None:
    assert flatten_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_flatten_list_3d() -> None:
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_list_empty_list() -> None:
    assert flatten_list([]) == []


def test_flatten_list_3d_one_value() -> None:
    assert flatten_list([[[1]]]) == [1]


def test_flatten_list_4d() -> None:
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
