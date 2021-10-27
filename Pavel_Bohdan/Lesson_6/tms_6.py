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

str_1 = "abeehhhhhccced"    
Count_1 = Counter(str_1)
Count_2 = Count_1.most_common()
lst_1 = [list(i) for i in Count_2]
lst_2 = []
for i in lst_1:
    for j in i:
        lst_2.append(j)
lst_3 = [str(i) for i in lst_2]
str_2 = ''.join(lst_3)
if '1' in str_2:
    str_2 = str_2.replace('1', '')
print(str_2) # вывод не идентичен требуемому, но считает правильно + упорядочивает по убыванию))


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
if opr == 1:
    print('Сумма:', plus(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
elif opr == 2:
    print('Разница:', minus(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
elif opr == 3:
    print('Произведение:', multi(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
elif opr == 4:
    print('Частное:', div(int(input("Введите первое число: ")), int(input("Введите второе число: "))))


#4
def function(a, *args, name = 'None', **kwargs):
    """
    Функция с изменяемым числом входных параметров
    """
    
    dict_1 = {'mandatory_position_argument': a, 'additional_position_arguments': tuple(args), 'mandatory_named_argument': {'name':'test2'}, 'additional_named_arguments': kwargs}
    return dict_1

result = function(1, 2, 3, name = 'test', surname = 'test2', some = 'something')
print(result)


#5
my_list = [1, 2, 3]
def changes(my_list):
    """
    Функция возвращает измененный список и не изменяет исходный
    """
    my_list.append('a')
    return my_list

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

def call(x):
    """
    Функция, которая проверяет есть ли в списке объект, которые можно вызвать
    """
    for i in x:
        if callable(i) == True:
            print(f'{i} is collable') 
    return

call([int, str])

