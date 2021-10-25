import game
import shifr_cezar
import random

count = 0  # переменная для подсчёта ошибок


def choice():
    '''
    This function describes the choice of programs
    '''
    global count
    var = int(input('''Выберите программу:
    1) Крестики-нолики
    2) Шифр Цезаря
    '''))
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
    else:
        if count < 2:  # если ввёл не ту цифру из меню
            print('Вы совершили ошибкую. Повторите выбор')
            count += 1
            choice()
        else:
            f = [game.main, shifr_cezar.main]  # рандомный запуск одной из двух программ
            rand_func = random.choice(f)
            rand_func()


choice()
