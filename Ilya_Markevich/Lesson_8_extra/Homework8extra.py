# Задание 3
names = ["Ilya", "Nadya", "Carri"]
result_3 = filter(lambda x: 'y' in x, names)  # Выбирает имена с "y"
print(list(result_3))

# Задание 2
sp = [10, 24, 8, 255, 14, 99, 658]
res = lambda list_2: sorted(list_2, reverse=True)
print(res(sp))


# декоратор caching, который в течение X последних секунд с момента последнего вызова (в нашему случае 3) будет запоминать вычесленное ранее значение,
# и возвращать его вместо повторного вызова функции. Если время таймаута истекло между вызовами функции, значение должно быть вычислено заново и еще раз
#закешировано на X секунд
import time
def caching(timeout):
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
