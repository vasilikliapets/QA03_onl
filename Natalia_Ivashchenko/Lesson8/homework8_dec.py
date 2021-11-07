import time


def word(func):
    """
    The decorator prints before and after the function call the words “Before” and “After”
    """
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper


def number(func):
    """
    The decorator adds 1 to the number
    """
    def wrapper(*args):
        val = func(*args) + 1
        print(val)
    return wrapper


def text_up(func):
    """
    Decorator converts text to uppercase
    """
    def wrapper(text):
        print(text.upper())

    return wrapper


def func_name(func):
    """
    The decorator displays the name of the function
    """
    def wrapper(*args):
        print(func.__name__)
        print(func(*args))

    return wrapper


def change(func):
    """
    The decorator changes the order of the arguments
    """
    def wrapper(*args):
        ls = [*args]
        nls = ls[::-1]
        func(nls)

    return wrapper


def timer(func):
    """
    The decorator calculates the running time of the function
    """
    def wrapper(*args):
        start_time = time.perf_counter()
        value = func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('time:', run_time)
        return value

    return wrapper
