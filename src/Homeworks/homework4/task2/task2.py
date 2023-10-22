def int_to_bin(num):
    if int(num) == 0:
        return "0"
    result_num = ""
    num = int(num)
    while num > 0:
        result_num += str(num % 2)
        num //= 2
    return result_num[::-1]


def float_to_bin(num, float_len):
    result_num = ""
    num = float("0." + num)
    while num > 0 and len(result_num) < float_len:
        result_num += str(int((num * 2) // 1))
        num = (num * 2) % 1
    return result_num


def decimal_to_binary(num, float_part_len):
    integer_part = num[: num.find(".")]
    float_part = num[num.find(".") + 1 :]
    integer_part_in_bin = int_to_bin(integer_part)
    float_part_in_bin = float_to_bin(float_part, float_part_len)
    return integer_part_in_bin + "." + float_part_in_bin


def exponential(num):
    if num[: num.find(".")] == "0":
        p = len(num[num.find(".") + 1 : num.find("1")])
        p_sign = "-"
    else:
        p = len(num[: num.find(".")])
        p_sign = ""
    return (
        "0." + num[: num.find(".")] + num[num.find(".") + 1 :] + "*2^" + p_sign + str(p)
    )


def normalize_for_save(num, int_part_len, float_part_len, sign):
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    int_part = num[: num.find(".")]
    int_part = int_part[::-1]
    float_part = num[num.find(".") + 1 :]
    while len(int_part) < int_part_len:
        int_part += "0"
    while len(float_part) < float_part_len:
        float_part += "0"
    final_form = sign + int_part[::-1] + float_part
    return " ".join(final_form[i * 8 : (i + 1) * 8] for i in range(8))


def main():
    num = input("Enter float number: ")
    int_part_depth = 0
    float_part_depth = 0
    if float(num) >= 0:
        sign = "+"
    else:
        sign = "-"
    form = input("Enter format of number(1, 2 or 3):\n1) FP16\n2) FP32\n3) FP64\n")
    match form:
        case "1":
            int_part_depth = 5
            float_part_depth = 10
        case "2":
            int_part_depth = 8
            float_part_depth = 23
        case "3":
            int_part_depth = 11
            float_part_depth = 52
    bin_int_float_num = decimal_to_binary(str(abs(float(num))), int_part_depth)
    save_num = normalize_for_save(
        bin_int_float_num, int_part_depth, float_part_depth, sign
    )
    res_num = sign + exponential(bin_int_float_num)
    print(f"Result: {res_num}")
    print(f"Save as {save_num}")


if __name__ == "__main__":
    main()
