from io import StringIO
import pytest
from src.Practice.prac9.task1.main import *
from src.Practice.prac9.task1.FSM import *


def test_make_fsms():
    assert make_fsms() == [
        FSMachine(
            states=[
                {"b": 0, "a": 1},
                {"b": 2, "a": 1},
                {"b": 3, "a": 1},
                {"b": 0, "a": 1},
            ],
            start_state=0,
            accepted_states=[3],
        ),
        FSMachine(
            states=[
                {"0123456789": 1, "+-": 5},
                {"0123456789": 1, "E": 3, ".": 6},
                {"0123456789": 2, "E": 3},
                {"0123456789": 4, "+-": 7},
                {"0123456789": 4},
                {"0123456789": 1},
                {"0123456789": 2},
                {"0123456789": 4},
            ],
            start_state=0,
            accepted_states=[1, 2, 4],
        ),
    ]


@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("123abc", "String didn't belongs to any language."),
        ("aabb", "String belongs to abb-type language."),
        ("-1234.123E+12", "String belongs to digits language."),
        ("123.E", "String didn't belongs to any language."),
    ],
)
def test_output_match(string_input, expected):
    assert output_match(make_fsms(), string_input) == expected


@pytest.mark.parametrize(
    "user_input, output",
    [
        ("123abc", "String didn't belongs to any language.\n"),
        ("aabb", "String belongs to abb-type language.\n"),
        ("-1234.123E+12", "String belongs to digits language.\n"),
        ("123.E", "String didn't belongs to any language.\n"),
    ],
)
def test_main(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    fake_output = fake_output.getvalue()
    assert output == fake_output
