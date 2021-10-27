#1
from functools import reduce
from typing import Counter

def luhn(code):
    """
    Функция для проверки действительности номеров карт
    """
    # Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр
    # Номер индекса равен числу, над которым проводится операция
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    return ((evens + odds) % 10 == 0)

print("Прошел проверку: ", luhn('4561 2612 1234 5467'))


#2
str_1 = "cccbba"

def letters_in_a_row(str_1):
    """
    Функция высчитывает количество букв написаных подряд
    """
    in_a_row = 1  
    result = [str_1[0]]
    for i in range(0, (len(str_1) - 1)):
        if str_1[i] == str_1[i+1]:
            in_a_row += 1
        else:
            if in_a_row == 1:
                result.append(str_1[i + 1])
                in_a_row = 1
            else:
                result.append(in_a_row)
                result.append(str_1[i+1])
                in_a_row = 1
    if in_a_row > 1:
        result.append(in_a_row)
    result = ''.join(map(str, result))
    return result
    
print(letters_in_a_row(str_1))

#3
#Калькулятор

def plus(x, y):
    """
    Функция сложения
    """
    return x + y

def minus(x, y):
    """
    Функция вычитания
    """
    return x - y

def multi(x, y):
    """
    Функция умножения
    """
    return x * y

def div(x, y):
    """
    Функция деления
    """
    if y != 0:
        return x / y
    else:
        print('На 0 делить нельзя') 

opr = int(input('Введите номер пункта меню: '))
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
if 1<= opr <= 4:
    if opr == 1:
        print('Сумма:', plus(x, y))
    elif opr == 2:
        print('Разница:', minus(x, y))
    elif opr == 3:
        print('Произведение:', multi(x, y))
    elif opr == 4:
        print('Частное:', div(x, y))
else:
    print('Такого пункта в меню не существует')

#4
def function(a, *args, name = 'None', **kwargs):
    """
    Функция с изменяемым числом входных параметров
    """
    
    dict_1 = {'mandatory_position_argument': a, 'additional_position_arguments': args, 'mandatory_named_argument': {'name':'test2'}, 'additional_named_arguments': kwargs}
    return dict_1

result = function(1, 2, 3, name = 'test', surname = 'test2', some = 'something')
print(result)


#5
my_list = [1, 2, 3]
def changes(my_list):
    """
    Функция возвращает измененный список и не изменяет исходный
    """
    changed_list = my_list[:]
    changed_list.append('a')
    return changed_list

print(my_list)
print(changes(my_list))


#6

def counter_1(x):
    """
    Функция возвращает количество элементов приведенных данных
    """
    a = 0
    b = 0
    c = 0
    for i in x:
        if isinstance(i, int) == True:
            a = a + 1
        elif isinstance(i, str) == True:
            b = b + 1
        elif isinstance(i, tuple) == True:
            c = c + 1
    return print({'int':a, 'str':b, 'tuple':c})
lst_4 = [1, 2, 'a', (1, 2), 'b']
print(counter_1(lst_4))


#7
a = 5
b = 5.0
print(hash(a), id(a))
print(hash(b), id(b))


#8

def call_able(x):
    """
    Функция, которая проверяет есть ли в списке объект, которые можно вызвать
    """
    resultat = False
    for i in x:
        if callable(i) == True:
            resultat = True
            
    return resultat

print(call_able([None, str]))
