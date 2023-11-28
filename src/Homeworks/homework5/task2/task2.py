import string


def encode(line: str) -> str:
    line_for_use = "0" + line
    new_letters_index = (
        list(
            filter(
                lambda index: line_for_use[index - 1] != line_for_use[index],
                range(len(line_for_use)),
            )
        )
        + [len(line_for_use)]
    )[1:]
    return "".join(
        list(
            map(
                lambda letter, next_letter: line_for_use[letter]
                + str(next_letter - letter),
                new_letters_index,
                new_letters_index[1:],
            )
        )
    )


def decode(line: str) -> str:
    letters_index = list(
        filter(lambda index: line[index] in string.ascii_letters, range(len(line)))
    ) + [len(line)]
    return "".join(
        list(
            map(
                lambda letter, next_letter: line[letter]
                * int(line[letter + 1 : next_letter]),
                letters_index,
                letters_index[1:],
            )
        )
    )


def check_input_to_decode(string_input: str) -> ValueError | bool:
    if len(string_input) == 0:
        raise ValueError("Cant decode empty string.")
    if string_input[-1].isdigit():
        i = 0
        while i != len(string_input):
            if string_input[i].isalpha() and string_input[i + 1].isalpha():
                raise ValueError("You need to put string like a12b4c1095.")
            i += 1
        return True
    raise ValueError("Last symbol of string need to be digit.")


def check_input_to_encode(string_input: str) -> ValueError | bool:
    if len(string_input) == 0:
        raise ValueError("Cant encode empty string.")
    if not string_input.isalpha():
        raise ValueError("Your string must include only latin letters.")
    return True


def main():
    string_input = input("Enter a string: ")
    func_match = input("Enter what you want to do:\n1) Encode\n2) Decode\n")
    match func_match:
        case "1":
            try:
                check_input_to_encode(string_input)
                print(encode(string_input))
            except Exception as err:
                print(f"Program failed with error: {err}")
        case "2":
            try:
                check_input_to_decode(string_input)
                print(decode(string_input))
            except Exception as err:
                print(f"Program failed with error: {err}")


if __name__ == "__main__":
    main()
