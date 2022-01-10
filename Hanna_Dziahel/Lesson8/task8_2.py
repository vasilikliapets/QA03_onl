# Напишите функцию декоратор, которая добавляет 1 к заданному числу

def decorator_add(func):
    """
    This fucntion-decorator prints adds 1 to number from decorated function
    :param func:
    :return: wrapper
    """
    def wrapper(*args):

        return(func(*args)) + 1
    return wrapper


@decorator_add
def summa(number):
    return number


# Используем __name__== '__main__', так как будем запускать декоратор из
# этого модуля в другом модуле, чтобы в нем не выполнился запуск функций
# из этого модуля
if __name__ == '__main__':
    print(summa(5))
