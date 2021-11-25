from decorators_8 import before_and_after, plus_one, func_name, timer, upper_register, change_the_order


@before_and_after
@plus_one
def math_calculation(x, y, z):
    '''
    This function returns the result of mathematical expression
    '''
    return round((x * y) % z + (x ** y) ** 0.5, 1)


@timer
@func_name
def fibbonachi(a):
    '''
    This function calculates and returns the fibonacci number
    '''
    def fib(a):
        if a == 1:
            return 0
        if a == 2:
            return 1
        return fib(a - 1) + fib(a - 2)

    return fib(a)


@upper_register
def input_string():
    '''This function returns the text'''
    a = str(input('Введите текст: '))
    return a


@change_the_order
def func(*args):
    '''This function prints it's parameters'''
    print(args)
