class InputTypeError(Exception):
    pass


def change_type(digit):
    """
    The function get should get digit and change type to float
    """
    if isinstance(digit, (int, float)):
        return float(digit)
    elif isinstance(digit, str):
        raise InputTypeError("Wrong type")
