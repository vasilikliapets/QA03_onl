# 1) Напишите функцию, которая возвращает строку: “Hello world!”

def hello_world():
    return 'Hello world!'


print(hello_world())


# 2) Напишите функцию, которая вычисляет сумму трех чисел и возвращает результат в основную ветку программы.

def sum(x, y, z):
    return x + y + z


x = int(input('Введите первое число '))
y = int(input('Введите второе число '))
z = int(input('Введите третье число '))

print('сумма трех чисел равна', sum(x, y, z))


# 3) Придумайте программу, в которой из одной функции вызывается вторая.
# При этом ни одна из них ничего не возвращает в основную ветку программы,
# обе должны выводить результаты своей работы с помощью функции print().

def first():
    print(
        '\nНочь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще хоть четверть века —\nВсё будет так. Исхода нет.')


def second():
    print(first())
    print(
        '\nУмрешь — начнешь опять сначала\nИ повторится всё, как встарь:\nНочь, ледяная рябь канала,\nАптека, улица, фонарь.')


print(second())


# 4) Напишите функцию, которая не принимает отрицательные числа. и возвращает число наоборот.
# 21445 => 54421
# 123456789 => 987654321

def rever(x):
    if x < 0:
        return False
    else:
        x = str(x)
        rever_x = x[::-1]
        return rever_x


x = int(input('\n\nВведите целое число '))
print(rever(x))


# 5) Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_1 = 0
        fib_2 = 1
        i = 0
        while i < n - 2:
            fib_sum = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_sum
            i = i + 1
        return fib_2


n = int(input('\n\nВведите номер элемента из последовательности Фибоначчи '))
print('Элемент последовательности Фибоначчи под номером', n, '=', fib(n))


# 6) Напишите функцию, которая проверяет на то, является ли строка палиндромом или нет.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

def palindrome(phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()
    i = 0
    while i < len(phrase):
        if phrase[::-1] == phrase:
            return 'Фраза является палиндромом'
        else:
            return 'Фраза не является палиндромом'


phrase = input('\n\nВведите фразу ')
print(palindrome(phrase))

# 7) У вас интернет магазин, надо написать функцию которая проверяет что введен правильный купон и он еще действителен
#
# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     #Code here!
#
# check_сoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# check_сoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if current_date[2] < expiration_date[2] and entered_code == correct_code:
        return True
    elif current_date[2] == expiration_date[2] and current_date[1] < expiration_date[1] and entered_code == correct_code:
        return True
    elif current_date[2] == expiration_date[2] and current_date[1] == expiration_date[1] and current_date[0] <= expiration_date[0] and entered_code == correct_code:
        return True
    else:
        return False

code = input('\n\nВведите код ')
date = input('Введите срок действия купона в формате dd/mm/yyyy ')

date = date.split('/')
#print(type(date), date[2])

current_date = str(datetime.now().date()).split('-')
current_date.reverse()
#print(type(current_date), current_date[2])

print(check_coupon(code, '123', current_date, date))


# 8) Фильтр. Функция принимает на вход список, проверяет есть ли эти элементы в списке exclude,
# если есть удаляет их и возвращает список с оставшимися элементами
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

# filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) => ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"] => ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
# ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] => []

exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def f(filter_list):
    filter_list_new = []
    for i in range(0, len(filter_list)):
        if filter_list[i] not in exclude:
            filter_list_new.append(filter_list[i])
    return filter_list_new


filter_list = list(map(str, input('Введите список чисел через запятую с пробелом: ').split(', ')))
print(f(filter_list))
