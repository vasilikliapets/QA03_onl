import time


def before_after(func):
    """Пишет Before и After"""

    def wrapper(*args):
        print("Before")
        res = func(*args)
        print("After")
        return res

    return wrapper


def func_2(func):
    """Добавляет 1 к заданному числу функции"""

    def wrapper(*args):
        result = func(*args) + 1
        return print(result)

    return wrapper


def upper_func(func):
    """Переводит полученную строку в верхний регистр"""

    def wrapper(arg1):
        return func(arg1).upper()

    return wrapper


def func_name(func):
    """Выводит имя функции на экран"""

    def wrapper(*args):
        a = func.__name__  # Встроенный метод по возврату имени функции
        func(*args)
        return print(a)

    return wrapper


def change(func):
    """функция принимает все свои не именованные аргументы в порядке, обратном тому, в котором их передали"""

    def wrapper(*args):
        li = args[::-1]  # Срез листа в обратном порядке
        return func(li)

    return wrapper


def timer(func):
    """Таймер выполнения функции"""

    def wrapper(*args):
        start_time = time.perf_counter_ns()  # Время начала
        res = func(*args)
        print(f"{time.perf_counter_ns() - start_time} наносекунд")  # Время окончания минус время начала (в наносекундах!)
        return res

    return wrapper
