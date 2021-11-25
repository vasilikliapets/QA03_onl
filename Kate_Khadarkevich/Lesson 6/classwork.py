# 1) Напишите функцию, которая возвращает строку: “Hello world!”
def world():
    return 'Hello, world!'


print(world())


# 2) Напишите функцию, которая вычисляет сумму трех чисел и возвращает результат в основную ветку программы.
def summa():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    c = int(input('Введите третье число:'))
    d = a + b + c
    return (d)


print(summa())


# 4) Напишите функцию, которая не принимает отрицательные числа. и возвращает число наоборот.
# 21445 => 54421
# 123456789 => 987654321

def fun_number():
    n1 = int(input("Введите целое число: "))
    if n1 >= 0:
        n2 = str(n1)
        n3 = n2[::-1]
        print('Обратное число:', n3)
    else:
        print('Это отрицательное число!')


fun_number()


# 5) Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.

def fibonach():
    n = input("Номер элемента ряда Фибоначчи: ")
    n = int(n)
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return (fib2)


print(fibonach())


# 6) Напишите функцию, которая проверяет на то, является ли строка палиндромом или нет.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
def palindrom():
    word = str(input('Введите слово для проверки:'))
    word_new = word[::-1]
    if word == word_new:
        print('Слово является палиндромом!')
    else:
        print('Слово не палиндром!')


palindrom()


# 7) У вас интернет магазин, надо написать функцию которая проверяет что введен правильный купон и он еще действителен
#
# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     #Code here!
#
# check_сoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# check_сoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code == correct_code:
        if current_date <= expiration_date:
            print(True)
        else:
            print(False)
    else:
        print(False)


check_coupon("123", "123", "July 9, 2015", "July 9, 2015")
check_coupon("123", "123", "July 9, 2015", "July 2, 2015")


# 8) Фильтр. Функция принимает на вход список, проверяет есть ли эти элементы в списке exclude,
# если есть удаляет их и возвращает список с оставшимися элементами
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
#
# filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) => ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"] => ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
# ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] => []

def spisok(filter_list):
    exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    filter_list = list(set(filter_list) - set(exclude))
    print(filter_list)


spisok(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
