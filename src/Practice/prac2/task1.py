from math import gcd


def main():
    n = input("Введите число - предел для знаменателя: ")
    while not check_input(n):
        n = input("Введенное n не является числом, повторите ввод: ")
    all_nums = find_answers(int(n))
    result = sort_nums(all_nums)
    print("\n".join(map(str, result)))


def sort_nums(lst):
    return sorted(lst, key=lambda x: float(x[x.find("=") + 2 :]))


def find_answers(n):
    all_nums = []
    for i in range(1, n - 1):
        check = True
        for j in range(i + 1, n + 1):
            if gcd(i, j) == 1 and i / j not in all_nums:
                res = i / j
                all_nums.append(f"{i} / {j} = {res}")
    return all_nums


def check_input(n):
    return n.isdigit()


if __name__ == "__main__":
    main()
