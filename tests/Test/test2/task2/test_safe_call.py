from src.Test.Test2.task2.Safe_call import *
import pytest


@safe_call
def foo(a):
    if a < 100:
        raise ValueError("a must be more or equal 100.")
    return a


@safe_call
def goo(b):
    if type(b) == str:
        raise ValueError("b must be  not str.")
    return foo(b)


@pytest.mark.parametrize(
    "func, input_arg, expected_line, expected_num, expected_type_error, expected_error_message",
    [
        (
            foo,
            0,
            'raise ValueError("a must be more or equal 100.")',
            8,
            "'ValueError'",
            "a must be more or equal 100.",
        ),
        (
            foo,
            "abc",
            "if a < 100:",
            7,
            "'TypeError'",
            "'<' not supported between instances of 'str' and 'int'",
        ),
        (
            foo,
            [],
            "if a < 100:",
            7,
            "'TypeError'",
            "'<' not supported between instances of 'list' and 'int'",
        ),
    ],
)
def test_extract_error_line_from_stacktrace(
    func,
    input_arg,
    expected_line,
    expected_num,
    expected_type_error,
    expected_error_message,
):
    with warnings.catch_warnings(record=True):
        try:
            func(input_arg)
        except Exception:
            (
                output_line,
                output_num,
                output_type_error,
                output_error_message,
            ) = extract_error_line_from_stacktrace()
            assert output_line == expected_line
            assert output_num == expected_num
            assert output_type_error == expected_type_error
            assert output_error_message == expected_error_message


@pytest.mark.parametrize(
    "func, input_number, expected",
    (
        (
            foo,
            12,
            "\n"
            "error in function: foo\n"
            "type of error: 'ValueError'\n"
            "message of error: a must be more or equal 100.\n"
            'error line: raise ValueError("a must be more or equal 100.")\n'
            "error line num: 8",
        ),
        (
            foo,
            0,
            "\n"
            "error in function: foo\n"
            "type of error: 'ValueError'\n"
            "message of error: a must be more or equal 100.\n"
            'error line: raise ValueError("a must be more or equal 100.")\n'
            "error line num: 8",
        ),
        (
            foo,
            "asv",
            "\n"
            "error in function: foo\n"
            "type of error: 'TypeError'\n"
            "message of error: '<' not supported between instances of 'str' and 'int'\n"
            "error line: if a < 100:\n"
            "error line num: 7",
        ),
    ),
)
def test_safe_call_with_err(func, input_number, expected):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        func(input_number)
        assert len(w) == 1
        assert issubclass(w[-1].category, Warning)
        assert expected == str(w[-1].message)


@pytest.mark.parametrize(
    "input_number, expected", [(101, 101), (10000, 10000), (150000, 150000)]
)
def test_safe_call_without_err(input_number, expected):
    with warnings.catch_warnings(record=True) as w:
        output = foo(input_number)
        assert output == input_number
        assert len(w) == 0


@pytest.mark.parametrize(
    "func_name, type_error, message_error, error_line, error_line_num, expected",
    (
        (
            "foo",
            "'TypeError'",
            'can only concatenate str (not "list") to str',
            "print(a + b)",
            "40",
            "\n"
            "error in function: foo\n"
            "type of error: 'TypeError'\n"
            'message of error: can only concatenate str (not "list") to str\n'
            "error line: print(a + b)\n"
            "error line num: 40",
        ),
        (
            "gogogo",
            "'ErrorError'",
            "PIOMON",
            "print(a + b)",
            "666",
            "\n"
            "error in function: gogogo\n"
            "type of error: 'ErrorError'\n"
            "message of error: PIOMON\n"
            "error line: print(a + b)\n"
            "error line num: 666",
        ),
        (
            "big mistake in code...",
            "would i fix it?",
            "yes!",
            "i'm developer!",
            "I will fix this tests!",
            "\n"
            "error in function: big mistake in code...\n"
            "type of error: would i fix it?\n"
            "message of error: yes!\n"
            "error line: i'm developer!\n"
            "error line num: I will fix this tests!",
        ),
    ),
)
def test_return_message(
    func_name, type_error, message_error, error_line, error_line_num, expected
):
    assert (
        return_message(func_name, type_error, message_error, error_line, error_line_num)
        == expected
    )


@pytest.mark.parametrize(
    "func, input_num, expected",
    [
        (
            goo,
            12,
            "\n"
            "error in function: foo\n"
            "type of error: 'ValueError'\n"
            "message of error: a must be more or equal 100.\n"
            'error line: raise ValueError("a must be more or equal 100.")\n'
            "error line num: 8",
        ),
        (
            goo,
            "abc",
            "\n"
            "error in function: goo\n"
            "type of error: 'ValueError'\n"
            "message of error: b must be  not str.\n"
            'error line: raise ValueError("b must be  not str.")\n'
            "error line num: 15",
        ),
        (
            goo,
            0.13,
            "\n"
            "error in function: foo\n"
            "type of error: 'ValueError'\n"
            "message of error: a must be more or equal 100.\n"
            'error line: raise ValueError("a must be more or equal 100.")\n'
            "error line num: 8",
        ),
        (
            goo,
            [],
            "\n"
            "error in function: foo\n"
            "type of error: 'TypeError'\n"
            "message of error: '<' not supported between instances of 'list' and 'int'\n"
            "error line: if a < 100:\n"
            "error line num: 7",
        ),
    ],
)
def test_safe_call_nested_func(func, input_num, expected):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        func(input_num)
        assert len(w) == 1
        assert issubclass(w[-1].category, Warning)
        assert expected == str(w[-1].message)
