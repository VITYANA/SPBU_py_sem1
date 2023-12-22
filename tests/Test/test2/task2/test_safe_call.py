from src.Test.Test2.task2.Safe_call import *
import pytest


@safe_call
def foo(a):
    if a < 100:
        raise ValueError("a must be more or equal 100.")
    return a


@pytest.mark.parametrize(
    "func, input_arg, expected_line, expected_num",
    [
        (foo, 0, 'raise ValueError("a must be more or equal 100.")', 8),
        (foo, "abc", "if a < 100:", 7),
    ],
)
def test_extract_error_line_from_stacktrace(
    func, input_arg, expected_line, expected_num
):
    with warnings.catch_warnings(record=True) as w:
        try:
            func(input_arg)
        except Exception:
            output_line, output_num = extract_error_line_from_stacktrace()
            assert output_line == expected_line
            assert output_num == expected_num


@pytest.mark.parametrize(
    "func, input_number, expected",
    (
        (
            foo,
            12,
            (
                "\n"
                "error in function: foo\n"
                "type of error: 'ValueError'\n"
                "message of error: a must be more or equal 100.\n"
                'error line: raise ValueError("a must be more or equal 100.")\n'
                "error line num: 8"
            ),
        ),
        (
            foo,
            0,
            (
                "\n"
                "error in function: foo\n"
                "type of error: 'ValueError'\n"
                "message of error: a must be more or equal 100.\n"
                'error line: raise ValueError("a must be more or equal 100.")\n'
                "error line num: 8"
            ),
        ),
        (
            foo,
            "asv",
            (
                "\n"
                "error in function: foo\n"
                "type of error: 'TypeError'\n"
                "message of error: '<' not supported between instances of 'str' and 'int'\n"
                "error line: if a < 100:\n"
                "error line num: 7"
            ),
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
        assert output == int(input_number)
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
            (
                "\n"
                "error in function: foo\n"
                "type of error: 'TypeError'\n"
                'message of error: can only concatenate str (not "list") to str\n'
                "error line: print(a + b)\n"
                "error line num: 40"
            ),
        ),
        (
            "gogogo",
            "'ErrorError'",
            "PIOMON",
            "print(a + b)",
            "666",
            (
                "\n"
                "error in function: gogogo\n"
                "type of error: 'ErrorError'\n"
                "message of error: PIOMON\n"
                "error line: print(a + b)\n"
                "error line num: 666"
            ),
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
