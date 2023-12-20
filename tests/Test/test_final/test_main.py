from src.Test.Test_final.main import *
from io import StringIO
import pytest


# @pytest.mark.parametrize("input_line, input_int, expected", (
#                          ("ab", "1", "Sprite side size must be integer. Enter correct digit: \n"),
#                          ("", "1", "Sprite side size must be integer. Enter correct digit: \n"),
#                          ("int", "1", "Sprite side size must be integer. Enter correct digit: \n")))
# def test_validate_input(input_line, input_int, expected, monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda _: input_line)
#     fake_output = StringIO()
#     monkeypatch.setattr("sys.stdout", fake_output)
#     validate_input(input_line)
#     output = fake_output.getvalue()
#     return_value = validate_input(input_int)
#     assert output == expected and input_int == return_value


@pytest.mark.parametrize("size", (5, 10, 12))
def test_generate_matrix(size):
    matrix = generate_matrix(size)
    assert len(matrix) == size and (len(matrix[i]) == size for i in range(size))


@pytest.mark.parametrize(
    "matrix, sprite_size, expected",
    (
        (
            [
                [" ", "█", "█", " ", "█"],
                [" ", "█", " ", " ", " "],
                ["█", "█", " ", "█", "█"],
                ["█", "█", "█", " ", "█"],
                [" ", " ", "█", " ", "█"],
            ],
            5,
            [
                [" ", "█", "█", " ", "█"],
                [" ", "█", " ", " ", " "],
                ["█", "█", " ", "█", "█"],
                [" ", "█", " ", " ", " "],
                [" ", "█", "█", " ", "█"],
            ],
        ),
        (
            [
                ["█", " ", " ", "█"],
                [" ", " ", "█", " "],
                [" ", "█", " ", "█"],
                [" ", "█", " ", "█"],
            ],
            4,
            [
                ["█", " ", " ", "█"],
                [" ", " ", "█", " "],
                [" ", " ", "█", " "],
                ["█", " ", " ", "█"],
            ],
        ),
        (
            [[" ", " ", "█"], ["█", " ", "█"], [" ", "█", "█"]],
            3,
            [[" ", " ", "█"], ["█", " ", "█"], [" ", " ", "█"]],
        ),
    ),
)
def test_horizontal_symmetry(matrix, sprite_size, expected):
    hor_sym_matr = horizontal_symmetry(matrix, sprite_size)
    assert hor_sym_matr == expected


@pytest.mark.parametrize(
    "matrix, sprite_size, expected",
    (
        (
            [
                [" ", "█", "█", " ", "█"],
                [" ", "█", " ", " ", " "],
                ["█", "█", " ", "█", "█"],
                ["█", "█", "█", " ", "█"],
                [" ", " ", "█", " ", "█"],
            ],
            5,
            [
                [" ", " ", "█", " ", " "],
                ["█", "█", "█", "█", "█"],
                ["█", " ", " ", " ", "█"],
                [" ", " ", "█", " ", " "],
                ["█", " ", "█", " ", "█"],
            ],
        ),
        (
            [
                ["█", " ", " ", "█"],
                [" ", " ", "█", " "],
                [" ", "█", " ", "█"],
                [" ", "█", " ", "█"],
            ],
            4,
            [
                ["█", " ", " ", "█"],
                [" ", " ", " ", " "],
                [" ", "█", "█", " "],
                ["█", " ", " ", "█"],
            ],
        ),
        (
            [[" ", " ", "█"], ["█", " ", "█"], [" ", "█", "█"]],
            3,
            [[" ", "█", " "], [" ", " ", " "], ["█", "█", "█"]],
        ),
    ),
)
def test_vertical_symmetry(matrix, sprite_size, expected):
    ver_sym_matr = vertical_symmetry(matrix, sprite_size)
    assert ver_sym_matr == expected


@pytest.mark.parametrize(
    "sprite_size, symmetry_type", ((5, 0), (5, 1), (5, 2), (3, 0), (3, 1), (3, 2))
)
def test_create_sprite(sprite_size, symmetry_type):
    matrix = create_sprite(sprite_size, symmetry_type)
    assert len(matrix) == sprite_size and (
        len(matrix[i]) == sprite_size for i in range(sprite_size)
    )


@pytest.mark.parametrize(
    "matrix, sprite_size, expected",
    (
        (
            [
                [" ", "█", "█", " ", "█"],
                [" ", "█", " ", " ", " "],
                ["█", "█", " ", "█", "█"],
                ["█", "█", "█", " ", "█"],
                [" ", " ", "█", " ", "█"],
            ],
            5,
            [
                [" ", " ", "█", " ", " "],
                ["█", "█", "█", "█", "█"],
                ["█", " ", " ", " ", "█"],
                ["█", "█", "█", "█", "█"],
                [" ", " ", "█", " ", " "],
            ],
        ),
        (
            [
                ["█", " ", " ", "█"],
                [" ", " ", "█", " "],
                [" ", "█", " ", "█"],
                [" ", "█", " ", "█"],
            ],
            4,
            [
                ["█", " ", " ", "█"],
                [" ", " ", " ", " "],
                [" ", " ", " ", " "],
                ["█", " ", " ", "█"],
            ],
        ),
        (
            [[" ", " ", "█"], ["█", " ", "█"], [" ", "█", "█"]],
            3,
            [[" ", "█", " "], [" ", " ", " "], [" ", "█", " "]],
        ),
    ),
)
def test_horizontal_vertical_symmetry(matrix, sprite_size, expected):
    hor_vert_sym_matr = horizontal_symmetry(
        vertical_symmetry(matrix, sprite_size), sprite_size
    )
    assert hor_vert_sym_matr == expected


@pytest.mark.parametrize(
    "input_line, expected",
    (
        ("abc", "Sprite size need to be digit.\n"),
        (" ", "Sprite size need to be digit.\n"),
        ("ascasc", "Sprite size need to be digit.\n"),
    ),
)
def test_main_err(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
