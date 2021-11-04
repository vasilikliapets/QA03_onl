# 1.Validate
def luna(card):
    """
    The function validates the card
    """
    checksum = 0
    cardnumbers = list(map(int, card))
    for count, num in enumerate(cardnumbers):
        if count % 2 == 0:
            buffer = num * 2
            if buffer > 9:
                buffer -= 9
            checksum += buffer
        else:
            checksum += num
    return checksum % 10 == 0


def card_check():
    """
    The function checks that only numbers are entered in the card number
    """
    card = input('введите номер: ')
    if not card.isdigit():
        print('Номер карты должен содержать только цифры')
    else:
        print(luna(card))


card_check()


# 2. Подсчет количества букв

import collections


def check_string(string: str):
    """
    The function counts the repetitions of letters in a string
    """
    d = []
    i = 0
    counter = 1
    while i < len(string):
        if i == len(string) - 1:
            d.append((string[i], counter))
            break
        if string[i] == string[i + 1]:
            counter += 1
        else:
            d.append((string[i], counter))
            counter = 1
        i += 1

    s = ""
    for t in d:
        if t[1] > 1:
            s += f"{t[0]}{t[1]}"
        else:
            s += f"{t[0]}"
    return s


print(check_string("abeehhhhhccced"))

# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


# Простейший калькулятор v0.1

def calculator(x: float, y: float, op):
    """
    The function asks for an operation and two numbers, and displays the result of the operation
    :param x: first number
    :param y: second number
    :param op: operation
    """
    if op == '1':
        print(f"Сумма {x} и {y} =", x + y)
    elif op == '2':
        print(f"Разность {x} и {y} =", x - y)
    elif op == '3':
        print(f"Произведение {x} и {y} =", x * y)
    elif op == '4':
        if y == 0:
            print('на ноль делить нельзя!')
            y = int(input('Ведите второе число не равное нулю: '))
            print(f"Деление {x} на {y} =", x / y)
        else:
            print(f"Деление {x} на {y} =", x / y)


op = input('Операции: \n'
           '1. Сложение \n'
           '2. Вычитание \n'
           '3. Умножение \n'
           '4. Деление \n'
           'Введите номер пункта меню: ')
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
calculator(x, y, op)


# Написать функцию с изменяемым числом входных параметров
def function(a, *args, name=None, **kwargs):
    """
    A function with a variable number of input parameters, returns the result in a specific form
    :param a: one positional argument
    :param args: variable number of positional arguments
    :param name: one named argument
    :param kwargs: variable number of named arguments
    """
    dictionary = {"mandatory_position_argument": a, "additional_position_arguments": args,
        "mandatory_named_argument": {'name': name}, "additional_named_arguments": kwargs}
    return dictionary


result = function(1, 2, 3, name='test', surname='test2', some='something')
print(result)


# 5. Работа с областями видимости

my_list = [1, 2, 3]


def change(list: list):
    """
    The function returns a new modified list, but does not change the original list.
    """
    change_list = list[:]
    change_list.append('a')
    return change_list


print(my_list)
print(change(my_list))


# 6.Функция проверяющая тип данных
ls = [1, 2, "a", (1, 2), "b"]


def check_type(ls: list):
    """
    The function takes a list of numbers, strings and tuples
    and returns how many elements of the given data are in the list
    """
    d = []
    i = 0
    str_counter = 0
    tupl_counter = 0
    int_counter = 0
    while i < len(ls):
        if type(ls[i]) == str:
            str_counter += 1
            d.append(("str", str_counter))
        elif type(ls[i]) == tuple:
            tupl_counter += 1
            d.append(("tuple", tupl_counter))
        elif type(ls[i]) == int:
            int_counter += 1
            d.append(("int", int_counter))
        elif i == len(ls) - 1:
            break
        i += 1
    return dict(d)


print(check_type(ls))


# 7. Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.

a = ''
b = 0

print(hash(a))
print(hash(b))
print(id(a))
print(id(b))


# 8 написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать
list1 = [5, int]


def call(x):
    """
    the function checks if there is an object in the list that can be called
    """
    c = 0
    for i, el in enumerate(x):
        if callable(el) == True:
            c += 1
    if c == 0:
        print('В списке нет объектов, которые можно вызвать')
    else:
        print('В списке есть объекты, которые можно вызвать')


call(list1)
