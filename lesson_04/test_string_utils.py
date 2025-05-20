import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Позитивные тесты

# Делает первую букву заглавной
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Удаляет пробелы в начале
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    ("  Skypro123", "Skypro123"),
    ("  Skypro 123", "Skypro 123")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Возвращает True или False
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Удаляет все подстроки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "pro", "Sky"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


# Негативные проверки

# Делает первую букву заглавной
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Удаляет пробелы в начале
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", "")

])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Возвращает True или False
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "U", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Удаляет все подстроки
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "u", "SkyPro")  # Пример с символом, которого нет в строке
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
