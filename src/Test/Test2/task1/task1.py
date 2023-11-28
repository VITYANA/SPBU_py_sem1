def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def check_input(n):
    if not n.isdigit():
        print("The number must be an integer from 0 to 90.")
        return False
    n = int(n)
    if n < 0 or n > 90:
        print("The number must belong to the segment from 0 to 90.")
        return False
    return True


def main():
    n = input("Enter n - number of Fibonacci number: ")
    if check_input(n) is True:
        n = int(n)
        print(f"{n} Fibonacci number is {fib(n)}.")


if __name__ == "__main__":
    main()
