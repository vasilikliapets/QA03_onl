import pytest
from function_1 import check_lower
from function_2 import set_float, InputTypeError
from function_3 import check_punctuation


@pytest.mark.parametrize('word', ['type', 'world', 'cold'])
def test_check_lower_pos(word, get_time, get_name, count_time):
    """test for positive"""
    assert check_lower(word) is True


@pytest.mark.parametrize('word', ["God", 'America', 'USA_12'])
def test_check_lower_neg(word):  # test for negative
    assert check_lower(word) is False


@pytest.mark.parametrize('var_1', [1, 2.5, 889])
def test_set_float_pos(var_1):
    assert isinstance(set_float(var_1), float)


@pytest.mark.parametrize('var_1', [{12, 18}, (), []])
def test_set_float_neg(var_1):
    assert isinstance(set_float(var_1), float) is False


@pytest.mark.parametrize('var_1', "r")
def test_set_float_err(var_1):
    with pytest.raises(InputTypeError):
        set_float(var_1)


@pytest.mark.parametrize('symbol', "!@#")
def test_check_punctuation_pos(symbol):
    assert check_punctuation(symbol) is True


@pytest.mark.parametrize('symbol', "str")
def test_check_punctuation_neg(symbol):
    assert check_punctuation(symbol) is False
