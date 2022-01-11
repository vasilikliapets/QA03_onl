import pytest

from HM_19.hm_19_3func_1 import check_syllab
from HM_19.hm_19_3func_2 import InputTypeError
from HM_19.hm_19_3func_3 import check_spec_syllable


@pytest.mark.parametrize('word', ["hello", "dear", "guest"])
def test_hm19_func1_lowercase(check_time, word, name_file, time_session_test):
    assert check_syllab(word)  # is True писать?


@pytest.mark.parametrize('word', ["Last", "Dear", "God"])
def test_hm19_func1_lowercase2(word, time_session_test):
    assert check_syllab(word) is False
    # Или так лучше?
    # assert not check_syllab(word)


@pytest.mark.parametrize('numbers', ["asv", "12", "!@#"])
def test_hm19_func2_change_type(numbers, time_session_test):
    assert InputTypeError


@pytest.mark.parametrize('symb', ["!", "$", "&"])
def test_hm19_func3_spec_sillable(symb, time_session_test):
    assert check_spec_syllable(symb)
