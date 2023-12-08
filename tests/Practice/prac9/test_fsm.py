import pytest
import string
from src.Practice.prac9.task1.FSM import *


@pytest.fixture
def create_fs_machine_digits():
    table_digits = [
        {string.digits: 1, "+-": 5},
        {string.digits: 1, "E": 3, ".": 6},
        {string.digits: 2, "E": 3},
        {string.digits: 4, "+-": 7},
        {string.digits: 4},
        {string.digits: 1},
        {string.digits: 2},
        {string.digits: 4},
    ]
    return create_fs_machine(table_digits, 0, [1, 2, 4])


@pytest.fixture
def create_fs_machine_abb():
    table_abb = [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}]
    return create_fs_machine(table_abb, 0, [3])


def test_create_fs_machine():
    example = create_fs_machine([{"abc": 0, "def": 1}, {"mcp": 0}], 0, [0, 1])
    assert (
        type(example) == FSMachine
        and example.states == [{"abc": 0, "def": 1}, {"mcp": 0}]
        and example.start_state == 0
        and example.accepted_states == [0, 1]
    )


@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("+inf", False),
        ("+12", True),
        ("+", False),
        (".123", False),
        ("1234", True),
        ("123.", False),
        ("123.23", True),
        ("123.23E", False),
        ("123.23E+", False),
        ("123.23E-2", True),
        ("123.23E+2.", False),
        ("", False),
    ],
)
def test_validate_string_with_digits(string_input, expected, create_fs_machine_digits):
    assert validate_string(create_fs_machine_digits, string_input) == expected


@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("", False),
        ("aaa", False),
        ("abb", True),
        ("1298", False),
        ("adasvabb", False),
        ("aaaaababb", True),
        ("abbabbabbabbabb", True),
        ("abbab", False),
    ],
)
def test_validate_string_with_string_abb(string_input, expected, create_fs_machine_abb):
    assert validate_string(create_fs_machine_abb, string_input) == expected
