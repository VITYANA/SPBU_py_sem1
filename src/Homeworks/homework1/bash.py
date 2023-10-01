import sys
import os


def find_file(name, directory):
    for root, dirs, files in os.walk(directory):
        if name in files:
            return os.path.join(root, name)


def return_head_lines(file, parameter):
    final_list = []
    i = 0
    with open(file) as file_in:
        for lines in file_in:
            if i == parameter:
                break
            final_list.append(lines)
            i += 1
    return "".join(final_list)


def return_head_bytes(file, parameter):
    final_arr = b""
    i = 0
    with open(file) as file_in:
        for lines in file_in:
            while i != parameter:
                final_arr += lines[i].encode()
                i += len(lines[i])
    return final_arr.decode()


def return_tail_lines(file, parameter):
    final_list = []
    reversed_list = open(file).read()[::-1]
    i = 0
    current_lines = 0
    while i != len(file) and current_lines != parameter:
        if reversed_list[i] == "\n":
            final_list.append(reversed_list[i])
            i += 1
            current_lines += 1
        else:
            final_list.append(reversed_list[i])
            i += 1
    return "".join(final_list[::-1])


def return_tail_bytes(string, parameter):
    final_string = ""
    reversed_string = string[::-1]
    current_bytes = 0
    i = 0
    while i != len(string) and current_bytes != parameter:
        current_bytes += len(reversed_string[i].encode("utf-8"))
        final_string += reversed_string[i]
        i += 1
    return final_string[::-1]


if __name__ == "__main__":
    file_get = find_file(sys.argv[-1], "/")
    main_function_name = sys.argv[1]
    args = sys.argv[2:-1]
    if main_function_name == "wc":
        result = []
        l = 1
        w = 0
        c = 0
        m = 0
        with open(file_get) as file_start:
            for lines in file_start:
                if "\n" in lines:
                    l += 1
                w += lines.count(" ")
                m += len(lines)
        if "-l" in args:
            result.append(l)
        if "-w" in args:
            result.append(w + l)
        if "-c" in args:
            result.append(os.path.getsize(file_get))
        if "-m" in args:
            result.append(m)
        print(*result, sys.argv[-1])
    elif main_function_name == "head":
        number = int(sys.argv[3])
        if "-n" in args:
            print(return_head_lines(file_get, number))
        elif "-c" in args:
            print(return_head_bytes(file_get, number))
    elif main_function_name == "tail":
        number = int(sys.argv[3])
        if "-n" in args:
            print(return_tail_lines(file_get, number))
        elif "-c" in args:
            print(return_tail_bytes(file_get, number))
