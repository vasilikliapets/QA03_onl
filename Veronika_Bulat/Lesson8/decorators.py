from functools import wraps
from time import time


def before_and_after_decorator(func):
    """
    The function-decorator prints 'Before' and 'After'
    and prints the result of decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


def increment_decorator(func):
    """
    The function-decorator returns the result
    of decorated function + 1
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1

    return wrapper


def uppercase_decorator(func):
    """
    The function-decorator converts the received
    text to uppercase
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)).upper()

    return wrapper


def name_decorator(func):
    """
    The function-decorator displays the name
    of the function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


def reverse_decorator(func):
    """
    The function-decorator makes it so that
    the decorated function accepts all
    of its unnamed arguments in the opposite
    order of what they were passed in
    """

    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapper


def duration_decorator(func):
    """
    The function-decorator that calculates
    the running time of the function being decorated
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print("Function duration: ", time() - start_time)
        return result

    return wrapper
