# модуль который предоставляет возможность выбрать
# одну из двух предыдущих программ и запустить ее.

import random
from homework7_shifr import code
from homework7_vklad import bank

count = 1


def ch():
    """
    The function offers to choose one of two programs and start it.
    After three errors, it launches one of the programs chosen at random.
    """
    var = input('Выберите программу: 1 - Шифр цезаря, 2 - Банковский вклад ')
    if var == '1':
        code()
        var2 = input('Для запуска другой программы введите 1')
        if var2 == '1':
            bank()
        else:
            print('Программа завершена')
    elif var == '2':
        bank()
        var2 = input('Для запуска другой программы введите 1: ')
        if var2 == '1':
            code()
        else:
            print('Программа завершена')
    else:
        global count
        if count < 3:
            print('Неправильно выбрана программа!')
            count += 1
            ch()
        else:
            print('Запущена программа, выбранная случайно')
            prog = [code, bank]
            rand_prog = random.choice(prog)
            rand_prog()


ch()
