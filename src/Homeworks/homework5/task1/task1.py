def get_16b(s: str) -> list[str]:
    bit_list = []
    for i in s:
        if ord(i) < 65535:
            bit_1_symbol = f"{ord(i):016b}"
            bit_1_symbol = [
                " ".join(bit_1_symbol[j * 8 : (j + 1) * 8] for j in range(2))
            ]
            bit_list.append(bit_1_symbol[0])
        else:
            bit_1_symbol = f"{ord(i) - 65536:020b}"
            major_bits = f"{(int(bit_1_symbol[:10], 2) + 55296):b}"
            minor_bits = f"{(int(bit_1_symbol[10:], 2) + 56320):b}"
            result_1_symbol_bit = major_bits + minor_bits
            result_1_symbol_bit = [
                " ".join(result_1_symbol_bit[j * 8 : (j + 1) * 8] for j in range(4))
            ]
            bit_list.append(result_1_symbol_bit[0])
    return bit_list


def get_unicode_code(s: str) -> list[str]:
    code_list = [
        f"U+{hex(ord(i)).replace('x', '', 1).lstrip('0').zfill(4).upper()}" for i in s
    ]
    return code_list


def main():
    string_input = input("Enter a string: ")
    bit_code = get_16b(string_input)
    unicode = get_unicode_code(string_input)
    for i in range(len(string_input)):
        print("{}   {}   {}".format(string_input[i], unicode[i], bit_code[i]))


if __name__ == "__main__":
    main()
