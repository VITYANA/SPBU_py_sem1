from sys import argv
from os.path import exists
from collections import Counter
import re


def get_str(file_name):
    with open(file_name, "r") as file:
        str_input = str(file.readlines())
        reg = re.compile("[^a-zA-Z]")
    return reg.sub("", str(str_input))


def count_chars(string):
    dict_of_chars = Counter(list(string))
    return dict_of_chars


def sort_dict(string):
    return dict(sorted(string.items()))


def write_file(file_name, sorted_dict):
    with open(file_name, "w") as file:
        for key, val in sorted_dict.items():
            file.write("{}: {}\n".format(key, val))
    return True


def file_check(read_file_name, write_file_name):
    if not (exists(read_file_name)):
        print(f"не существует {read_file_name}")
        return False
    if exists(write_file_name):
        print(f"файл {write_file_name} уже существует")
        return False
    return True


def main():
    read_file_name, write_file_name = argv[1:]
    if file_check(read_file_name, write_file_name):
        string_input = get_str(read_file_name)
        dict_of_chars = count_chars(string_input)
        sorted_dict = sort_dict(dict_of_chars)
        write_file(write_file_name, sorted_dict)


if __name__ == "__main__":
    main()
