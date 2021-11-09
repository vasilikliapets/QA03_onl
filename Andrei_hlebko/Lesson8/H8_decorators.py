import functools
import time


def insert_before_and_after(func):
    """
    This function add word "before" text and "after" text around your text
    """

    @functools.wraps(func)
    def wrapper(a):
        print("Before")
        print(func(a))
        print("After")

    return wrapper


def add_1(func):
    """
    This function add 1 to your int value
    """

    def wrapper(x):
        res = func(x) + 1
        return res

    return wrapper


def do_twice(func):
    """
    The function launch your function twice
    """

    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


def make_upper(func):
    """
    The function make your text BIG
    """

    @functools.wraps(func)
    def wrapper_make_upper(text):
        print(func(text).upper())

    return wrapper_make_upper


def func_name(func):
    """
    The function return name your function
    """

    @functools.wraps(func)
    def wrapper_func_name(a):
        # func(a)
        print(func.__name__)
        return func(a)

    return wrapper_func_name


def change(func):
    """
    The function make reverse your values
    """

    def wrapper_change(*args):
        spis = args[::-1]
        return func(spis)

    return wrapper_change


def timer(func):
    """
    The function return how much time is spend on the function
    """

    @functools.wraps(func)
    def wrapper_timer(a):
        start_time = time.time()
        func(a)
        finish_time = time.time()
        print(f"func timer1 = {abs(start_time - finish_time)}")
        return func(a)

    return wrapper_timer
