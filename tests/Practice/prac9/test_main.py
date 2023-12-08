from io import StringIO
import pytest
from src.Practice.prac9.task1.main import *
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
def test_digits_validation(string_input, expected, create_fs_machine_digits):
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
def test_abb_validation(string_input, expected, create_fs_machine_abb):
    assert validate_string(create_fs_machine_abb, string_input) == expected


@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("123abc", "This string match no language."),
        ("aabb", "This is abb-type language."),
        ("-1234.123E+12", "This is Digits language."),
        ("123.E", "This string match no language."),
    ],
)
def test_output_match(string_input, expected):
    assert output_match(string_input) == expected


@pytest.mark.parametrize(
    "user_input, output",
    [
        ("123abc", "This string match no language.\n"),
        ("aabb", "This is abb-type language.\n"),
        ("-1234.123E+12", "This is Digits language.\n"),
        ("123.E", "This string match no language.\n"),
    ],
)
def test_main(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    fake_output = fake_output.getvalue()
    assert output == fake_output
