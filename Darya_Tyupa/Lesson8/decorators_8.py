import functools


def before_and_after(func):
    '''
    This function-decorator prints 'Before' and 'After' and prints the result of decorated function
    '''

    @functools.wraps(func)
    def wrapper(x, y, z):
        print('Before')
        print(func(x, y, z))
        print('After')

    return wrapper


def plus_one(func):
    '''
    This function-decorator returns the result of decorated function + 1
    '''

    @functools.wraps(func)
    def wrapper(x, y, z):
        result = func(x, y, z) + 1
        return result

    return wrapper


def timer(func):
    '''
    This function-decorator measures and prints the performing time of the decorated function
    '''

    @functools.wraps(func)
    def wrapper(a):
        import time
        start_time = time.time()
        result = func(a)
        end_time = time.time()
        process_time = str(end_time - start_time)
        print(process_time)
        return result

    return wrapper


def func_name(func):
    '''
    This function-decorator prints the name of decorated function
    '''

    @functools.wraps(func)
    def wrapper(a):
        result = func(a)
        print(func.__name__)
        return result

    return wrapper


def upper_register(func):
    '''This function-decorator prints the text in uppercase'''

    @functools.wraps(func)
    def wrapper():
        print(func().upper())

    return wrapper


def change_the_order(func):
    '''
    This function-decorator runs the decorated function with parameters in reverse order
    '''

    @functools.wraps(func)
    def wrapper(*args):
        func(*args[::-1])

    return wrapper
