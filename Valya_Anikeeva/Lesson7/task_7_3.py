import random
from task_7_1 import run_bank
from task_7_2 import code

chet = 0
while chet < 3:
    punkt = input("Выбери программу: 1 - Банковский вклад, 2 - Шифр Цезаря ")
    if punkt == '1':
        run_bank()
        chet = 0
        continue
    elif punkt == '2':
        code()
        chet = 0
        continue
    else:
        chet += 1
        print('Wrong')
        continue
else:
    print("Потрачено 3 попытки, запуск случайной программы")
    value_r = random.choice((run_bank(), code))
    value_r()
