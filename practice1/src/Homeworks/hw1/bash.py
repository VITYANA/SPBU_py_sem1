import sys
import os


def find_file(name, directory):
    for root, dirs, files in os.walk(directory):
        if name in files:
            return os.path.join(root, name)


def return_head_lines(string, parameter):
    i = 0
    current_strings = 0
    final_string = ''
    while i != len(string) and current_strings != parameter:
        if string[i] == '\n':
            final_string += string[i]
            current_strings += 1
            i += 1
        else:
            final_string += string[i]
            i += 1
    return final_string


def return_head_bytes(string, parameter):
    final_string = ''
    current_bytes = 0
    i = 0
    while i != len(string) and current_bytes != parameter:
        final_string += string[i]
        i += 1
        current_bytes += len(string[i].encode('utf-8'))
    return final_string


def return_tail_lines(string, parameter):
    final_string = ''
    reversed_string = string[::-1]
    i = 0
    current_lines = 0
    while i != len(string) and current_lines != parameter:
        if reversed_string[i] == "\n":
            final_string += reversed_string[i]
            i += 1
            current_lines += 1
        else:
            final_string += reversed_string[i]
            i += 1
    return final_string[::-1]


def return_tail_bytes(string, parameter):
    final_string = ''
    reversed_string = string[::-1]
    current_bytes = 0
    i = 0
    while i != len(string) and current_bytes != parameter:
        current_bytes += len(reversed_string[i].encode('utf-8'))
        final_string += reversed_string[i]
        i += 1
    return final_string[::-1]


if __name__ == "__main__":
    file_get = find_file(sys.argv[-1], "/")
    main_function_name = (sys.argv[1])
    args = sys.argv[2:-1]
    file = open(file_get).read()
    if main_function_name == "wc":
        result = []
        if "-l" in args:
            result.append(file.count("\n"))
        if "-w" in args:
            result.append(file.count(" "))
        if "-c" in args:
            result.append(os.path.getsize(file_get))
        if "-m" in args:
            result.append(len(file))
        print(*result, sys.argv[-1])
    elif main_function_name == "head":
        number = int(sys.argv[3])
        if "-n" in args:
            print(return_head_lines(file, number))
        elif "-c" in args:
            print(return_head_bytes(file, number))
    elif main_function_name == "tail":
        number = int(sys.argv[3])
        if "-n" in args:
            print(return_tail_lines(file, number))
        elif "-c" in args:
            print(return_tail_bytes(file, number))
