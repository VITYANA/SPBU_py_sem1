class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        n = self
        while n.next:
            n = n.next
        n.next = end


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
    with open(file_in) as file:
        for lines in file:
            if i < 3:
                if i == 1:
                    linked_list = Node(lines)
                    linked_list_n = linked_list
                    i += 1
                else:
                    parameters.append(lines.rstrip())
                    i += 1
            else:
                start_line = lines[lines.find("[") + 1:lines.find("]")]
                fragment_line = lines[lines.rfind("[") + 1:lines.rfind("]")]
                if lines[:lines.find("[")] == "INSERT":
                    linked_list.append(insert(linked_list_n.data, start_line, fragment_line))
                elif lines[:lines.find("[")] == "REPLACE":
                    linked_list.append(replace(linked_list_n.data, start_line, fragment_line))
                elif lines[:lines.find("[")] == "DELETE":
                    linked_list.append(delete(linked_list_n.data, start_line, fragment_line))
                linked_list_n = linked_list_n.next
    with open(file_out, 'w') as file:
        node = linked_list
        file.write(node.data)
        while node.next:
            node = node.next
            file.write(node.data)


if __name__ == "__main__":
    dna_in = input("Введите путь до файла с изначальным ДНК: ")
    dna_out = input("Введите путь до файла, в котором будет содержаться конечная последовательность ДНК: ")
    find_dna(dna_in, dna_out)
