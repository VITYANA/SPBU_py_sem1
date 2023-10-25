def main_func():
    args = tuple(input("Please, write a, b, c: ").split())
    check_input(args)
    a, b, c = float(args[0]), float(args[1]), float(args[2])
    result = solve_equation(a, b, c)
    print(f"Solution of the equation: {''.join(map(str, result))}")


def check_input(args):
    if len(args) != 3:
        raise AttributeError("You need to input 3 args!")
    for i in args:
        if not is_number(i):
            raise ValueError(f"{i} isn't number!")
    return True


def solve_equation(a, b, c):
    if a == b == c == 0:
        return "Solve is any real number."
    elif a == b == 0:
        raise ValueError("Wrong parameters. a and b cant be zero.")
    elif a == 0:
        return linear_equation_solve(b, c)
    else:
        return quadratic_equation_solve(a, b, c)


def quadratic_equation_solve(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        res = (
            f"x1 = {((-b + discriminant ** 0.5) / (2 * a))} ",
            f"x2 = {((-b - discriminant ** 0.5) / (2 * a))}",
        )
        return res
    elif discriminant == 0:
        return tuple(f"x = {-b / (2 * a)}")
    else:
        raise ValueError("Negative discriminant, no solves.")


def linear_equation_solve(k, b):
    res = (f"x = {-b / k}",)
    return res


def is_number(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main_func()
