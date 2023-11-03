from src.Practice.prac7.BST import *
import pytest


def dummy_bst(elements: tuple):
    map = create_tree_map()
    for i in elements:
        put(map, i[0], i[1])
    return map


def test_create_tree_map():
    map_example = create_tree_map()
    assert map_example == Tree(None)


@pytest.mark.parametrize(
    "elements",
    [
        ((1, 1), (3, 3), (2, 2), (4, 4)),
        (()),
    ],
)
def test_delete_tree_map(elements):
    map = dummy_bst(elements)
    delete_tree_map(map)
    assert map.root is None


@pytest.mark.parametrize(
    "elements,order,expected",
    [
        (((15, 15), (6, 6), (1, 1), (12, 12)), "inorder", [15, 6, 1, 12]),
        (((15, 15), (6, 6), (1, 1), (12, 12)), "postorder", [1, 6, 12, 15]),
        (((15, 15), (6, 6), (1, 1), (12, 12)), "preorder", [1, 12, 6, 15]),
        ((), "postorder", []),
    ],
)
def test_traverse(elements, order, expected):
    map = dummy_bst(elements)
    assert traverse(map, order) == expected


@pytest.mark.parametrize(
    "elements,put_element,expected",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), (1, 12), [8, 3, 1, 6]),
        (((8, 8), (3, 3), (1, 1), (6, 6)), (10, 10), [8, 3, 1, 6, 10]),
        ((), (1, 1), [1]),
    ],
)
def test_put(elements, put_element, expected):
    map = dummy_bst(elements)
    put(map, *put_element)
    assert traverse(map, "inorder") == expected


@pytest.mark.parametrize(
    "elements,key,expected_value,expected_order",
    [
        (((10, 10), (30, 30), (1, 1), (20, 20)), 1, 1, [10, 30, 20]),
        (
            (
                (10, 10),
                (30, 30),
                (1, 1),
                (20, 20),
                (4, 4),
                (71, 71),
                (12, 12),
                (13, 13),
                (7, 7),
            ),
            4,
            4,
            [10, 1, 7, 30, 20, 12, 13, 71],
        ),
    ],
)
def test_remove(elements, key, expected_value, expected_order):
    map = dummy_bst(elements)
    remove_value = remove(map, key)
    assert remove_value == expected_value and traverse(map, "inorder") == expected_order


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 4, 4),
        (((12, 12), (6, 6), (18, 18), (3, 3), (21, 21)), 21, 21),
    ],
)
def test_get(elements, key, expected):
    map = dummy_bst(elements)
    assert get_value(map, key) == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((100, 99), (99, 98), (101, 100), (1, 6)), 1, True),
        (((0, 0), (2, 2), (4, 4), (-4, -4)), 10, False),
    ],
)
def test_has_element(elements, key, expected):
    map = dummy_bst(elements)
    assert has_key(map, key) == expected
