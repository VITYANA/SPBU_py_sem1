from functools import wraps


def curry_explicit(function, arity):
    if arity < 0:
        raise ValueError("Arity cannot be negative.")
    elif arity == 0:
        return function()
    argument_list = []

    @wraps(function)
    def inner_func(arguments):
        if arity == len(arguments):
            return function(*arguments)

        def curry(arg):
            return inner_func([*arguments, arg])

        return curry

    return inner_func(argument_list)


def uncurry_explicit(function, arity):
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    @wraps(function)
    def uncurry(*args):
        if len(args) == 1 or len(args) == 0:
            return function(*args)
        result = function(args[0])
        for i in range(1, arity):
            result = result(args[i])
        return result

    return uncurry


if __name__ == "__main__":
    f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    g2 = uncurry_explicit(f2, 3)
    print(f2(123)(456)(562))  # <123,456,562>
    print(g2(123, 456, 562))  # <123,456,562>
