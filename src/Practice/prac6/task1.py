def main_func():
    args = input("Please, write a, b, c: ").split()
    if len(args) != 3 or any(not is_number(i) for i in args):
        return "Wrong input!"
    a, b, c = float(args[0]), float(args[1]), float(args[2])
    if a != 0:
        res = quadratic_equation_solve(a, b, c)
        if len(res) == 2:
            return f"x1 = {res[0]}\nx2 = {res[1]}"
        elif len(res) == 1:
            return -b / (2 * a)
        else:
            return res
    elif a == 0:
        return linear_equation_solve(float(b), float(c))


def quadratic_equation_solve(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        return [
            (-b + discriminant**0.5) / (2 * a),
            (-b - discriminant**0.5) / (2 * a),
        ]
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        return "Negative discriminant, no solves."


def linear_equation_solve(k, b):
    if k == 0:
        if b == 0:
            return "Wrong parameters. k and b cant be zero."
        return "Solve is any real number."
    result = -b / k
    return result


def is_number(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print(main_func())
