class InputTypeError(Exception):
    pass


def type_float(number):
    """
    Function swap 'int' to 'float'
    """
    if isinstance(number, (int, float)):
        number = float(number)
    elif isinstance(number, str):
        raise InputTypeError
    return number
