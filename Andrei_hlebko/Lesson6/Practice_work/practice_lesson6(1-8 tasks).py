# 1 Напишите функцию, которая возвращает строку: “Hello world!”

# def hello_world():
#     return "Hello world"
#
# print(hello_world())

# 2 Напишите функцию, которая вычисляет сумму трех чисел и возвращает результат в основную ветку программы.

# def summa_3(a,b,c):
#     return a+b+c
#
# print(summa_3(1,2,3))

# 3 Придумайте программу, в которой из одной функции вызывается вторая. При этом ни одна из них ничего не возвращает
# в основную ветку программы, обе должны выводить результаты своей работы с помощью функции print().

# def func_1():
#     print("function1")
#     func_2()
#
# def func_2():
#     print("function2")
#
#
# func_1()

# 4 Напишите функцию, которая не принимает отрицательные числа. и возвращает число наоборот.
# 21445 => 54421
# 123456789 => 987654321

# def chislo_reverse(chislo):
#     if chislo < 0:
#         return "Не принимаем отрицательные числа"
#     else:
#         chislo = str(chislo)
#         return chislo[::-1]
#
# print(chislo_reverse(-123456789))

# 5 Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.

# def fibona4(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibona4(n-1) +fibona4(n-2)
#
# print(fibona4(5))
#


# 6 Напишите функцию, которая проверяет на то, является ли строка палиндромом или нет.
# def palindrom(stroka):
#     if stroka.islower() == stroka[::-1].islower():
#         return "Палиндром"
#     else:
#         return "Это не Палиндром"
#
# print(palindrom("SOS"))

# 7 У вас интернет магазин, надо написать функцию которая проверяет что введен правильный купон и он еще действителен

# def check_coupon(entered_code, correct_code, current_date, expiration_date):
# #Code here!

# check_сoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# check_сoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

# def check_сoupon(entered_code, correct_code, current_date, expiration_date):
#     if entered_code == correct_code and current_date <= expiration_date:
#         return True
#     return False
#
# print(check_сoupon("123", "123", "July 9, 2015", "July 2, 2015"))

# 8 Фильтр. Функция принимает на вход список, проверяет есть ли эти элементы в списке exclude,
# если есть удаляет их и возвращает список с оставшимися элементами
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
#
# filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) =>
#                                                                   ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"] => ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
# ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] => []


def check_spisok(spisok):
    exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    spisok_return = []
    for i in spisok:
        if i not in exclude:
            spisok_return.append(i)
    return spisok_return


print(check_spisok(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]))
