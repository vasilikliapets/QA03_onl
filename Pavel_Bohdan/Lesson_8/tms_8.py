from functools import wraps
import decor_8

"""
Модуль с функциями для проверки работы декораторов
"""
#1
@decor_8.decor_before_after
def func_1():
    """Функция выводит текст 'Nice' """
    print('Nice')

func_1()


#2
@decor_8.plus_one
def insert_variable(x):
    """Функция принимает числовое значение"""
    return int(x)
    
print(insert_variable(3))


#3
@decor_8.all_letters_capital
def letters():
    """Функция принимает текс"""
    return letters()

print(letters('all_letters_capital'))


#4
@decor_8.func_name
def you_got_it():
    """Функция с названием:)"""
    return

print(you_got_it())


#5
@decor_8.change
def wright_func(*args):
    """Функция выводит введенные аргументы"""
    result = args
    return result

print(wright_func(1, 3, 5))


#6
@decor_8.run_timer
#@decor_8.change  # Добавлен "change" декоратор для проверки его работы
def test_func(a, b):
    """Функция возводит число в степень"""
    result = a ** b
    print(f'{a} в степени {b} равно {result}')
    return 

test_func(5, 3)


#7
@decor_8.run_timer
def fibo_nacci(n):
    """Функция выводит последовательность фибоначчи до n-ого числа"""
    num_1 = 0
    num_2 = 1
    print(f'Последовательность Фибоначчи до {n} числа: ')
    for i in range(0, n):
        num_1, num_2 = num_2, num_1 + num_2
        result = print(num_1, end = ' ')
    print()
    return result

fibo_nacci(15)


#8
@decor_8.decor_before_after
@decor_8.plus_one
def discriminant(*qwert):
    a = qwert[0]
    b = qwert[1]
    c = qwert[2]
    d = (b ** 2) - (4 * a * c)
    return d

discriminant(4, 8, 2)