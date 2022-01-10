import pytest

from lower_case import lower_case
from type_float import type_float
from simbol import is_simbol
from type_float import InputTypeError



@pytest.mark.parametrize('word', ['qwert', 'qwERT', 'abxd'])
def test_lower_case(word, file_name, start_time, run_time):
    assert lower_case(word) is True

@pytest.mark.parametrize('number', [45, 456, 'hr'])
def test_type_float(number, file_name, start_time, run_time):
    assert isinstance(type_float(number), float)

@pytest.mark.parametrize('number', [45, 456, 'hr'])
def test_type_float_error(number, file_name, start_time, run_time):
    assert InputTypeError

@pytest.mark.parametrize('simbol', ['*', '$', 'r'])
def test_is_simbol(simbol, file_name, start_time, run_time):
    assert is_simbol(simbol) == True