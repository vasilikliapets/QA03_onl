# 3. Простейший калькулятор v0.1

def simple_calc():
    """
    This function is a calculator for simple operations.
    """
    if choice == '1':
        result = one_number + two_number
        print('Сумма:', result)
    elif choice == '2':
        result = one_number - two_number
        print('Вычитание:', result)
    elif choice == '3':
        result = one_number * two_number
        print('Произведение:', result)
    else:
        result = one_number // two_number
        ost = one_number % two_number
        print('Частное:', result, 'Остаток:', ost)


print('Выберите операцию: \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление')
print('Введите номер пункта меню:')
choice = int(input())
print('Введите первое число:')
one_number = int(input())
print('Введите второе число:')
two_number = int(input())
if choice == 4 and two_number == 0: # проверка деления на 0
    print('Делить на 0 нельзя')
elif choice > 4 or choice <= 0: #проверка что введен существующий пункт меню операций
    print('Данный пункт меню отсутсвует. Выберите 1,2,3 или 4')
else:
    simple_calc(choice)     # если всё выбрано верно запускаем функцию
