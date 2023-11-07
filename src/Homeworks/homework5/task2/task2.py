import re


def decode(string: str):
    output = re.sub(r"([a-z])(\d*)", lambda x: str(x[0][0] * int(x[0][1:])), string)
    return output


def encode(string: str):
    str_ = re.sub(r"(\w)\1*", lambda x: x[0][0] + str(len(x[0])), string)
    return str_


def check_input_to_decode(string_input: str):
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


def check_input_to_encode(string_input: str):
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
