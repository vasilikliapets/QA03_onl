#1 Декоратор caching,в течение X последних секунд с момента последнего вызова
# будет запоминать вычесленное ранее значение,и возвращать его вместо повторного вызова функции.
# Если время таймаута истекло между вызовами функции, значение должно быть вычислено заново
# и еще раз закешировано на X секунд

import time


def caching(timeout):  # декоратор принимающий значение
    """Декоратор кэширует результат функции"""

    def decorator(func):
        end_time = 0
        res = 0

        def wrapper(x):
            nonlocal end_time
            nonlocal res
            start = time.time()
            a = abs(end_time - start)
            if a < timeout:
                print('Кэш:', res)
            else:
                res = func(x)
                print(res)
                end_time = time.time()
            return res

        return wrapper

    return decorator


@caching(timeout=3)
def func(x):
    return {x: 42}


x = func(2)
assert x is func(2)
time.sleep(4)
assert x is not func(2)

#2 Лямбда функция, которая будет сортировать список по убыванию и возвращать его

l = [1,5,9,10,15,27,30]

func_l = lambda x: sorted(x)[::-1]
print(func_l(l))

#3 Лямбда, которая проверяет есть ли в слове буква t, отфильтруйте список имен с помощью функции filter

names = ['Ivan', 'Anton', 'Antonina', 'Maria']

func_l2 = filter(lambda x: 't' in x, names)
print(list(func_l2))
