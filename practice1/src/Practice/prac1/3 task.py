def primal(znachenie):
    potok = []
    for i in range(1, znachenie + 1):
        count = 0
        for j in range(2, znachenie):
            if i % j == 0:
                count += 1
            if count > 1:
                break
        if count == 1:
            potok.append(i)
    return potok


if __name__ == "__main__":
    a = int(input("Введите число: "))
    print(", ".join(map(str, primal(a))))
