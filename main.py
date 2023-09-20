import csv


def find_matches(file_in):
    words_count = {}
    with open(file_in) as file:
        for lines in file:
            for element in lines.split():
                if words_count.get(element, None):
                    words_count[element] += 1
                else:
                    words_count[element] = 1
    return words_count


if __name__ == "__main__":
    file_path_in = input("Введите путь до файла, подлежащего анализу: ")
    file_path_out = input("Введите путь до файла, в который нужно передать результаты анализа: ")
    final_dict = find_matches(file_path_in)
    with open(file_path_out, "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(final_dict.items())
