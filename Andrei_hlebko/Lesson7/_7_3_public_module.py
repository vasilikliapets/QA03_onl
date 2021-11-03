import random

import _7_1_bank_deposit as L7_bank_dep
import _7_2_shifr_cezar as L7_shfr_ces

def second_game():
    vybor = int(input("""
            Хотите сыграть в другую игру?
            Выбери программу:
            1)Расчет банковского вклада
            2)Шифр Цезаря
            :"""))

    if vybor == 1:
        L7_bank_dep.start_bank()
    elif vybor == 2:
        L7_shfr_ces.start_shifr()
    else:
        print("Вы ввели неправильно число!")

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
            second_game()
        elif vybor == 2:
            L7_shfr_ces.start_shifr()
            second_game()
        elif vybor == 3:
            break
        else:
            attempts -= 1
        print("Вы ввели неправильно число!")
    else:
        flag = False
        random.choice([L7_bank_dep.start_bank, L7_shfr_ces.start_shifr])()


