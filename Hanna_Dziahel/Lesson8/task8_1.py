# Напишите декоратор, который печатает перед и после вызова функции
# слова “Before” and “After”).	Напишите декоратор, который печатает
# перед и после вызова функции слова “Before” and “After”


def decorator_print(func):
    """
    This fucntion-decorator prints words Before and After and returns
    decorated function between them
    :param func:
    :return: wrapper
    """

    def wrapper(*args):
        print("Before")
        result = func(*args)
        print(result)
        print("After")
        return result

    return wrapper


@decorator_print
def simple_function():
    return "I love Python"


# Используем __name__== '__main__', так как будем запускать декоратор из
# этого модуля в другом модуле, чтобы в нем не выполнился запуск функций
# из этого модуля
if __name__ == '__main__':
    simple_function()
