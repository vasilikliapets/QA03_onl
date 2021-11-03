import game
import shifr_cezar
import random


def choice():
    var = int(input('''Выберите программу:
        1) Крестики-нолики
        2) Шифр Цезаря
        '''))
    return var


count = 0  # переменная для подсчёта ошибок

flag = True
while flag:
    var = choice()
    if var == 1:  # если выбрал крестики-нолики
        game.main()
        case = int(input('''
        Запустить вторую программу?
        1) Да
        2) Нет'''))
        if case == 1:
            shifr_cezar.main()
        else:
            print('Конец сеанса')
            break
    elif var == 2:  # если выбрал шифровальщика
        shifr_cezar.main()
        case = int(input('''
        Запустить вторую программу?
        1) Да
        2) Нет'''))
        if case == 1:
            game.main()
        else:
            print('Конец сеанса')
            break
    else:
        if count < 2:  # если ввёл не ту цифру из меню
            print('Вы совершили ошибкую. Повторите выбор')
            count += 1
        else:
            f = [game.main, shifr_cezar.main]  # рандомный запуск одной из двух программ
            rand_func = random.choice(f)
            rand_func()
            flag = False
