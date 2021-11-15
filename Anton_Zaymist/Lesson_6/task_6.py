from collections import Counter


# 1.Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты(число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания
# Алгоритм Луна
# Примеры
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True
# Для проверки:
# https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
def luhn(card):
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


print(luhn('4561261212345464'))
print(luhn('4561261212345467'))

card_number = input("Введите номер карты: ")
print(luhn(card_number))

# 2. Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

print(Counter("abeehhhhhccced"))

# 3. Простейший калькулятор v0.1
while True:
    s = input("Выберите операцию:\n"
              "1. Сложение: +\n"
              "2. Разница: -\n"
              "3. Произведение: *\n"
              "4. Деление: /\n"
              "5. Выйти: exit\n")

    if s == 'exit':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Деление на ноль")
    else:
        print("Введите цифру")


# 4. Написать функцию с изменяемым числом входных параметров
# При объявлении функции предусмотреть один позиционный и один именованный аргумент, который по умолчанию равен None
# (в примере это аргумент с именем name).
# Также предусмотреть возможность передачи нескольких именованных и позиционных аргументов
# Функция должна возвращать следующее
# result = function(1, 2, 3, name=’test’, surname=’test2’, some=’something’)
# Print(result)
# 🡪 {“mandatory_position_argument”: 1, “additional_position_arguments”: (2, 3),
# “mandatory_named_argument”: {“name”: “test2”}, “additional_named_arguments”:{“surname”: “test2”, “some”: “something”}}

def func(a, *args, name=None, **kwargs):
    dict_1 = {"mandatory_position_argument": a}
    if args != ():
        dict_1["additional_position_arguments"] = args
    dict_1["mandatory_named_argument"] = {'name': name}
    if kwargs != ():
        dict_1["additional_named_arguments"] = kwargs
    return dict_1


result = func(1, 2, 3, name='test', surname='test2', some='something')
print(result)

# 5. Работа с областями видимости
# На уровне модуля создать список из 3-х элементов
# Написать функцию, которая принимает на вход этот список и добавляет в него элементы.
# Функция должна вернуть измененный список.
# При этом исходный список не должен измениться. Пример c функцией которая добавляет в список символ “a”:
# My_list = [1, 2, 3]
# Changed_list = change_list(My_list)
# Print(My_list)
# 🡪 [1, 2, 3]
# Print(Changed_list)
# 🡪 [1, 2, 3, “a”]

my_list = [1, 2, 3]


def change_list(my_list):
    list_change = my_list[:]
    list_change.append("a")
    return list_change


changed_list = change_list(my_list)
print(my_list)
print(changed_list)

# 6. Функция проверяющая тип данных
# Написать функцию которая принимает на фход список из чисел, строк и таплов
# Функция должна вернуть сколько в списке элементов приведенных данных
# print(my_function([1, 2, “a”, (1, 2), “b”])
# 🡪 {“int”: 2, “str”: 2, “tuple”: 1}

# 7. Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.

a = 350.0
b = 350
print("Hash:", hash(a), hash(b))
print("Id:", id(a), id(b))

# 8. написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать

list_1 = [1, 2, True, int]


def call(list_1):
    for i in list_1:
        if callable(i):
            return True
    return False


print(call(list_1))