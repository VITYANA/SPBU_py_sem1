import csv
import os


def find_matches(file_in):
    words_count = {}
    with open(file_in) as file:
        for lines in file:
            for element in lines.split():
                if element in words_count:
                    words_count[element] += 1
                else:
                    words_count[element] = 1
    return words_count


if __name__ == "__main__":
    file_path_in = input("Введите путь до файла, подлежащего анализу: ")
    while not os.path.exists(file_path_in):
        file_path_in = input(
            "Путь до файла, подлежащего анализу, некорректный, попробуйте ещё раз:\n"
        )
    file_path_out = input(
        "Введите путь до файла, в который нужно передать результаты анализа: "
    )
    while not os.path.exists(file_path_out):
        file_path_out = input(
            "Введите путь до файла, в который нужно передать результаты анализа, некорректный, попробуйте ещё раз:\n"
        )
    final_dict = find_matches(file_path_in)
    with open(file_path_out, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(final_dict.items())
    print("Результаты анализа записаны.")
