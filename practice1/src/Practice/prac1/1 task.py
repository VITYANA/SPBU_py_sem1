def delenie(delimoe, delitel):
    chastnoe = 0
    while delimoe >= delitel:
        chastnoe += 1
        delimoe -= delitel
    return chastnoe


if __name__ == '__main__':
    delimoe = int(input("Введите делимое: "))
    delitel = int(input("Введите делитель: "))
    print(f"Неполное частное от деления = {delenie(delimoe, delitel)}")
