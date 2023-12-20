import random


COLOR = "█"


def main():
    sprite_size = input("Input sprite side size: ")
    if not sprite_size.isdigit():
        print("Sprite size need to be digit.")
        return 0
    sprite_size = int(sprite_size)
    while input() == "":
        symmetry_type = random.randint(0, 2)
        matrix = create_sprite(sprite_size, symmetry_type)
        for row in matrix:
            print("".join(row))


def create_sprite(sprite_size, symmetry_type):
    matrix = generate_matrix(sprite_size)
    match symmetry_type:
        case 1:
            matrix = vertical_symmetry(matrix, sprite_size)
        case 2:
            matrix = horizontal_symmetry(matrix, sprite_size)
        case 3:
            matrix = horizontal_symmetry(
                vertical_symmetry(matrix, sprite_size), sprite_size
            )
    return matrix


def horizontal_symmetry(matrix, sprite_size):
    for x in range((sprite_size // 2) + 1):
        matrix[sprite_size - 1 - x] = matrix[x]
    return matrix


def vertical_symmetry(matrix, sprite_size):
    hor_sym_matrix = horizontal_symmetry(matrix, sprite_size)
    matr_transpos = [
        [hor_sym_matrix[i][j] for i in range(sprite_size)] for j in range(sprite_size)
    ]
    return matr_transpos


def generate_matrix(sprite_size):
    matrix = [
        [COLOR if random.randint(0, 1) == 1 else " " for j in range(sprite_size)]
        for i in range(sprite_size)
    ]
    return matrix


if __name__ == "__main__":
    main()
