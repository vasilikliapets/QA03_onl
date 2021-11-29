from task_7_1 import count_deposit
from task_7_2 import caesar_shift
import random

i = 0
print('Выберите программу:')

while i < 4:
    program = input('1) Вычисление суммы вклада \n2) Шифр Цезаря\n')
    if program == '1':
        count_deposit()
    elif program == '2':
        caesar_shift()
    else:
        i += 1
        if i < 4:
            print('\nВыберите программу из предложенных в списке')
        else:
            error = random.choice((count_deposit, caesar_shift))
            error()