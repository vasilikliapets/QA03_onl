# для проверки декоратора, приводящего текст в верхний регистр, и декоратора change

from decorators import three_decorator, change


@three_decorator
def func_word():
    text = input('Введите любой текст:')
    print('Начальная строка:', text)
    return text


func_word()

@ change
def func_argum(*args):
    print(*args)


func_argum(10, 2, 'b', 15)
