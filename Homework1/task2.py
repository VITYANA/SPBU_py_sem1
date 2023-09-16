def multiply_vectors(coord1, coord2):
    res = 0
    for i in range(len(coord1)):
        res += coord1[i] * coord2[i]
    return res


def length(coord):
    res = 0
    for i in range(len(coord)):
        res += coord[i] ** 2
    return res ** 0.5


def angle_between_vectors(coord1, coord2):
    return multiply_vectors(coord1, coord2) / (length(coord1) * length(coord2))


def match_vectors():
    vec_coord1 = list(
        map(int, input("Введите координаты вектора 1 через пробел: ").split()))
    vec_coord2 = list(
        map(int, input("Введите координаты вектора 2 через пробел: ").split()))
    path_vector = input(
        "Введите коды операций, которыми хотите воспользоваться через пробел: \n1.скалярное произведение "
        "\n2.вычисление длины 1 вектора \n3.вычисление длины 2 вектора \n4.нахождение угла между векторами\n")
    if "1" in path_vector:
        print("Скалярное произведение =", multiply_vectors(vec_coord1, vec_coord2))
    if "2" in path_vector:
        print("Длина 1 вектора =", length(vec_coord1))
    if "3" in path_vector:
        print("Длина 2 вектора =", length(vec_coord2))
    if "4" in path_vector:
        print("Угол между векторами =", angle_between_vectors(vec_coord1, vec_coord2))


def transposition(matr, x, y):
    matr_transpos = [[matr[i][j] for i in range(y)] for j in range(x)]
    return matr_transpos


def matrix_sum(matr_1, matr_2, x_1, y_1, x_2, y_2):
    if x_1 != x_2 or y_1 != y_2:
        print("Размеры матриц не соответствуют")
    else:
        matr_sum = [[matr_1[i][j] + matr_2[i][j] for i in range(x_1)] for j in range(y_1)]
        return matr_sum


def multiply_matrix(matr_1, matr_2, x_1, y_2, x_2, y_1):
    if x_1 != y_2:
        print("Размеры матриц не соответствуют")
    else:
        matr_final = [[sum(matr_1[j][i] * matr_2[i][k] for i in range(x_1)) for k in range(x_2)] for j in range(y_1)]
        return matr_final


def match_matrix():
    a = input("Введите кол-во столбцов и кол-во строк 1 матрицы: ").split()
    x1 = int(a[0])
    y1 = int(a[1])
    print("Введите 1 матрицу построчно, числа через пробел:")
    i = 0
    matr1 = []
    while i != y1:
        matr1.append(list(map(int, input().split())))
        i += 1
    a = input("Введите кол-во столбцов и кол-во строк 2 матрицы: ").split()
    x2 = int(a[0])
    y2 = int(a[1])
    print("Введите 2 матрицу построчно, числа через пробел:")
    i = 0
    matr2 = []
    while i != y2:
        matr2.append(list(map(int, input().split())))
        i += 1
    path_matrix = input("Введите коды операций, которой хотите воспользоваться: \n1.транспонирование 1 матрицы"
                        " \n2.транспонирование 2 матрицы \n3.сложение \n4.произведение\n")
    if '1' in path_matrix:
        print(*transposition(matr1, x1, y1), sep = "\n")
        print("\n")
    if '2' in path_matrix:
        print(*transposition(matr2, x2, y2), sep = "\n")
        print("\n")
    if '3' in path_matrix:
        print(*matrix_sum(matr1, matr2, x1, y1, x2, y2), sep = "\n")
        print("\n")
    if '4' in path_matrix:
        print(*multiply_matrix(matr1, matr2, x1, y2, x2, y1), sep = "\n")


if __name__ == "__main__":
    path = input("Введите с чем хотите работать: \n1.векторы \n2.матрицы\n")
    match path:
        case "1":
            match_vectors()
        case "2":
            match_matrix()
