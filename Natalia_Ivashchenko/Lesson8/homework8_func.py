from homework8_dec import number
from homework8_dec import word
from homework8_dec import text_up
from homework8_dec import timer
from homework8_dec import func_name
from homework8_dec import change


@text_up
def change_text(text):
    print(text)


change_text('hello world!')


@change
def argument(*args):
    print(*args)


argument(1, 'a', 2, 'b', 3, 'c')


@timer
@func_name
def fibonachi(el):
    fib1 = 1
    fib2 = 1
    n = el - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


fibonachi(10)


@word
@number
def formula(x, y):
    result = (x + y) ** x / y
    return result


formula(3, 5)
