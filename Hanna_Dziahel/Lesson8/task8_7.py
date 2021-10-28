# Напишите функцию, которая вычисляет значение числа Фибоначчи для заданного
# количества элементов последовательности и возвращает его и оберните ее
# декоратором timer и func_name
from task8_4 import decorator_func_name
from task8_6 import timer


@timer
@decorator_func_name
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a, b

data = fibonacci(10)
print(data)
