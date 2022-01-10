from hw8decorators import decorator1
from hw8decorators import decorator2
from hw8decorators import decorator3
from hw8decorators import decorator4
from hw8decorators import decorator5
from hw8decorators import decorator6


@decorator3
def txt(text):
    print(text)


txt('welcome')


@decorator5
def arguments(*args):
    print(*args)


arguments('s', 'e', 'r', 'g', 'e', 'y')


@decorator6
@decorator4
def fibonachi(n):
    fib1 = fib2 = 1
    n = int(n) - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


fibonachi(15)


@decorator1
@decorator2
def math(x, y):
    result = round((((x - y) / (x + 2)) ** y), 2)
    return result


math(125, 13)


