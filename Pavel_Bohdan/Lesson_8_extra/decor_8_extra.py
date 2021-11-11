import time
import functools

#1
def caching(timeout):
    """Декоратор кэширования результата"""
    def outer_wrapper(func):
        time_ref, value = 0, 0
        def wrapper(*args):
            nonlocal time_ref
            nonlocal value
            now = time.time()
            a = abs(time_ref - now)
            if a < timeout:
                print(value)
            else:
                value = func(*args)
                print(value)
                time_ref = time.time()
            return value
        return wrapper
    return outer_wrapper
    
