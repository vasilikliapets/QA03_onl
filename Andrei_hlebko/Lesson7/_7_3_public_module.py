import random

import _7_1_bank_deposit as L7_bank_dep
import _7_2_shifr_cezar as L7_shfr_ces

attempts = 3
flag = True
while flag:
    if attempts > 0:
        vybor = int(input("""
        Выбери программу:
        1)Расчет банковского вклада
        2)Шифр Цезаря
        3)Выход из программы
        :"""))

        if vybor == 1:
            L7_bank_dep.start_bank()
        elif vybor == 2:
            L7_shfr_ces.start_shifr()
        elif vybor == 3:
            break
        else:
            attempts -= 1
        print("Вы ввели неправильно число!")
    else:
        flag = False
        x = random.randint(1, 2)
        if x == 1:
            L7_bank_dep.start_bank()
        else:
            L7_shfr_ces.start_shifr()

        # spis = [L7_bank_dep.start_bank(), L7_shfr_ces.start_shifr()]
        # random.choice(spis) или random.choice([[L7_bank_dep.start_bank(), L7_shfr_ces.start_shifr()]])

        # Почему не работает random.choice если засовывать запуск модуля в list? Выбирает только первое значение всегда!
        # пробовал еще с or - тоже самое.
