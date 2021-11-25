import time


def caching(func):
    """Кэширование результатов функции"""
    end_time = 0
    var_1 = 0


    def wrapper(*args):
        nonlocal end_time
        nonlocal var_1
        global timeout
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


@caching
def summa(a, b):
    return a + b

timeout = int(input("Введите таймаут в секундах: "))
summa(2, 4)
time.sleep(2)
summa(2, 4)
time.sleep(5)
summa(2, 4)
