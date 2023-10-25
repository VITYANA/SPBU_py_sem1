import random


def main():
    print(
        "Добро пожаловать в мою игру, в ней я загадаю вам число формата 0000, а вы должны его отгадать. \n"
        "Правила:\n"
        "1)В случае, когда вы угадаете цифру, но она будет на другой позиции, я выведу Коровы - 1.\n"
        "2)В случае, когда вы угадаете цифру и её позицию, я выведу Быки - 1.\n"
        "Все цифры в числе разные.\n"
        "Удачи! "
    )
    hidden_num = randomize_num()
    print("\n--НАЧАЛО ИГРЫ--" "\nВводите числа!")
    print(guessing(hidden_num))


def guessing(hide_num):
    guessed_num = ""
    turn_num = 0
    while guessed_num != hide_num:
        turn_num += 1
        guessed_num = game(turn_num, hide_num)
    ret_str = f"Верно, поздавляю!\nКоличество попыток - {turn_num}"
    return ret_str


def game(turn_num, hide_num):
    a, b = 0, 0
    guessed_num = check_input(input())
    for i in range(4):
        if guessed_num[i] in hide_num:
            if guessed_num[i] == hide_num[i]:
                b += 1
            else:
                a += 1
    print(f"{turn_num}: Быки - {a} | Коровы - {b}")
    return guessed_num


def check_input(string):
    if len(string) != 4 or any(not string[i].isdigit() for i in range(4)):
        while len(string) != 4 or any(not string[i].isdigit() for i in range(4)):
            string = input("Неверный формат числа!\nВведите число типа 0000\n")
    return string


def randomize_num():
    hidden_num = ""
    while len(hidden_num) == 0:
        number = random.sample(range(10), 4)
        if number[0] != 0:
            hidden_num = "".join(map(str, number))
    print(hidden_num)
    return hidden_num


if __name__ == "__main__":
    main()
