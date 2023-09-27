def multiply(x_):
    x_square = x_**2
    return (x_square + x_) * (x_square + 1) + 1


if __name__ == "__main__":
    x = int(input("Введите x: "))
    print(f"{x} ^ 4 + {x} ^ 3 + {x} ^ 2 + {x} + 1 =", multiply(x))
