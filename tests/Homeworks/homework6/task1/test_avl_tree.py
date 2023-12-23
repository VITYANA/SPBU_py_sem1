import random

from src.Homeworks.homework6.task1.AVLtree import *
import pytest


@pytest.fixture()
def empty_tree():
    empty_tree = create_tree_map()
    return empty_tree


@pytest.fixture()
def tree():
    tree = create_tree_map()
    for i in range(10):
        put(tree, i, i)
    return tree


def dummy_bst(elements: tuple):
    map = create_tree_map()
    for i in elements:
        put(map, i[0], i[1])
    return map


def test_create_tree_map():
    test_tree = create_tree_map()
    assert test_tree == Tree()


def test_put(empty_tree):
    actual_tree = empty_tree
    balance_factor = []
    for i in range(20):
        key_value = random.randint(0, 1000)
        put(actual_tree, key_value, key_value)
        balance_factor.append(get_balance_factor(actual_tree.root))
    balance_factor = list(filter(lambda cond: cond < 2, balance_factor))
    assert len(balance_factor) == 20


@pytest.mark.parametrize("key, values", ((1, 1), (3, 3), (5, 5), (7, 7), (9, 9)))
def test_get_function(key, values, tree):
    actual = get_value(tree, key)
    assert actual == values


@pytest.mark.parametrize("key, expected", ((10, -1), (-3, -1)))
def test_get_function(key, expected, tree):
    assert get_value(tree, key) == expected


@pytest.mark.parametrize(
    "key, result",
    (
        (0, True),
        (2, True),
        (9, True),
        (10, False),
        (-1, False),
    ),
)
def test_has_key(key, result, tree):
    actual = has_key(tree, key)
    assert actual == result


def test_put_root(empty_tree):
    put_root(empty_tree, 3, 3)
    assert empty_tree.root == TreeNode(3, 3)


@pytest.mark.parametrize(
    "key, order",
    [
        (1, [[0, 0], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]),
        (3, [[0, 0], [1, 1], [2, 2], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]),
    ],
)
def test_remove(tree, key, order):
    remove(tree, key)
    actual = traverse(tree, "postorder")
    assert actual == order


def test_remove_empty_tree(empty_tree):
    with pytest.raises(ValueError):
        remove(empty_tree, 999)


@pytest.mark.parametrize(
    "elements,order,expected",
    [
        (
            ((15, 15), (6, 6), (1, 1), (12, 12)),
            "inorder",
            [[6, 6], [1, 1], [15, 15], [12, 12]],
        ),
        (
            ((15, 15), (6, 6), (1, 1), (12, 12)),
            "postorder",
            [[1, 1], [6, 6], [12, 12], [15, 15]],
        ),
        (
            ((15, 15), (6, 6), (1, 1), (12, 12)),
            "preorder",
            [[1, 1], [12, 12], [15, 15], [6, 6]],
        ),
        ((), "postorder", []),
    ],
)
def test_traverse(elements, order, expected):
    map = dummy_bst(elements)
    assert traverse(map, order) == expected


def test_extract_max(tree):
    actual = get_maximum(tree)
    assert actual == 9


def test_extract_min(tree):
    actual = get_minimum(tree)
    assert actual == 0


split_data_set = [
    (
        5,
        [
            [[0, 0], [1, 1], [2, 2], [3, 3], [7, 7], [8, 8], [9, 9]],
            [[4, 4], [5, 5], [6, 6]],
        ],
    ),
    (
        10,
        [
            [
                [0, 0],
                [1, 1],
                [2, 2],
                [3, 3],
                [4, 4],
                [5, 5],
                [6, 6],
                [7, 7],
                [8, 8],
                [9, 9],
            ],
            [],
        ],
    ),
    (
        7,
        [
            [[0, 0], [1, 1], [2, 2], [3, 3]],
            [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],
        ],
    ),
]


@pytest.mark.parametrize(
    "key, result",
    split_data_set,
)
def test_split_function(key, result, tree):
    actual = list(map(lambda _tree: traverse(_tree, "postorder"), split(tree, key)))
    assert actual == result


new_tree_data = [
    [-10, -10],
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
    [9, 9],
    [10, 10],
]


def test_merge_functions(tree):
    new_tree = create_tree_map()
    put(new_tree, -10, -10)
    put(new_tree, 10, 10)
    actual = traverse(merge(new_tree, tree), "postorder")
    assert actual == new_tree_data


def test_split_tree_empty(empty_tree):
    actual = split(empty_tree, 100)
    assert actual == (empty_tree, empty_tree)


def test_merge_tree_empty_scenario(empty_tree):
    actual = merge(empty_tree, empty_tree)
    assert actual == empty_tree


@pytest.mark.parametrize(
    "args, result",
    (
        ([1, 2, 3], [[2, 1], [1, 1], [3, 1]]),
        ([1, 2, 0, -1, -2], [[1, 1], [-1, 1], [-2, 1], [0, 1], [2, 1]]),
    ),
)
def test_balance_function(args, result, empty_tree):
    for arg in args:
        put(empty_tree, arg, 1)
    assert traverse(empty_tree, "inorder") == result
