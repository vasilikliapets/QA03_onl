# 1. Напишите декоратор, который печатает перед и после вызова функции слова “Before” and “After”
import time


def decorator1(func):
    """
    The decorator that prints the words "Before” and ”After" before and after the function call
    """

    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper


# 2. Напишите функцию декоратор, которая добавляет 1 к заданному числу
def decorator2(func):
    """
    The decorator function that adds 1 to a given number
    """

    def wrapper(*args):
        x = func(*args) + 1
        print(x)

    return wrapper


# 3. Напишите функцию декоратор, которая переводит полученный текст в верхний регистр
def decorator3(txt):
    """
    The decorator function that translates the resulting text into uppercase
    """

    def wrapper(txt):
        print(txt.upper())

    return wrapper


# 4. Напишите декоратор func_name, который выводит на экран имя функции (func.__name__)
def decorator4(func):
    """
    The func_name decorator that displays the function name (func.__name__)
    """

    def wrapper(*args):
        print(func.__name__)
        print(func(*args))

    return wrapper


# 5. Напишите декоратор change, который делает так, что задекорированная функция принимает все свои не именованные
# аргументы в порядке, обратном тому, в котором их передали
def decorator5(func):
    """
    The change decorator, which makes it so that the decorated function accepts all its unnamed the arguments are in the
     reverse order in which they were passed
    """

    def wrapper(*args):
        li = [*args]
        obli = li[::-1]
        func(obli)

    return wrapper


# 6. Напишите декоратор, который вычисляет время работы декорируемой функции (timer)
def decorator6(func):
    """
    The decorator that calculates the running time of the decorated function (timer)
    """

    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("time execution = {}".format(end_time - start_time))

    return wrapper
