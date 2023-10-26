def main_func():
    args = tuple(input("Please, write a, b, c: ").split())
    try:
        check_input(args)
    except Exception as err:
        print(f"Incorrect input: {err}")
        return 0
    a, b, c = map(float, args)
    try:
        result = solve_equation(a, b, c)
        print(f"Solution of the equation: {', '.join(map(str, result))}")
    except Exception as err:
        print(f"Program ended with error: {err}")
        return 0


def check_input(args):
    if len(args) != 3:
        raise ValueError("You need to input 3 args!")
    for i in args:
        if not is_number(i):
            raise ValueError(f"{i} isn't number!")
    return True


def solve_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError("All coefficient cant be zero.")
    elif a == b == 0:
        raise ValueError("Wrong parameters. a and b cant be zero simultaneously.")
    elif a == 0:
        return linear_equation_solve(b, c)
    else:
        return quadratic_equation_solve(a, b, c)


def quadratic_equation_solve(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant == 0:
        return ((-b / (2 * a)),)
    elif discriminant < 0:
        raise ArithmeticError("Negative discriminant, no solves.")
    res = (
        ((-b + discriminant**0.5) / (2 * a)),
        ((-b - discriminant**0.5) / (2 * a)),
    )
    return res


def linear_equation_solve(k, b):
    return ((-b / k),)


def is_number(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main_func()
