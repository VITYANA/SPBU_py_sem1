from io import StringIO

from src.Test.Test2.task2.task2 import *
import pytest


@spy
def foo(a, b):
    return a, b


@spy
def foo2():
    return True


foo3 = lambda x: x


@spy
def foo(num):
    print(num)


@spy
def foo4(x):
    return x


def test_print_usage_statistic():
    value = [i for i in print_usage_statistic(foo)]
    assert "".join(value) == ""


def test_print_usage():
    for _ in range(54):
        foo2()
    result = list(print_usage_statistic(foo2))
    assert len(result) == 54


def test_print_usage_exception():
    for _ in range(3):
        foo3("aaa")
    with pytest.raises(AttributeError):
        list(print_usage_statistic(foo3))
