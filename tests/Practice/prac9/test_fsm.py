import pytest
from src.Practice.prac9.task1.main import *


def test_create_fs_machine():
    example = create_fs_machine([{"abc": 0, "def": 1}, {"mcp": 0}], 0, [0, 1])
    assert (
        type(example) == FSMachine
        and example.states == [{"abc": 0, "def": 1}, {"mcp": 0}]
        and example.start_state == 0
        and example.terminal_states == [0, 1]
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
def test_validate_string_with_digits(string_input, expected):
    assert validate_string(make_fsms()[1], string_input) == expected


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
def test_validate_string_with_string_abb(string_input, expected):
    assert validate_string(make_fsms()[0], string_input) == expected
