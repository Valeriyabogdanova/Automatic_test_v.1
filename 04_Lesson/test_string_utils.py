import  pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_str",
                          [("moscow", "Moscow"),
                           ("no doubt", "No doubt"),
                           ("false", "False"),])

def test_capitalise_positive(input_str, expected_str):
     assert string_utils.capitalize(input_str) == expected_str

@pytest.mark.parametrize("input_str, expected",
                         [("  Hello", "Hello"),
                          (" my name is", "my name is"),])

def test_trim_positive(input_str, expected):
    assert  string_utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, symbol, res",
                         [("House", "H", True),
                          ("Kill it", "N", False),])

def test_contains_positive(input_str, symbol, res):
    assert string_utils.contains(input_str,symbol) == res

@pytest.mark.parametrize("input_str, symbol, result",
                         [("Monster", "M", "onster"),
                          ("Dollar", "Dol", "lar"),])

def test_delete_symbol_positive(input_str, symbol, result):
    assert  string_utils.delete_symbol(input_str, symbol) == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_str",
                          [("", ""),
                           ("  ", "  "),
                           ("123", "123"),])

def test_capitalise_negative(input_str, expected_str):
     assert string_utils.capitalize(input_str) == expected_str