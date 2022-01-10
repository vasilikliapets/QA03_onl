# Напишите функцию декоратор, которая переводит полученный текст
# в верхний регистр

def decorator(func):
    """
    This fucntion-decorator converts text from decorated function to uppercase
    :param func:
    :return: wrapper
    """
    def wrapper(text):
        return func(text).upper()
    return wrapper


@decorator
def main_function(text):
    return text


print(main_function("Python lovers"))
