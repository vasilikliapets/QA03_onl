import time


def caching(timeout):
    timeout = timeout
    '''
    The decorator is casing the result of function
    '''

    def decorator(func):
        end_time = 0
        result = 0

        def wrapper(x):
            nonlocal end_time
            nonlocal result
            nonlocal timeout
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


# Лямбда функция, которая сортирует список по убыванию и возвращяет его

lis = lambda ls: sorted(ls, reverse=True)
print(lis([1, 2, 3, 4, 5, 6, 7]))


# Лямбда функция, которая проверяет есть ли в слове буква 't'

spisok = ['Anton', 'Anna', 'Marta', 'Vera']
name = filter(lambda world: 't' in world, spisok)
print(list(name))
