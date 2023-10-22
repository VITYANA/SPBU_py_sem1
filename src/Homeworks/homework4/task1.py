def binary_transform(num, bit_count):
    origin_num = num
    num = abs(num)
    binary_num = ""
    while num:
        binary_num += str(num % 2)
        num //= 2
        if len(binary_num) > bit_count - 1:
            raise ValueError("Overflow")
    while len(binary_num) < bit_count - 1:
        binary_num += "0"
    if origin_num >= 0:
        binary_num += "0"
    else:
        binary_num += "1"
    return binary_num[::-1]


def reverse_binary_transform(binary_num):
    reverse_binary_num = binary_num
    if binary_num[0] == "1":
        binary_num = binary_num[::-1]
        reverse_binary_num = ""
        for i in range(len(binary_num) - 1):
            if binary_num[i] == "0":
                reverse_binary_num += "1"
            else:
                reverse_binary_num += "0"
        reverse_binary_num += "1"
        reverse_binary_num = reverse_binary_num[::-1]
    return reverse_binary_num


def additional_binary_transform(reverse_bin_num):
    additional_binary_num = reverse_bin_num
    if reverse_bin_num[0] == "1":
        reverse_bin_num = reverse_bin_num[::-1]
        add_1 = True
        additional_binary_num = ""
        for i in range(len(reverse_bin_num)):
            if reverse_bin_num[i] == "1":
                if add_1:
                    additional_binary_num += "0"
                else:
                    additional_binary_num += "1"
            else:
                if add_1:
                    additional_binary_num += "1"
                    add_1 = False
                else:
                    additional_binary_num += "0"
        additional_binary_num = additional_binary_num[::-1]
    return additional_binary_num


def sum_in_binary(num_1, num_2):
    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    sum_result = ""
    need_to_plus_1 = False
    for i in range(len(num_1)):
        if need_to_plus_1:
            sum_result += str((int(num_1[i]) + int(num_2[i]) + 1) % 2)
            if (int(num_1[i]) + int(num_2[i]) + 1) <= 1:
                need_to_plus_1 = False
        else:
            sum_result += str((int(num_1[i]) + int(num_2[i])) % 2)
            if int(num_1[i]) + int(num_2[i]) > 1:
                need_to_plus_1 = True
    sum_result = sum_result[::-1]
    return sum_result


def binary_to_decimal(binary, depth):
    result_str = binary
    if binary[0] == "1":
        result_str = reverse_binary_transform(binary)
        result_str = sum_in_binary(
            result_str,
            additional_binary_transform(
                reverse_binary_transform(binary_transform(1, depth))
            ),
        )
    result_num = 0
    result_str = result_str[::-1]
    for i in range(len(result_str) - 1):
        result_num += int(result_str[i]) * 2**i
    if binary[0] == "1":
        result_num *= -1
    return result_num


def results_out(num1, num2, bit_count):
    binary_number1 = binary_transform(num1, bit_count)
    binary_number2 = binary_transform(num2, bit_count)
    reverse_binary_number1 = reverse_binary_transform(binary_number1)
    reverse_binary_number2 = reverse_binary_transform(binary_number2)
    additional_binary_num1 = additional_binary_transform(reverse_binary_number1)
    additional_binary_num2 = additional_binary_transform(reverse_binary_number2)
    sum_of_nums = sum_in_binary(additional_binary_num1, additional_binary_num2)
    decimal_num_sum = binary_to_decimal(sum_of_nums, bit_count)
    num2_for_differ = additional_binary_transform(
        reverse_binary_transform(binary_transform(-num2, bit_count))
    )
    differ = sum_in_binary(additional_binary_num1, num2_for_differ)
    decimal_num_differ = binary_to_decimal(differ, bit_count)
    print(
        f"numbers in binary:\n   1) binary x: {binary_number1}\n      binary y: {binary_number2}\n"
        f"   2) reverse binary x: {reverse_binary_number1}\n      reverse binary y: {reverse_binary_number2}\n"
        f"   3) additional binary x: {additional_binary_num1}\n      additional binary y: {additional_binary_num2}\n"
        f"sum:\n   in binary: {additional_binary_num1} + {additional_binary_num2} = {sum_of_nums}\n"
        f"   in decimal: {num1} + {num2} = {decimal_num_sum}\n"
        f"differ:\n   in binary: {additional_binary_num1} - {num2_for_differ} = {differ}\n"
        f"   in decimal: {num1} - {num2} = {decimal_num_differ}"
    )


if __name__ == "__main__":
    number_1 = int(input("Введите 1 число: "))
    number_2 = int(input("Введите 2 число: "))
    bit_depth = int(input("Введите количество бит в представлении числа: "))
    results_out(number_1, number_2, bit_depth)
