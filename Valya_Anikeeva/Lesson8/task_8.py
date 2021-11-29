import time


def dec_1(func):
    """декоратор, который печатает перед и после вызова функции слова
    “Before” and “After”"""

    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper


def dec_2(func):
    """функция декоратор, которая добавляет 1 к заданному числу"""

    def wrapper(*args):
        number = func(*args) + 1
        print(number)

    return wrapper


def dec_3(func):
    """функция декоратор, которая переводит полученный текст в
    верхний регистр"""

    def wrapper(text):
        print(text.upper())

    return wrapper


def func_name(func):
    """декоратор func_name, который выводит на экран имя функции
    (func.__name__)"""

    def wrapper(*args):
        print(func.__name__)
        print(func(*args))

    return wrapper


def change(func):
    """задекорированная функция принимает все свои не именованные аргументы в порядке,
    обратном  тому, в котором их передали"""

    def wrapper(*args):
        ls = args[::-1]
        return func(ls)

    return wrapper


def timer(func):
    """декоратор, который вычисляет время работы декорируемой функции (timer)"""

    def wrapper(*args):
        start_time = time.perf_counter()
        val = func(*args)
        print('time', time.perf_counter() - start_time)
        return val

    return wrapper
