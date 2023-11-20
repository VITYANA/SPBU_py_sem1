def transform_from_decimal_to_binary(num, bit_count):
    original_num = num
    original_num = abs(original_num)
    binary_num = ""
    while original_num > 0:
        binary_num += str(original_num % 2)
        original_num //= 2
        if len(binary_num) > bit_count - 1:
            raise ValueError("Overflow")
    binary_num = add_zero(binary_num, bit_count)
    if num >= 0:
        binary_num_sign = "0"
    else:
        binary_num_sign = "1"
    binary_num += binary_num_sign
    return binary_num[::-1]


def add_zero(binary_num, bit_count):
    while len(binary_num) < bit_count - 1:
        binary_num += "0"
    return binary_num


def reverse_binary_transform(binary_num):
    reverse_binary_num = binary_num
    if not (binary_num[0] == "1"):
        return reverse_binary_num
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
    if not reverse_bin_num[0] == "1":
        return additional_binary_num
    reverse_bin_num = reverse_bin_num[::-1]
    additional_binary_num = ""
    carry = 1
    for i in range(len(reverse_bin_num)):
        additional_binary_num += str((int(reverse_bin_num[i]) + carry) % 2)
        carry = (int(reverse_bin_num[i]) + carry) // 2
    return additional_binary_num[::-1]


def sum_in_binary(num_1, num_2):
    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    sum_result = ""
    carry = 0
    for i in range(len(num_1)):
        sum_result += str((int(num_1[i]) + int(num_2[i]) + carry) % 2)
        carry = (int(num_1[i]) + int(num_2[i]) + carry) // 2
    return sum_result[::-1]


def get_binary_from_additional(binary, depth):
    result_str = binary
    if not binary[0] == "1":
        return result_str[::-1]
    result_str = reverse_binary_transform(binary)
    result_str = sum_in_binary(
        result_str,
        additional_binary_transform(
            reverse_binary_transform(transform_from_decimal_to_binary(1, depth))
        ),
    )
    return result_str[::-1]


def binary_to_decimal(binary, depth):
    result_str = get_binary_from_additional(binary, depth)
    result_num = 0
    for i in range(len(result_str) - 1):
        result_num += int(result_str[i]) * 2**i
    if binary[0] == "1":
        result_num *= -1
    return result_num


def check_input(num1, num2, bit_count):
    check_flag = True
    try:
        transform_from_decimal_to_binary(num1, bit_count)
    except Exception as err:
        check_flag = False
        print(f"{err}: Can't transform {num1} to binary with {bit_count} bit count.")
    try:
        transform_from_decimal_to_binary(num2, bit_count)
    except Exception as err:
        print(f"{err}: Can't transform {num2} to binary with {bit_count} bit count.")
        check_flag = False
    return check_flag


def results_out(num1, num2, bit_count):
    if not check_input(num1, num2, bit_count):
        return 0
    binary_number1 = transform_from_decimal_to_binary(num1, bit_count)
    binary_number2 = transform_from_decimal_to_binary(num2, bit_count)
    reverse_binary_number1 = reverse_binary_transform(binary_number1)
    reverse_binary_number2 = reverse_binary_transform(binary_number2)
    additional_binary_num1 = additional_binary_transform(reverse_binary_number1)
    additional_binary_num2 = additional_binary_transform(reverse_binary_number2)
    sum_of_nums = sum_in_binary(additional_binary_num1, additional_binary_num2)
    decimal_num_sum = binary_to_decimal(sum_of_nums, bit_count)
    num2_for_differ = additional_binary_transform(
        reverse_binary_transform(transform_from_decimal_to_binary(-num2, bit_count))
    )
    differ = sum_in_binary(additional_binary_num1, num2_for_differ)
    decimal_num_differ = binary_to_decimal(differ, bit_count)
    print(f"numbers in binary:")
    print(f"   1) binary x: {binary_number1}")
    print(f"      binary y: {binary_number2}")
    print(f"   2) reverse binary x: {reverse_binary_number1}")
    print(f"      reverse binary y: {reverse_binary_number2}")
    print(f"   3) additional binary x: {additional_binary_num1}")
    print(f"      additional binary y: {additional_binary_num2}")
    print(f"sum:")
    print(
        f"   in binary: {additional_binary_num1} + {additional_binary_num2} = {sum_of_nums}"
    )
    print(f"   in decimal: {num1} + {num2} = {decimal_num_sum}")
    print(f"differ:")
    print(f"   in binary: {additional_binary_num1} - {num2_for_differ} = {differ}")
    print(f"   in decimal: {num1} - {num2} = {decimal_num_differ}")


if __name__ == "__main__":
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    bit_depth = int(input("Enter bit count in your numbers in binary: "))
    results_out(number_1, number_2, bit_depth)
