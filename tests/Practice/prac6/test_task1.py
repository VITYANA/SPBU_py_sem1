from io import StringIO
import pytest
from src.Practice.prac6.task1 import *


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (2, -5, 3, ("x1 = 1.5 ", "x2 = 1.0")),
        (1, -4, 3, ("x1 = 3.0 ", "x2 = 1.0")),
        (1, 4, 3, ("x1 = -1.0 ", "x2 = -3.0")),
    ],
)
def test_quadratic_equation_solve(a, b, c, expected):
    assert quadratic_equation_solve(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, ValueError),  # ValueError("Negative discriminant, no solves.")
        (5, 3, 7, ValueError),
        (12, 12, 12, ValueError),
    ],
)
def test_quadratic_equation_solve_ERROR(a, b, c, expected):
    with pytest.raises(ValueError):
        assert quadratic_equation_solve(a, b, c) == expected


@pytest.mark.parametrize("k, b, expected", [(2, 3, ("x = -1.5",))])
def test_linear_equation_solve(k, b, expected):
    assert linear_equation_solve(k, b) == expected


@pytest.mark.parametrize(
    "tpl, expected", ((("1", "2", "3"), True), (("15", "30", "0"), True))
)
def test_check_input(tpl, expected):
    assert check_input(tpl) == expected


@pytest.mark.parametrize(
    "tpl, expected",
    (
        (("1",), AttributeError),
        (("ab", "0"), AttributeError),
        (("ab",), AttributeError),
    ),
)
def test_check_input_AttributeError(tpl, expected):
    with pytest.raises(AttributeError):
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


@pytest.mark.parametrize("a, b, c, expected", ((0, 0, 0, "Solve is any real number."),))
def test_solve_equation_000(a, b, c, expected):
    assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected", ((0, 0, 3, ValueError), (0, 0, 21, ValueError))
)
def test_solve_equation_ValueError(a, b, c, expected):
    with pytest.raises(ValueError):
        assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (0, 3, 3, linear_equation_solve(3, 3)),
        (0, 15, -6, linear_equation_solve(15, -6)),
    ),
)
def test_solve_equation_linear(a, b, c, expected):
    assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (3, 15, 3, quadratic_equation_solve(3, 15, 3)),
        (8, 15, -6, quadratic_equation_solve(8, 15, -6)),
    ),
)
def test_solve_equation_quadratic(a, b, c, expected):
    assert solve_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "argument, expected", [("1", True), ("acd", False), ("0.000", True)]
)
def test_is_number(argument, expected):
    assert is_number(argument) == expected


@pytest.mark.parametrize(
    "input_line, expected",
    [
        ("2 -5 3", "Solution of the equation: x1 = 1.5 x2 = 1.0\n"),
        ("1 -4 3", "Solution of the equation: x1 = 3.0 x2 = 1.0\n"),
        ("1 4 3", "Solution of the equation: x1 = -1.0 x2 = -3.0\n"),
        ("0 2 5", "Solution of the equation: x = -2.5\n"),
    ],
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
    [
        ("1 2 3", "Program ended with error: Negative discriminant, no solves.\n"),
        ("12", "Incorrect input: You need to input 3 args!\n"),
        ("1 a 3", "Incorrect input: a isn't number!\n"),
        ("0 0 15", "Program ended with error: Wrong parameters. a and b cant be zero.\n"),
    ],
)
def test_main_scenario_err(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_func()
    output = fake_output.getvalue()
    assert output == expected
