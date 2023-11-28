from src.Homeworks.homework5.task2.task2 import *
import pytest


@pytest.mark.parametrize(
    "string, expected",
    (
        ("aaabbcccc", "a3b2c4"),
        ("abc", "a1b1c1"),
        ("aaaaaaaaaaaa", "a12"),
    ),
)
def test_encode(string, expected):
    assert encode(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    (("a0b0c0", ""), ("a1b2c3", "abbccc"), ("a10b2", "aaaaaaaaaabb")),
)
def test_decode(string, expected):
    assert decode(string) == expected


@pytest.mark.parametrize(
    "string, expected", (("a0b0c0", True), ("a1b2c3", True), ("a10b2", True))
)
def test_check_input_to_decode(string, expected):
    assert check_input_to_decode(string) == expected


@pytest.mark.parametrize(
    "string, expected", (("aaabbcccc", True), ("abc", True), ("aaaaaaaaaaaa", True))
)
def test_check_input_to_encode(string, expected):
    assert check_input_to_encode(string) == expected


@pytest.mark.parametrize(
    "string, expected", (("aa4b2", ValueError), ("", ValueError), ("abc", ValueError))
)
def test_check_input_to_decode_error(string, expected):
    with pytest.raises(expected):
        assert check_input_to_decode(string) == expected


@pytest.mark.parametrize(
    "string, expected", (("a1b2c3", ValueError), ("213", ValueError), ("", ValueError))
)
def test_check_input_to_encode_error(string, expected):
    with pytest.raises(expected):
        assert check_input_to_encode(string) == expected
