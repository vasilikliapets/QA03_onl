# 3
from HomeWork_7_1 import bank
from HomeWork_7_2 import encode
import random

i = 0

while i < 4:
    print('Выберите программу:\n'
          'Вклад: 1\n'
          'Кодировать: 2\n')
    program = input('Введите номер программы: \n')
    if program == '1':
        bank(a, years)
    elif program == '2':
        enode()
    else:
        i += 1
        if i < 4:
            print('Попробуйте еще раз!')
        else:
            error = random.choice((bank, encode))
            error()
