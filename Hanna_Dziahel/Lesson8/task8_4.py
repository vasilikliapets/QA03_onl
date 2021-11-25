# Напишите декоратор func_name, который выводит на экран
# имя функции (func.__name__)

def decorator_func_name(func):
    """
    This function-decorator prints decorated function name
    :param func:
    :return: wrapper
    """
    def wrapper(*args):
        result = func(*args)
        if args == ():
            return func.__name__
        else:
            string = func.__name__ + "\n" + str(list(result))
            return string
    return wrapper


@decorator_func_name
def honey_text():
    return ("cute kitten")


# Используем __name__== '__main__', так как будем запускать декоратор из
# этого модуля в другом модуле, чтобы в нем не выполнился запуск функций
# из этого модуля
if __name__ == '__main__':
    print("Имя функции: ", honey_text())

