class InputTypeError(Exception):  # собственная ошибка
    pass


def set_float(var_1):
    if isinstance(var_1, (int, float)):  # проверка формата
        var_1 = float(var_1)  # приведение к float
    elif isinstance(var_1, str):
        raise InputTypeError("Функция не принимает строки")
    return var_1
