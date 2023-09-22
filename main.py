if __name__ == "__main__":
    n = int(input("Введите число - предел для знаменателя: "))
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if j % i != 0 or i == 1:
                print(i, '/',  j)
