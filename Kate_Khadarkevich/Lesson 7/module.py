# модуль дает возможность выбрать одну из двух предыдущих программ и запустить ее

from bank import for_bank
from shifr import shifr
import random

i = 0
while i < 4:
    choise = input('Выберите программу для запуска: \n1-Сумма вклада \n2-Шифр Цезаря\n')
    if choise == '1':
        for_bank()
        i = 0
        continue
    elif choise == '2':
        shifr()
        i = 0
        continue
    elif choise != '1' or choise != '2':
        print('Такой программы нет! Повторите выбор')
        i += 1
        er_choise = random.choice((for_bank, shifr))   # запускаю  программу, выбранную случайно
        er_choise()
