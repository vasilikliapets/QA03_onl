# Напишите декоратор, который вычисляет время работы
# декорируемой функции (timer)

# Импортируем модуль time
import time

my_list = range(1,100)


def timer(func):
    """
    This function-decorator calculates the running time of the decorated
    function
    :param func:
    :return: wrapper
    """
    def wrapper(list):
        start_time = time.time()
        # Запишем выполнение функции в переменную
        result = func(list)
        # Используем sleep() для того, чтобы увеличить время выполнения функции
        time.sleep(2)
        end_time = time.time()
        print('Время выполнения = {}'.format(end_time-start_time))

        # Вернем значение выполнения функции здесь, так как у декоратора
        # есть свойство поглощать значение функции и вернется просто None,
        # если потом выполнить нашу функцию
        return result
    return wrapper


@timer
def sort_list(list):
    return sorted(list, reverse=True)


# Используем __name__== '__main__', так как будем запускать декоратор из
# этого модуля в другом модуле, чтобы в нем не выполнился запуск функций
# из этого модуля
if __name__ == '__main__':
    print(sort_list(my_list))