from functools import wraps
from time import time, sleep


def caching(expires: int):
    """
    Decorator for caching
    """

    def decorator(func: callable):
        cache = None
        cached_at = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache
            nonlocal cached_at
            current_time = time()
            if (current_time - cached_at) > expires:
                cache = func(*args, **kwargs)
                cached_at = current_time
            return cache

        return wrapper

    return decorator


@caching(3)
def addition(a, b):
    """
    Addition of numbers
    """
    return a + b


print(addition(1, 2))
sleep(1)
print(addition(3, 4))
sleep(3)
print(addition(5, 6))
sleep(2)
print(addition(7, 8))
print(addition(9, 0))
sleep(3)
print(addition(0, 1))
print(addition(2, 3))

sorted_reverse = lambda a: sorted(a, reverse=True)
print(sorted_reverse([1, 5, 2, 58, 4, 12, 8, 78]))

names = ["Ann", "Mary", "Edith", "Osip", "Mikhail", "Jane", "Bob"]
print(list(filter(lambda name: not name.find('t') == -1, names)))
