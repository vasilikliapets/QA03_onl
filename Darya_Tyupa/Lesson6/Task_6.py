# 1 Напишите функцию, которая возвращает строку: “Hello world!”

def world():
    return 'Hello world'


print(world())


# 2 Напишите функцию, которая вычисляет сумму трех чисел и возвращает результат в основную ветку программы.

def summa(a, b, c):
    return a + b + c


d = summa(1, 2, 3)
print(d)


# 3 Придумайте программу, в которой из одной функции вызывается вторая. При этом ни одна из них ничего не возвращает в основную ветку программы, обе должны выводить результаты своей работы с помощью функции print().

def question():
    print('How old are you?')


def answer(a):
    question()
    print(a)


answer(28)


# 4 Напишите функцию, которая не принимает отрицательные числа. и возвращает число наоборот

def reverse_number(a):
    if a < 0:
        return False
    else:
        a = str(a)[::-1]
        a = int(a)
        return a


print(reverse_number(123456789))


# 5 Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))


# 6 Напишите функцию, которая проверяет на то, является ли строка палиндромом или нет

def palindrom(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return palindrom(a[1:-1])


print(palindrom('level'))
print(palindrom('cat'))


# 7 Написать функцию которая проверяет что введен правильный купон и он еще действителен

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code == correct_code and current_date <= expiration_date:
        return True
    return False


print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))


# 8 Функция принимает на вход список, проверяет есть ли эти элементы в списке exclude, если есть удаляет их и возвращает список с оставшимися элементами
def filter_list(a):
    exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    for i in exclude:
        if i in a:
            a.remove(i)
    return a


print(filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
print(filter_list(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]))
print(filter_list(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]))
