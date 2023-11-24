from io import StringIO
from src.Test.Test2.task1.task1 import *
import pytest


@pytest.mark.parametrize("n, expected",
                         [
                             (0, 0),
                             (1, 1),
                             (5, 5),
                             (90, 2880067194370816120)
                         ])
def test_fib(n, expected):
    assert fib(n) == expected


@pytest.mark.parametrize("n, expected",
                         [
                             ("12", True),
                             ("001", True),
                             ("abcd", False),
                             ("91", False),
                             ("-1", False),
                             ("2.5", False),
                             ("inf", False),
                             ("-0", False),
                             (".0123", False)
                         ])
def test_check_input(n, expected):
    assert check_input(n) == expected


@pytest.mark.parametrize("n, expected",
                         [
                             ("0", '0 Fibonacci number is 0.\n'),
                             ("12", '12 Fibonacci number is 144.\n'),
                             ("90", '90 Fibonacci number is 2880067194370816120.\n'),
                             ("abc", 'The number must be an integer from 0 to 90.\n'),
                             ("100", 'The number must belong to the segment from 0 to 90.\n'),
                             ("2.5", 'The number must be an integer from 0 to 90.\n')
                         ])
def test_main(monkeypatch, n, expected):
    monkeypatch.setattr("builtins.input", lambda _: n)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
