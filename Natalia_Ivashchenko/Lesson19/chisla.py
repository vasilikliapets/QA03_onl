class InputTypeError(Exception):
    pass


def check_number(chislo):
    if chislo.isnumeric():
        return float(chislo)
    else:
        raise InputTypeError


check_number('6')
