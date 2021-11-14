import functions_8


def choice():
    a = int(input('''
    Выберите функцию, которую вы хотите запустить:
    1) Перевести текст в верхний регистр
    2) Вывести аргументы функции в обратном порядке
    3) Вычислить значение фибоначи 
    4) Вычислить математическое выражение '''))
    if a == 1:
        functions_8.input_string()
    elif a == 2:
        functions_8.func(1, 2, int, False, 'yes', [1, 2])
    elif a == 3:
        c = int(input('Введите номер элемента в последовательности: '))
        print(functions_8.fibbonachi(c))
    elif a == 4:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        z = int(input('Введите третье число: '))
        functions_8.math_calculation(x, y, z)
    else:
        print('Такого пункта нет в меню. Запустите программу заново')


choice()
