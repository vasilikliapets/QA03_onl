# Реализуйте декоратор caching, который в течение X последних секунд с момента
# последнего вызова (в нашему случае 3) будет запоминать вычисленное ранее
# значение, и возвращать его вместо повторного вызова функции.
# Если время таймаута истекло между вызовами функции, значение должно быть
# вычислено заново и еще раз закешировано на X секунд.

# Импортрируем модуль threading для работы с потоками. Он содержит необходимые
# классы для работы с потоками. Основной класс в этой библиотеке Thread.
# Thread — это отдельный поток выполнения. Это означает, что в нашей программе
# могут работать две и более подпрограммы одновременно.
import threading
import time


def caching(func):
    """
    This fucntion-decorator which, during the last X seconds since the last
    call, remembers the previously calculated value and returns it instead of
    calling the function again. If the timeout expires between function calls,
     the value is recalculated and cached again for X seconds.
    :param func:
    :return: wrapper
    """
    # Запишем пустое значение в переменную cache
    cache = {}

    # Функция для удаления кеша после определенного timeout
    def clear_cache(key: int, timeout: int):
        # Объявляем nonlocal видимость для использования переменной уровнем
        # выше
        nonlocal cache
        # Используем time.sleep, что позволяет отсрочить выполнение вызываемого
        # потока на указанное количество секунд (timeout)
        time.sleep(timeout)
        # Через del очищаем cache key
        del cache[key]

    def wrapper(key: int):
        # Объявляем nonlocal видимость для использования переменной уровнем
        # выше
        nonlocal cache
        if key in cache:
            print("Значение, полученное из кеша: ", cache[key])
            return cache[key]
        value = func(key)
        cache[key] = value
        print("Значение, добавленное в кеш: ", cache[key])

        # Чтобы запустить отдельный поток, нужно создать экземпляр
        # потока Thread и затем запустить его с помощью метода .start()
        # Когда мы создаем поток Thread, мы передаем ему функцию и список,
        # содержащий аргументы этой функции.
        thread = threading.Thread(target=clear_cache, args=(key, 3, ))
        thread.start()
        return value

    return wrapper

@caching
def wrap_number(number):
    return {"number": number}

x = wrap_number(2)
assert x is wrap_number(2)
time.sleep(2)
assert x is wrap_number(2)
time.sleep(2)
assert x is not wrap_number(2)








