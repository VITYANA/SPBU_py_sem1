def main():
    n = int(input("Введите число - предел для знаменателя: "))
    check_input(n)
    all_nums = find_answers(n)
    result = sort_nums(all_nums)
    print("\n".join(map(str, result)))


def sort_nums(lst):
    return sorted(lst, key=lambda x: float(x[x.find("=") + 2 :]))


def find_answers(n):
    all_nums = []
    for i in range(1, n):
        check = True
        for j in range(i + 1, n + 1):
            for divider in range(2, n):
                if i % divider == 0 and j % divider == 0:
                    check = False
            if check and i / j not in all_nums:
                res = i / j
                all_nums.append(f"{i} / {j} = {res}")
    return all_nums


def check_input(n):
    try:
        int(n)
        return True
    except TypeError:
        raise TypeError(f"{n} isn't integer.")


if __name__ == "__main__":
    main()