# 1. Реализуйте декоратор caching, который в течение X последних секунд с момента последнего вызова
# (в нашему случае 3) будет запоминать вычесленное ранее значение, и возвращать его вместо повторного вызова функции.
# Если время таймаута истекло между вызовами функции, значение должно быть вычислено заново и еще раз закешировано
# на X секунд.

import time


def caching(timeout):
    """
    Caches function results
    """
    def decorator(func):
        end_time = 0
        result = 0

        def wrapper(x):
            nonlocal end_time
            nonlocal result
            start = time.time()
            a = abs(end_time - start)
            if a < timeout:
                print(f"Кэш: {result}")
            else:
                result = func(x)
                print(result)
                end_time = time.time()
            return result

        return wrapper

    return decorator


@caching(timeout=3)
def func(x):
    return {x: 42}


x = func(2)
assert x is func(2)
time.sleep(4)
assert x is not func(2)
