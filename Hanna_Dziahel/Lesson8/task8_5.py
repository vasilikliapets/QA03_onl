# Напишите декоратор change, который делает так, что задекорированная
# функция принимает все свои не именованные аргументы в порядке,
# обратном тому, в котором их передали

def decorator_change(func):
    """
    This function-decorator reverses values from decorated function
    :param func:
    :return: wrapper
    """
    def wrapper(*tuples):
        new_tup = tuples[::-1]
        return new_tup
    return wrapper


@decorator_change
def show_positional_args(*args):
    tuple_args = args
    return tuple_args


print(show_positional_args(1, 2, 3, 4, 5, 6, 7))