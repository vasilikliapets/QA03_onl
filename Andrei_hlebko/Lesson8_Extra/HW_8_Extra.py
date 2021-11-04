# Task 1 - Реализуйте декоратор caching, который в течение X последних секунд с момента последнего вызова
# # (в нашему случае 3) будет запоминать вычесленное ранее значение, и возвращать его вместо повторного вызова функции.
# # Если время таймаута истекло между вызовами функции, значение должно быть вычислено заново и еще раз закешировано на X секунд.

import time


def caching(timeout):
    '''
    This function-decorator is casing the result of decorated function
    '''

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

        return wrapper

    return decorator


@caching(timeout=3)
def func(x):
    return {x: 42}


func(2)
time.sleep(2)
func(2)
time.sleep(5)
func(2)

# TASK 2 -Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его
spisok_task2 = lambda x: sorted(x)[::-1]
print(spisok_task2([1, 7, 5, 4, 3, 267, 6]))

# TASK 3 - Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't', и отфильтруйте список имен
# с помощью функции filter

names = ["Andry", "Veronika", "Katya", "Sasha", "Masha", "Maxim", "Konstantin"]
result = filter(lambda x: 't' in x, names)
print(list(result))
