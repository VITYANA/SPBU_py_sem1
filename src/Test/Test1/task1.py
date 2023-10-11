import sys
import os


def find_file(name, directory):
    for root, dirs, files in os.walk(directory):
        if name in files:
            return os.path.join(root, name)
        else:
            return False


def file(name, directory):
    for root, dirs, files in os.walk(directory):
        if name in files:
            return True


def sort(file_in, file_out, a, b):
    first_out = []
    second_out = []
    third_out = []
    with open(file_in, "r") as file:
        for line in file:
            all_nums = line.split()
            for i in all_nums:
                if int(i) < a:
                    first_out.append(i)
                elif a <= int(i) <= b:
                    second_out.append(i)
                elif int(i) > b:
                    third_out.append(i)
    first_out.append("\n")
    second_out.append("\n")
    with open(file_out, "w") as file:
        file.write(" ".join(first_out))
        file.write(" ".join(second_out))
        file.write(" ".join(third_out))


if __name__ == "__main__":
    # if not os.path.isfile(sys.argv[-2]):
    #     print(f"No {sys.argv[-2]} file")
    # elif os.path.isfile(sys.argv[-1]):
    #     print(f"file {sys.argv[-1]} already exist")
    # else:
        file_in_get = find_file(sys.argv[-2], "/")
        file_out_get = find_file(sys.argv[-1], "/")
        first_num = int(sys.argv[1])
        second_num = int(sys.argv[2])
        sort(file_in_get, file_out_get, first_num, second_num)
