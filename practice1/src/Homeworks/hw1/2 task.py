def multiply_vectors(coord):
    return int(coord[0]) * int(coord[3]) + int(coord[1]) * int(coord[4]) + int(coord[2]) * int(coord[5])


def length_1(coord):
    return ((int(coord[0])) ** 2 + (int(coord[1])) ** 2 + (int(coord[2])) ** 2) ** 0.5


def length_2(coord):
    return ((int(coord[3])) ** 2 + (int(coord[4])) ** 2 + (int(coord[5])) ** 2) ** 0.5


def angle_between_vectors(coord):
    return multiply_vectors(coord) / (length_1(coord) * length_2(coord))


def transposition(matr, x, y):
    matr_transpos = [matr[j][i] for i in range(x) for j in range(y)]
    matr_final = []
    n = 0
    for i in range(1, x * y + 1):
        if i % y == 0:
            matr_final.append(matr_transpos[n:i])
            n = i
    return "\n".join(map(str, matr_final))


def matrix_sum(matr_1, matr_2, x_1, y_1, x_2, y_2):
    if x_1 != x_2 or y_1 != y_2:
        return "Размеры матриц не соответствуют"
    else:
        matr_sum = [matr_1[i][j] + matr_2[i][j] for i in range(x_1) for j in range(y_1)]
        matr_final = []
        n = 0
        for i in range(1, x_1 * y_1 + 1):
            if i % y_1 == 0:
                matr_final.append(matr_sum[n:i])
                n = i
        return "\n".join(map(str, matr_final))


def multiply_matrix(matr_1, matr_2, x_1, y_2):
    if x_1 != y_2:
        return "Размеры матриц не соответствуют"
    else:
        matr_final = [[0 for i in range(x2)] for i in range(y1)]
        for i in range(y1):
            for j in range(x2):
                for k in range(x1):
                    matr_final[i][j] += matr_1[i][k] * matr_2[k][j]
        return "\n".join(map(str, matr_final))


if __name__ == "__main__":
    path = input("Введите с чем хотите работать: \n1.векторы \n2.матрицы\n")
    match path:
        case "1":
            vec_coord = list(
                map(int, input("Введите координаты векторов x1, y1, z1, x2, y2, z2 через пробел: ").split()))
            path_vector = input(
                "Введите коды операций, которыми хотите воспользоваться через пробел: \n1.скалярное произведение "
                "\n2.вычисление длины 1 вектора \n3.вычисление длины 2 вектора \n4.нахождение угла между векторами\n"
            )
            if "1" in path_vector:
                print("Скалярное произведение =", multiply_vectors(vec_coord))
            if "2" in path_vector:
                print("Длина 1 вектора =", length_1(vec_coord))
            if "3" in path_vector:
                print("Длина 2 вектора =", length_2(vec_coord))
            if "4" in path_vector:
                print("Угол между векторами =", angle_between_vectors(vec_coord))
        case "2":
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
                print(transposition(matr1, x1, y1), "\n")
            if '2' in path_matrix:
                print(transposition(matr2, x2, y2), "\n")
            if '3' in path_matrix:
                print(matrix_sum(matr1, matr2, x1, y1, x2, y2), "\n")
            if '4' in path_matrix:
                print(multiply_matrix(matr1, matr2, x1, y2))
