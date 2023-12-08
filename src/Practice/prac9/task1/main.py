from src.Practice.prac9.task1.FSM import *
import string


def digits_validation(input_str: str) -> bool:
    table_digits = [
        {string.digits: 1, "+-": 5},
        {string.digits: 1, "E": 3, ".": 6},
        {string.digits: 2, "E": 3},
        {string.digits: 4, "+-": 7},
        {string.digits: 4},
        {string.digits: 1},
        {string.digits: 2},
        {string.digits: 4},
    ]
    return validate_string(create_fs_machine(table_digits, 0, [1, 2, 4]), input_str)


def abb_validation(input_str: str) -> bool:
    table_abb = [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}]
    return validate_string(create_fs_machine(table_abb, 0, [3]), input_str)


def output_match(user_input: str) -> str:
    if abb_validation(user_input):
        return "This is abb-type language."
    elif digits_validation(user_input):
        return "This is Digits language."
    else:
        return "This string match no language."


def main():
    user_input = input("Input string for validation: ")
    print(output_match(user_input))


if __name__ == "__main__":
    main()
