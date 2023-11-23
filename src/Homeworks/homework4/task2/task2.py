def int_to_bin(integer_part):
    integer_part = int(integer_part)
    if integer_part == 0:
        return "0"
    result_num = ""
    while integer_part > 0:
        result_num += str(integer_part % 2)
        integer_part //= 2
    return result_num[::-1]


def float_to_bin(float_part, float_part_depth):
    result_num = ""
    float_part = float("0." + float_part)
    while float_part > 0 and len(result_num) < float_part_depth:
        result_num += str(int((float_part * 2) // 1))
        float_part = (float_part * 2) % 1
    return result_num


def decimal_to_binary(float_part, float_part_depth):
    index_of_point = float_part.find(".")
    integer_part = float_part[:index_of_point]
    float_part = float_part[index_of_point + 1 :]
    integer_part_in_bin = int_to_bin(integer_part)
    float_part_in_bin = float_to_bin(float_part, float_part_depth)
    return integer_part_in_bin + "." + float_part_in_bin


def exponential(bin_str_float_num):
    index_of_point = bin_str_float_num.find(".")
    if bin_str_float_num[:index_of_point] == "0":
        num_order = len(
            bin_str_float_num[index_of_point + 1 : bin_str_float_num.find("1")]
        )
        num_order_sign = "-"
    else:
        num_order = len(bin_str_float_num[:index_of_point])
        num_order_sign = ""
    return (
        "0."
        + bin_str_float_num[:index_of_point]
        + bin_str_float_num[index_of_point + 1 :]
        + "*2^"
        + num_order_sign
        + str(num_order)
    )


def normalize_for_save(num, int_part_depth, float_part_depth, sign):
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    index_of_point = num.find(".")
    int_part = num[:index_of_point]
    int_part = int_part[::-1]
    float_part = num[index_of_point + 1 :]
    int_part += "0" * (int_part_depth - len(int_part))
    float_part += "0" * (float_part_depth - len(float_part))
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
    bin_str_float_num = decimal_to_binary(str(abs(float(num))), int_part_depth)
    save_num = normalize_for_save(
        bin_str_float_num, int_part_depth, float_part_depth, sign
    )
    res_num = sign + exponential(bin_str_float_num)
    print(f"Result: {res_num}")
    print(f"Save as {save_num}")


if __name__ == "__main__":
    main()
