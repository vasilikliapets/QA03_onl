import pytest
import chisla
from chisla import InputTypeError
import letters_lower
import symbols


class TestPozitiv:
    @pytest.mark.parametrize('letters', ['sep', 'oct', 'nov'])
    def test_lower_letters(self, letters):
        assert letters_lower.check_letters(letters), True

    @pytest.mark.parametrize('chislo', ['3', '46', '23'])
#    @pytest.fixture(params=['3', '46', '23'])
    def test_numbers(self, chislo):
        assert chisla.check_number(chislo), float(int(chislo))

    @pytest.mark.parametrize('symbol', ['@', '?', '+'])
    def test_symbols(self, symbol):
        assert symbols.check_symbols(symbol), True


class TestForError:
    def test_error(self):
        with pytest.raises(InputTypeError): chisla.check_number('qwe')


if __name__ == '__main__':
    pytest.main()
