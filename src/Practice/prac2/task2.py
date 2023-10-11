import random


def guessing(hide_num):
    guessed_num = ""
    turn_num = 0
    while guessed_num != hide_num:
        turn_num += 1
        a = 0
        b = 0
        guessed_num = input()
        if len(guessed_num) != 4:
            while len(guessed_num) != 4:
                guessed_num = input("Неверный формат числа!\nВведите число типа 0000\n")
        for i in range(4):
            if guessed_num[i] in hide_num:
                if guessed_num[i] == hide_num[i]:
                    b += 1
                else:
                    a += 1
        print(f"{turn_num}: A - {a} | B - {b}")
    ret_str = f"Верно, поздавляю!\nКоличество попыток - {turn_num}"
    return ret_str


if __name__ == "__main__":
    print(
        "Добро пожаловать в мою игру, в ней я загадаю вам число формата 0000, а вы должны его отгадать. \n"
        "Правила:\n"
        "1)В случае, когда вы угадаете цифру, но она будет на другой позиции, я выведу A - 1.\n"
        "2)В случае, когда вы угадаете цифру и её позицию, я выведу B - 1.\n"
        "Все цифры в числе разные.\n"
        "Удачи! "
    )
    hidden_num = ""
    while len(hidden_num) != 4:
        number = str(random.randint(0, 9))
        if number not in hidden_num:
            hidden_num += number
    print("\n--НАЧАЛО ИГРЫ--" "\nВводите числа!")
    print(guessing(hidden_num))
