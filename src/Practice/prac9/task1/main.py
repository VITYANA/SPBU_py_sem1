from src.Practice.prac9.task1.FSM import *
import string


LANGUAGES = [
    [
        "abb-type language",
        [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}],
        0,
        [3],
    ],
    [
        "digits language",
        [
            {string.digits: 1, "+-": 5},
            {string.digits: 1, "E": 3, ".": 6},
            {string.digits: 2, "E": 3},
            {string.digits: 4, "+-": 7},
            {string.digits: 4},
            {string.digits: 1},
            {string.digits: 2},
            {string.digits: 4},
        ],
        0,
        [1, 2, 4],
    ],
]


def make_fsms():
    fsms = []
    for i in range(len(LANGUAGES)):
        fsms.append(create_fs_machine(*LANGUAGES[i][1:]))
    return fsms


def output_match(fsms, user_input: str) -> str:
    lang_found_flag = False
    for i in range(len(fsms)):
        if validate_string(fsms[i], user_input):
            lang_found_flag = True
            return f"String belongs to {LANGUAGES[i][0]}."
    if lang_found_flag is False:
        return f"String didn't belongs to any language."


def main():
    user_input = input("Input string for validation: ")
    print(output_match(make_fsms(), user_input))


if __name__ == "__main__":
    main()
