# Напишите декоратор change, который делает так, что задекорированная
# функция принимает все свои не именованные аргументы в порядке,
# обратном тому, в котором их передали

#функция принимает все свои не именованные аргументы в порядке,
#обратном тому, в котором их передали
#тут тебе надо вызывать функцию свою изначальную с аргументами в обратном
# порядке, счас ты ее не вызываешь, а просто возвращаешь аргументы

def decorator_change(func):
    """
    This function-decorator reverses values from decorated function
    :param func:
    :return: wrapper
    """
    def wrapper(*tuples):
        new_tup = tuples[::-1]
        return func(new_tup)
    return wrapper


@decorator_change
def show_positional_args(*args):
    list_args = list(*args)
    return list_args


print(show_positional_args(1, 2, 3, 4, 5, 6, 7))