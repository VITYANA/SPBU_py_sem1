from io import StringIO
import pytest
from src.Practice.prac6.task1 import *


quadratic = [
    (2, -5, 3, [1.5, 1]),
    (1, -4, 3, [3, 1]),
    (1, 4, 3, [-1, -3]),
    (1, 2, 3, "Negative discriminant, no solves.")
]


linear = [
    (2, 3, -1.5),
    (0, 3, "Solve is any real number."),
    (3, 0, "Wrong parameters. k and b cant be zero.")
]


number = [
    ("1", True),
    ('acd', False),
    ("0.000", True)
]


main = [
    ("2 -5 3", "x1 = 1.5\nx2 = 1.0"),
    ("1 -4 3", "x1 = 3\nx2 = 1"),
    ("1 4 3", "x1 = -3\nx2 = -1"),
    ("1 2 3", "Negative discriminant, no solves."),
    ("0, 3", "Wrong input!"),
    ("0.000", "Wrong input!"),
    ("abc 1 3", "Wrong input!")
]


@pytest.mark.parametrize("a, b, c, expected", quadratic)
def quadratic_equation_solve_test(a, b, c, expected):
    actual = quadratic_equation_solve(a, b, c)
    assert actual == expected


@pytest.mark.parametrize("k, b, expected", linear)
def linear_equation_solve_test(k, b, expected):
    actual = linear_equation_solve(k, b)
    assert actual == expected


@pytest.mark.parametrize("argument, expected", number)
def is_number_test(argument, expected):
    actual = is_number(argument)
    assert actual == expected


@pytest.mark.parametrize("input_line, expected", main)
def test_main_scenario(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_func()
    output = fake_output.getvalue()
    for string in output:
        assert string == expected
