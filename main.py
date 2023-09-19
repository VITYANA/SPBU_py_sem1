import csv

def find_matches(file_in):
    words_count = []
    with open(file_in) as file:
        for lines in file:
            lines = sorted(lines.split())
            i = 0
            while i != len(lines):
                if lines[i] not in words_count:
                    words_count.append([lines[i], int(lines.count(lines[i]))])
                    i += lines.count(lines[i])
    i = 0
    while i != len(words_count):
        j = i + 1
        while j != len(words_count):
            if words_count[j][0] == words_count[i][0]:
                words_count[i][1] += words_count[j][1]
                del words_count[j]
            else:
                j += 1
        words_count[i][1] = str(words_count[i][1])
        i += 1
    return words_count


if __name__ == "__main__":
    file_path_in = input("Введите путь до файла, подлежащего анализу: ")
    file_path_out = input("Введите путь до файла, в который нужно передать результаты анализа: ")
    final_str = find_matches(file_path_in)
    with open(file_path_out, "a") as csv_file:
        writer = csv.writer(csv_file)
        for i in range(len(final_str)):
            writer.writerow(final_str[i])
