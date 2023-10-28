from io import StringIO
import pytest
from src.Practice.prac6.task1 import *


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (2, -5, 3, (1.5, 1.0)),
        (1, -4, 3, (3.0, 1.0)),
        (1, 4, 3, (-1.0, -3.0)),
        (2, 4, 2, (-1.0,)),
    ),
)
def test_quadratic_equation_solve(a, b, c, expected):
    assert quadratic_equation_solve(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (
            1,
            2,
            3,
            ArithmeticError,
        ),  # ArithmeticError("Negative discriminant, no solves.")
        (5, 3, 7, ArithmeticError),
        (12, 12, 12, ArithmeticError),
    ],
)
def test_quadratic_equation_solve_ERROR(a, b, c, expected):
    with pytest.raises(expected):
        assert quadratic_equation_solve(a, b, c) == expected


@pytest.mark.parametrize(
    "k, b, expected",
    (
        (2, 3, (-1.5,)),
        (3, 4, (-1.3333333333333333,)),
        (13, float("inf"), (float("-inf"),)),
    ),
)
def test_linear_equation_solve(k, b, expected):
    assert linear_equation_solve(k, b) == expected


@pytest.mark.parametrize(
    "tpl, expected",
    (
        (("1", "2", "3"), True),
        (("15", "30", "0"), True),
        (("3.9", "310210930129831", "inf"), True),
    ),
)
def test_check_input(tpl, expected):
    assert check_input(tpl) == expected


@pytest.mark.parametrize(
    "tpl, expected",
    (
        (("1",), ValueError),
        (("ab", "0"), ValueError),
        (("ab",), ValueError),
    ),
)
def test_check_input_AttributeError(tpl, expected):
    with pytest.raises(expected):
        assert check_input(tpl) == expected


@pytest.mark.parametrize(
    "tpl, expected",
    (
        (("1", "  ", "1,2312"), ValueError),
        (("ab", "0", "0"), ValueError),
        (("21", "error", "21"), AttributeError),
    ),
)
def test_check_input_ValueError(tpl, expected):
    with pytest.raises(ValueError):
        assert check_input(tpl) == expected


@pytest.mark.parametrize("a, b, c, expected", ((0, 0, 0, ValueError),))
def test_solve_equation_000(a, b, c, expected):
    with pytest.raises(expected):
        assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    ((0, 0, 3, ValueError), (0, 0, 21, ValueError), (0, 0, -9.3, ValueError)),
)
def test_solve_equation_ValueError(a, b, c, expected):  # when a, b = 0, 0
    with pytest.raises(ValueError):
        assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (0, 3, 3, linear_equation_solve(3, 3)),
        (0, 15, -6, linear_equation_solve(15, -6)),
        (0, 9, 10, linear_equation_solve(9, 10)),
    ),
)
def test_solve_equation_linear(a, b, c, expected):
    assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (3, 15, 3, quadratic_equation_solve(3, 15, 3)),
        (8, 15, -6, quadratic_equation_solve(8, 15, -6)),
        (13, 14, -9, quadratic_equation_solve(13, 14, -9)),
    ),
)
def test_solve_equation_quadratic(a, b, c, expected):
    assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "argument, expected", (("1", True), ("acd", False), ("0.000", True))
)
def test_is_number(argument, expected):
    assert is_number(argument) == expected


@pytest.mark.parametrize(
    "input_line, expected",
    (
        ("2 -5 3", "Solution of the equation: 1.5, 1.0\n"),
        ("1 -4 3", "Solution of the equation: 3.0, 1.0\n"),
        ("1 4 3", "Solution of the equation: -1.0, -3.0\n"),
        ("0 2 5", "Solution of the equation: -2.5\n"),
    ),
)
def test_main_scenario(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_func()
    output = fake_output.getvalue()
    assert output == expected


@pytest.mark.parametrize(
    "input_line, expected",
    (
        ("1 2 3", "Program ended with error: Negative discriminant, no solves.\n"),
        ("12", "Incorrect input: You need to input 3 args!\n"),
        ("1 a 3", "Incorrect input: a isn't number!\n"),
        (
            "0 0 15",
            "Program ended with error: Wrong parameters. a and b cant be zero simultaneously.\n",
        ),
        ("0 0 0", "Program ended with error: All coefficient cant be zero.\n"),
    ),
)
def test_main_scenario_err(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_func()
    output = fake_output.getvalue()
    assert output == expected
