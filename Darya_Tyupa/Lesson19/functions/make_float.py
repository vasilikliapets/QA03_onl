class InputTypeError(Exception):
    """My own exception"""


def make_float(number):
    """This function returns float number or exception"""
    if isinstance(number, (int, float)):
        return float(number)
    else:
        raise InputTypeError('Incorrect type of number')


