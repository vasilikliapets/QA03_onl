# 3. Общий модуль
import random
from Homework7_1 import bank
from Homework7_2 import code

i = 0
while i < 4:
    choise = input('Какая программа будет запущена: 1-Банковский вклад или 2-Шифр Цезаря: ')
    if choise == '1':
        bank()
        i = 0
        continue
    elif choise == '2':
        code()
        i = 0
        continue
    else:
        i += 1
        print('Данной программы не существует.')
print('Будет запущена одна из программ.')

a_choise = random.choice((bank, code))
a_choise()
