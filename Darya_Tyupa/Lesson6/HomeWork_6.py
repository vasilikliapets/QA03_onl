# 1 Validate
def validate(code):
    """
    This function validates the entered card number
    """
    if code.isdigit() is True:
        check_card(code)
    else:
        print('Введите валидный номер карты')
        return code


def check_card(a):
    """
    This function checks the card number using algorithm Luna
    """
    a = list(map(int, str(a)))
    b = a[-2::-2]
    c = a[-1::-2]
    n = len(b)
    for i in range(0, n):
        if b[i] * 2 > 9:
            b[i] = b[i] * 2 - 9
        else:
            b[i] = b[i] * 2
    summa = sum(c) + sum(b)
    if summa % 10 == 0:
        print('True')
    else:
        print('False')


a = input('Введите номер карты: ')

validate(a)


# 2 Подсчет количества букв

def count_letters(a):
    """
    This function counts repeatable letters
    """
    a = list(a)
    number = 1
    a_new = [a[0]]
    n = len(a)
    for i in range(0, n - 1):
        if a[i] == a[i + 1]:
            number += 1
        else:
            if number == 1:
                a_new.append(a[i + 1])
            else:
                a_new.append(number)
                a_new.append(a[i + 1])
                number = 1
    if number != 1:
        a_new.append(number)
    a_new = ''.join(str(i) for i in a_new)
    print(a_new)


a = 'aaabcccdaefggg'
count_letters(a)


# 3 Простейший калькулятор v0.1
def summ(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def multi(a, b):
    print(a * b)


def div(a, b):
    print('Частное:', a // b, 'Остаток:', round((a / b - a // b) * 10))


def select_option(x):
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    if x == 1:
        summ(a, b)
    elif x == 2:
        sub(a, b)
    elif x == 3:
        multi(a, b)
    elif x == 4:
        if b == 0:
            print('Делить на ноль нельзя')
        else:
            div(a, b)


# описываем наш калькулятор
print('''Выберите операцию:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление''')
x = int(input('Введите номер пункта меню:'))
if x <= 0 or x > 4:
    print('Такого пункта нет в меню')
else:
    select_option(x)


# 4 Написать функцию с изменяемым числом входных параметров
def function(a, *args, name=None, **kwargs):
    """
    This function returns the dictionary of parameters
    """
    x = {'mandatory_position_argument': a}
    if args != ():
        x['additional_position_arguments'] = args
    x['mandatory_named_argument'] = {'name': name}
    if kwargs != {}:
        x['additional_named_arguments'] = kwargs
    return x


result = function(1, 2, 3, name='test', surname='test2', some='something')
print(result)

# 5 Работа с областями видимости
import function_5_module  # импортируем модуль

my_list = [1, 2, 3]

changed_list = function_5_module.change_list(my_list)

print(my_list)
print(changed_list)

# 6 Функция проверяющая тип данных
a = [1, 2, 'a', (1, 2), 'b']


def my_function(a):
    """
    This function counts types in the list
    """
    types = []
    counted_types = {}
    defoult_types = ['str', 'int', 'tuple']
    for i in a:
        types.append(type(i))
    types = str(types)
    for i in defoult_types:
        if i in types:
            counted_types[i] = types.count(i)
    return counted_types


print(my_function(a))

# 7 Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.

a = 5
b = 5.0

print(id(a), id(b))
print(hash(a), hash(b))

print(a is b)

# 8 написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать
x = [int, 1, 2, list, 'a', (1, 2), False, enumerate]


def check_call(x):
    """
    This function returns the list of callable objects
    """
    a = []
    for i in x:
        if callable(i) is True:
            a.append(i)
    return a


print(check_call(x))
