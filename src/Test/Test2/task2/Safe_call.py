import functools
import traceback
import warnings
import sys


def safe_call(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception:
            func_name = function.__name__
            error_type, message_of_error = str(sys.exc_info()[0]), sys.exc_info()[1]
            error_type = error_type[error_type.find("'") : -1]
            error_line, error_line_num = extract_error_line_from_stacktrace()
            output_message = return_message(
                func_name, error_type, message_of_error, error_line, error_line_num
            )
            warnings.warn(output_message, category=Warning)

    return inner


def return_message(func_name, type_error, message_error, error_line, error_line_num):
    return_value = (
        f"\nerror in function: {func_name}\n"
        f"type of error: {type_error}\n"
        f"message of error: {message_error}\n"
        f"error line: {error_line}\n"
        f"error line num: {error_line_num}"
    )
    return return_value


def extract_error_line_from_stacktrace():
    stacktrace = traceback.extract_tb(sys.exc_info()[2])[-1]
    return stacktrace.line, stacktrace.lineno
