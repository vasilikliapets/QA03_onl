# 1. Реализуйте декоратор caching, который в течение X последних секунд с момента последнего вызова (в нашем случае 3)
# будет запоминать вычесленное ранее значение, и возвращать его вместо повторного вызова функции. Если время таймаута
# истекло между вызовами функции, значение должно быть вычислено заново и еще раз закешировано на X секунд.

import time


def caching(timeout):
    timeout = timeout
    '''
    The decorator that remembers the previously calculated value and returns it instead of calling the function again.
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

# 2. Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его

list2 = [2, 10, 56, 74, 95.08]
result2 = lambda x: sorted(x)[::-1]
print(result2(list2))

# 3. Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't', и отфильтруйте список имен с помощью
# функции filter

list_name = ['Sergey', 'Marta', 'Tom', 'Dmitriy', 'Anton', 'Vladislav']
result3 = filter(lambda x: 't' in x, list_name)
print(list(result3))
