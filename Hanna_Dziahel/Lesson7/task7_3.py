# Общий модуль, который предоставляет возможность выбрать одну из двух
# программ и запустить ее, также он позволяет по окончанию выполнения
# программы выбрать запуск другой

# Если пользователь совершит ошибку при выборе программы,
# первые три раза программа должна сообщить ему об ошибке,
# а на четвертый раз запустить одну из программ, выбранных случайно.

# Импортируем модули, содержащие 2 программы
import task7_1
import task7_2
import random


def run_choosing_process():
    """
    This function runs main program
    :return:
    """

    # Переменная для хранения количества неверных попыток пользователя
    count_invalid_attempts = 0
    while True:
        print("""Выберите программу:
            1) Банковский вклад
            2) Шифр Цезаря
            3) Выход из программы""")
        program_point = input("Введите номер пункта меню: ")

        # Если выбраны значения 1 или 2, запускается функция choose_program
        if program_point == 1 or program_point == 2:
            choose_program(program_point)

        # Если выбрано значения не из списка, то выводится сообщение об ошибке
        elif program_point not in [1, 2, 3]:
            print('Введен неверный номер пункта меню')

            # Создаем условие, которое соответсвует 3 неверным вводам
            if count_invalid_attempts < 2:
                count_invalid_attempts += 1
            # Используем функцию random и choose_program для рандомного
            # выбора после 3 неверных вводов
            else:
                random_value = random.choice([1, 2])
                choose_program(random_value)

                # Обнуляем значение неверных попыток
                count_invalid_attempts = 0

        # Условие для выхода из программы
        elif program_point == 3:
            break


def choose_program(value):
    """
    This functions runs program Bank deposit or Caesar cipher based on user's
    input value
    :param value: int
    :return:
    """
    if value == 1:
        task7_1.run_bank()
    elif value == 2:
        task7_2.run_ceasar()


run_choosing_process()
