from src.Practice.prac8.hashtable import *
import pytest


def dummy_hashtable(elements):
    hashtable = create_hashtable()
    for i in elements:
        put(hashtable, i[0], i[1])
    return hashtable


def test_create_hashtable():
    test_hashtable = create_hashtable()
    assert (
        test_hashtable.capacity == 1024
        and len(test_hashtable.table) == 1024
        and test_hashtable.size == 0
    )


def test_delete_hashtable():
    test_hashtable = create_hashtable()
    test_hashtable = delete_hashtable(test_hashtable)
    assert test_hashtable is None


@pytest.mark.parametrize(
    "elements, put_element, expected",
    (
        (((1, 1), (2, 2), (3, 3)), (15, 15), [(1, 1), (2, 2), (3, 3), (15, 15)]),
        (
            ((1, 1), (2, 2), (3, 3)),
            ("Noneisnotnone", None),
            [(1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)],
        ),
    ),
)
def test_put(elements, put_element, expected):
    test_hashtable = dummy_hashtable(elements)
    put(test_hashtable, *put_element)
    assert items(test_hashtable) == expected


@pytest.mark.parametrize(
    "elements, remove_key, expected",
    (
        (((1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)), "Noneisnotnone", None),
        (((1, 1), (2, 2), (3, 3), (15, 15)), 2, 2),
    ),
)
def test_remove(elements, remove_key, expected):
    test_hashtable = dummy_hashtable(elements)
    assert remove(test_hashtable, remove_key) == expected


@pytest.mark.parametrize(
    "elements, find_key, expected",
    (
        (((1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)), "Noneisnotnone", True),
        (((1, 1), (2, 2), (3, 3), (15, 15)), 2, True),
        (((20, 20), (30, 30)), 15, False),
    ),
)
def test_has_key(elements, find_key, expected):
    test_hashtable = dummy_hashtable(elements)
    assert has_key(test_hashtable, find_key) == expected


@pytest.mark.parametrize(
    "elements, get_key, expected",
    (
        (((1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)), "Noneisnotnone", None),
        (((1, 1), (2, 2), (3, 3), (15, 15)), 2, 2),
        (((20, 20), (30, 30), (19, "Hi, world!")), 19, "Hi, world!"),
    ),
)
def test_get(elements, get_key, expected):
    test_hashtable = dummy_hashtable(elements)
    assert get(test_hashtable, get_key) == expected


@pytest.mark.parametrize(
    "elements, expected",
    (
        (
            ((1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)),
            [(1, 1), (2, 2), (3, 3), ("Noneisnotnone", None)],
        ),
        (((1, 1), (2, 2), (3, 3), (15, 15)), [(1, 1), (2, 2), (3, 3), (15, 15)]),
        (((20, 20), (30, 30)), [(20, 20), (30, 30)]),
    ),
)
def test_items(elements, expected):
    test_hashtable = dummy_hashtable(elements)
    assert items(test_hashtable) == expected


def test_remove_error():
    test_hashtable = create_hashtable()
    with pytest.raises(KeyError):
        assert remove(test_hashtable, 2) == KeyError


def test_get_error():
    test_hashtable = create_hashtable()
    with pytest.raises(KeyError):
        assert get(test_hashtable, 15) == KeyError
