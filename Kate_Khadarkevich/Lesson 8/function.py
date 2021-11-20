from decorators import one_decorator, two_decorator, timer, func_name


@timer
@func_name
def fibonach():
    """The function calculates the value of the Fibonacci number"""
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


@one_decorator
@two_decorator
def func_two():
    """The function evaluates a mathematical expression"""
    c = x * y + y * b + x * b
    print('Результат вычисления:', c)
    return c

choice = input(
    'Выберите функцию для проверки:\n 1. Вычисление числа Фибоначчи \n 2. Вычисление математического выражения\n')
if choice == '1':
    n = int(input("Номер элемента ряда Фибоначчи: "))
    fibonach(n)
elif choice == '2':
    x = int(input("Задайте первое число: "))
    y = int(input("Задайте второе число: "))
    b = int(input("Задайте третье число: "))
    func_two(x, y, b)
else:
    print('Такой функции нет')
