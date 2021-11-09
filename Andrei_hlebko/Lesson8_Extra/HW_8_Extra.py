# Task 1 - Реализуйте декоратор caching, который в течение X последних секунд с момента последнего вызова
# # (в нашему случае 3) будет запоминать вычесленное ранее значение, и возвращать его вместо повторного вызова функции.
# # Если время таймаута истекло между вызовами функции, значение должно быть вычислено заново и еще раз закешировано на X секунд.

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

# TASK 2 -Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его
spisok_task2 = lambda x: sorted(x)[::-1]
print(spisok_task2([1, 7, 5, 4, 3, 267, 6]))

# TASK 3 - Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't', и отфильтруйте список имен
# с помощью функции filter

names = ["Andry", "Veronika", "Katya", "Sasha", "Masha", "Maxim", "Konstantin"]
result = filter(lambda x: 't' in x, names)
print(list(result))
