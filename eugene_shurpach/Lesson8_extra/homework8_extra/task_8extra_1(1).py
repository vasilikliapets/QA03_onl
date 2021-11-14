import time


def caching(timeout):  # декоратор принимающий значение
    """Кэширование результатов функции"""
    timeout = timeout

    def my_decorator(func):
        end_time = 0
        var_1 = 0

        def wrapper(*args):
            nonlocal end_time
            nonlocal var_1
            nonlocal timeout
            start = time.time()
            a = abs(end_time - start)
            if a < timeout:
                print(f"Кэш: {var_1}")
            else:
                var_1 = func(*args)
                print(var_1)
                end_time = time.time()
            return var_1

        return wrapper

    return my_decorator


timeout = int(input("Введите таймаут в секундах: "))


@caching(timeout=timeout)
def summa(a, b):
    return a + b


x = summa(270, 5)
assert x is summa(270, 5)
time.sleep(4)
assert x is not summa(270, 5)
