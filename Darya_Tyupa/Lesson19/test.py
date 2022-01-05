import pytest
from functions.make_float import make_float, InputTypeError
from functions.check_case import check_case
from functions.check_character import check_special_character


#т.к. тесты должны выполнятся по три раза, каждому тесту задаём по три параметра

@pytest.mark.parametrize('word', ['dasha', 'a', '12_bla'])    #проверка на True
def test_check_case_true(word, time_of_execution, scope_name, time_between_executions):
    # assert check_case(word) is True
    assert check_case(word)


@pytest.mark.parametrize('word', ['dasHa', 'CAT', 'kaptch_A'])    #проверка на False
def test_check_case_false(word, time_between_executions):
    # assert check_case(word) is False
    assert not check_case(word)

@pytest.mark.parametrize('number', [32, 0, -1])
def test_make_float(number, time_between_executions):
    assert type(make_float(number)) is float


@pytest.mark.parametrize('number', ['1', 'cat', '0'])    #тест который ожидает ошибку
def test_make_float_exception(number, time_between_executions):
    with pytest.raises(InputTypeError):
        make_float(number)


@pytest.mark.parametrize('character', ['-', '%', '.'])     #проверка на True
def test_check_special_character_true(character, time_between_executions):
    assert check_special_character(character)


@pytest.mark.parametrize('character', [1, 'a', [1]])     #проверка на False
def test_check_special_character_false(character, time_between_executions):
    assert check_special_character(character) is False
