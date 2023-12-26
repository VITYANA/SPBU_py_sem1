from io import StringIO
import pytest
from src.Practice.prac9.task1.main import *
from src.Practice.prac9.task1.FSM import *


def test_make_fsms():
    assert make_fsms() == [
        FSMachine(*LANGUAGES[0][1:]),
        FSMachine(
            *LANGUAGES[1][1:],
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
