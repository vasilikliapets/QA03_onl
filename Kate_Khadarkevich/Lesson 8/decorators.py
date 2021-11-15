import time

def one_decorator(func):
    def wrapper(*args):
        print('Before')
        func()
        print('After')

    return wrapper


def two_decorator(func):
    def wrapper(*args):
        a = func()
        c = a + 1
        print('Добавили единицу:', c)

    return wrapper


def three_decorator(func):
    def wrapper():
        s = func()
        d = s.upper()
        print('Измененная строка:', d)

    return wrapper


def func_name(func):
    def wrapper(*args):
        print(func.__name__)

    return wrapper


def change(func):
    def wrapper(*args):
        result = func(args[::-1])
        return result

    return wrapper


def timer(func):
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Функция выполнена за:', run_time)
        return
    return wrapper_timer
