import os


def insert(line, start, fragment):
    line_before_frag = line[:line.find(start) + len(start)]
    line_after_frag = line[line.find(start) + len(start):]
    return line_before_frag + fragment + line_after_frag


def replace(line, start, fragment):
    line_before_frag = line[:line.find(start)]
    line_after_frag = line[line.find(start) + len(start):]
    return line_before_frag + fragment + line_after_frag


def delete(line, start, end):
    start_delete = line.find(start)
    new_line = line[start_delete + len(start):]
    end_delete = new_line.find(end) + len(end) + len(start)
    return line[:start_delete] + line[end_delete:]


def find_dna(file_in, file_out):
    i = 0
    parameters = []
    dna_steps = []
    with open(file_in) as file:
        for lines in file:
            if i < 3:
                if i == 1:
                    dna_steps.append(lines)
                    i += 1
                else:
                    parameters.append(lines.rstrip())
                    i += 1
            else:
                start_line = lines.split()[1]
                fragment_line = lines.split()[2]
                if lines.split()[0] == "INSERT":
                    dna_steps.append(insert(dna_steps[-1], start_line, fragment_line))
                elif lines.split()[0] == "REPLACE":
                    dna_steps.append(replace(dna_steps[-1], start_line, fragment_line))
                elif lines.split()[0] == "DELETE":
                    dna_steps.append(delete(dna_steps[-1], start_line, fragment_line))
    with open(file_out, 'w') as file:
        file.writelines(dna_steps)


if __name__ == "__main__":
    dna_in = input("Введите путь до файла с изначальным ДНК:\n")
    while not os.path.exists(dna_in):
        dna_in = input("Путь до файла с изначальным ДНК указан некорректно, попробуйте ещё раз:\n")
    dna_out = input("Введите путь до файла, в котором будут содержаться результаты экспериментов:\n")
    while not os.path.exists(dna_out):
        dna_out = input("Путь до файла, в котором будут содержаться результаты экспериментов, указан некорректно, попробуйте ещё раз:\n")
    find_dna(dna_in, dna_out)
