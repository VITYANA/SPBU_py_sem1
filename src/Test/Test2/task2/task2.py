import functools
from datetime import datetime


def spy(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        current_time = datetime.now()
        params = {"args": args, "kwargs": kwargs}
        inner.logs.append((current_time, params))
        result = function(*args, **kwargs)
        return result

    inner.logs = []
    return inner


def print_usage_statistic(function):
    try:
        for log in function.logs:
            yield log
    except AttributeError:
        raise AttributeError(
            "It is impossible to find out the parameters of an undecorated function"
        )


@spy
def foo(num):
    print(num)


def main():
    foo(num=4)
    foo("hello")
    foo(5)
    for time, parameters in print_usage_statistic(foo):
        str_parameters = ", ".join(f"{k} = {v}" for k, v in parameters.items())
        print(
            f"function {foo.__name__} was called at {time} with parameters:\n{str_parameters}"
        )


if __name__ == "__main__":
    main()
