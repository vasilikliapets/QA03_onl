import time
from functools import wraps


# 1. Напишите декоратор, который печатает перед и после вызова функции слова “Before” and “After”

def decorater_function_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
        return func(*args, **kwargs)

    return wrapper


# 2. Напишите функцию декоратор, которая добавляет 1 к заданному числу
def decorater_function_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        result = value + 1
        print(result)

    return wrapper


# 3. Напишите функцию декоратор, которая переводит полученный текст в верхний регистр
def decorater_function_3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        upper_text = text.upper()
        print(upper_text)

    return wrapper


# 4. Напишите декоратор func_name, который выводит на экран имя функции (func.__name__)

def func_name(func):
    @wraps(func)
    def wrapper_func_name(*args, **kwargs):
        print('название функции', func.__name__)
        return func(*args, **kwargs)

    return wrapper_func_name


# 5. Напишите декоратор change, который делает так, что задекорированная функция принимает все свои
# не именованные аргументы в порядке, обратном тому, в котором их передали

def change(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = args[::-1]
        result = func(*args, **kwargs)
        print(result)

    return wrapper


# 6. Напишите декоратор, который вычисляет время работы декорируемой функции (timer)

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__} выполнена за {end_time - start_time} с")
        return func(*args, **kwargs)

    return wrapper_timer
