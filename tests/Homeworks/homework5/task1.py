import pytest
from io import StringIO
from src.Homeworks.homework5.task1.task1 import *


@pytest.mark.parametrize(
    "char, expected", [("A", ["U+0041"]), ("Æ", ["U+00C6"]), ("흔", ["U+D754"])]
)
def test_get_unicode_code(char, expected):
    assert get_unicode_code(char) == expected


@pytest.mark.parametrize(
    "char, expected",
    [
        ("ﺻ", ["11111110 10111011"]),
        ("𐍇", ["11011000 00000000 11011111 01000111"]),
        ("𐏊", ["11011000 00000000 11011111 11001010"]),
    ],
)
def test_get_16b(char, expected):
    assert get_16b(char) == expected


@pytest.mark.parametrize(
    "input_line, expected",
    [
        (
            "Hello, World!",
            "H   U+0048   00000000 01001000\ne   U+0065   00000000 01100101\nl   U+006C   00000000 01101100\nl   U+006C   00000000 01101100\no   U+006F   00000000 01101111\n,   U+002C   00000000 00101100\n    U+0020   00000000 00100000\nW   U+0057   00000000 01010111\no   U+006F   00000000 01101111\nr   U+0072   00000000 01110010\nl   U+006C   00000000 01101100\nd   U+0064   00000000 01100100\n!   U+0021   00000000 00100001\n",
        ),
        (
            "我爱一只猫",
            "我   U+6211   01100010 00010001\n爱   U+7231   01110010 00110001\n一   U+4E00   01001110 00000000\n只   U+53EA   01010011 11101010\n猫   U+732B   01110011 00101011\n",
        ),
    ],
)
def test_main(monkeypatch, input_line, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_line)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
