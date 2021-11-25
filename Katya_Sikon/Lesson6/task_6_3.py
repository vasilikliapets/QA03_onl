# 3. Простейший калькулятор v0.1 Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет
# произвести над числами, а затем запрашивает два числа и выводит результат Проверка деления на 0.

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def quotient(num1, num2):
    return num1 // num2


def remainder(num1, num2):
    return num1 % num2


operation = int(input('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\nВведите номер пункта '
                      'меню:'))

if operation == 1:
    print('сумма:', addition(num1=int(input('Введите первое число: ')), num2=int(input('Введите второе число: '))))
elif operation == 2:
    print('разность:',
          subtraction(num1=int(input('Введите первое число: ')), num2=int(input('Введите второе число: '))))
elif operation == 3:
    print('произведение:',
          multiplication(num1=int(input('Введите первое число: ')), num2=int(input('Введите второе число: '))))
elif operation == 4:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print('частное:', quotient(num1, num2), 'остаток:', remainder(num1, num2))
else:
    print('Введите номер пункта меню из предложенных вариантов')
