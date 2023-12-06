from os.path import exists
from src.Homeworks.homework6.task1.AVLtree import *


def add_command(tree, size, count):
    if tree.size != 0 and has_key(tree, size):
        put(tree, size, int(get_value(tree, size)) + int(count))
    else:
        put(tree, size, int(count))


def get_command(tree, size):
    return get_value(tree, size) if has_key(tree, size) else 0


def select_command(tree, size):
    if size is None:
        return -1
    size_exist = get_lower_bound(tree, size)
    if size_exist is None:
        return -1
    count_in_stock = get_value(tree, size_exist)
    if count_in_stock == 0:
        if get_upper_bound(tree, size_exist) != size:
            return select_command(tree, get_upper_bound(tree, size_exist))
        return -1
    if count_in_stock < 0:
        return -1
    put(tree, size_exist, count_in_stock - 1)
    return size_exist


def validate_files(input_file):
    if not exists(f"{input_file}"):
        raise ValueError(f"Command file {input_file} is not Exist")
    if exists("balance.txt"):
        raise ValueError("balance file is already exist")
    if exists("results.txt"):
        raise ValueError("results file is already exist")


def command_selection(tree, command, *args):
    args_len = len(args)
    match command:
        case "ADD":
            if args_len != 2:
                raise ValueError(f"ADD expected 2 argument, but {args_len} are given.")
            add_command(tree, *args)
        case "GET":
            if args_len != 1:
                raise ValueError(f"GET expected 1 argument, but {args_len} are given.")
            write_results(get_command(tree, *args))
        case "SELECT":
            if args_len != 1:
                raise ValueError(
                    f"SELECT expected 1 argument, but {args_len} are given."
                )
            select_size = select_command(tree, *args)
            write_results(select_size) if select_size >= 0 else write_results("SORRY")


def write_results(line):
    with open("results.txt", "a") as file:
        file.write(str(line) + "\n")


def write_balance(lst):
    with open("balance.txt", "a") as file:
        for pair in lst:
            file.write(f"{pair[0]} {pair[1]}\n")


def main():
    input_file = input("Enter file with commands: ")
    validate_files(input_file)
    tree = create_tree_map()
    with open(f"{input_file}") as file:
        for line in file.readlines():
            line = line.split(" ")
            command, args = line[0], list(map(int, line[1:]))
            command_selection(tree, command, *args)
    write_balance(list(filter(lambda pair: pair[1] > 0, traverse(tree, "postorder"))))


if __name__ == "__main__":
    main()
