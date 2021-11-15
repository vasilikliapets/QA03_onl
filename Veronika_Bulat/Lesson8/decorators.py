from functools import wraps
from time import time


def before_and_after_decorator(func):
    """

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

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1

    return wrapper


def uppercase_decorator(func):
    """

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)).upper()

    return wrapper


def name_decorator(func):
    """

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


def reverse_decorator(func):
    """

    """

    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapper


def duration_decorator(func):
    """

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print("Function duration: ", time() - start_time)
        return result

    return wrapper
