from models.utils.flatten_list import flatten_list


def test_function():
    entry = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10]]
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatten_list(entry) == expected
