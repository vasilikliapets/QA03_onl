# 1. Validate
def luhn(card):
    """
    Функция проверяет контрольную цифру в номере карты
    """
    # Сумма цифр номера карты
    checksum = 0
    # Перевод номера карты из строки в массив
    number_card = list(map(int, card))
    for count, number in enumerate(number_card):
        if count % 2 == 0:
            # Если умноженное число > 9, то из произведения вычитается 9 и плюсуем к сумме цифр checksum
            a = number * 2
            if a > 9:
                a -= 9
            checksum += a
            # Если умноженное число < 9, то число остается без изменений и прибавляется к сумме цифр checksum
        else:
            checksum += number
            # Если сумма цифр кратна 10, то номер карты верный
    return checksum % 10 == 0


while True:
    numb = input('Введите номер кредитной карты: ')
    if len(numb) != 16:
        print('Номер должен состоять из 16-ти цифр')
        continue
    elif not numb.isdigit():
        print('Допустим ввод только цифр')
    else:
        print(luhn(numb))
        break


# 2. Подсчет количества букв
def counting_letters(string: str):
    """
    Функция подсчитывает количество букв в строке
    """
    a = []
    i = 0
    counter = 1
    while i < len(string):
        if i == len(string) - 1:
            a.append((string[i], counter))
            break
        if string[i] == string[i + 1]:
            counter += 1
        else:
            a.append((string[i], counter))
            counter = 1
        i += 1

    b = ""
    for e in a:
        if e[1] > 1:
            b += f"{e[0]}{e[1]}"
        else:
            b += f"{e[0]}"
    return b


print(counting_letters("cccbba"))
print(counting_letters("abeehhhhhccced"))
print(counting_letters("aaabbceedd"))
print(counting_letters("abcde"))
print(counting_letters("aaabbdefffff"))

# 3. Простейший калькулятор v0.1


def summ(x, y):
    """
    Расчет суммы
    """
    return x + y


def raznost(x, y):
    """
    Расчет разности
    """
    return x - y


def proizvedenie(x, y):
    """
    Расчет произведения
    """
    return x * y


def chastnoe(x, y):
    """
    Расчет частного
    """
    return x / y


oper = int(input('Выберите операцию: 1. Сложение, 2. Вычитание, 3. Умножение, 4. Деление:'))
while True:
    if oper < 1 or oper > 4:
        print('Операция не существует')
        break
    else:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        if oper == 1:
            print(summ(a, b))
        elif oper == 2:
            print(raznost(a, b))
        elif oper == 3:
            print(proizvedenie(a, b))
        elif oper == 4:
            if b == 0:
                print('На ноль делить нельзя')
            else:
                print(chastnoe(a, b))
        break

# 4. Написать функцию с изменяемым числом входных параметров
def func(a, *args, name=None, **kwargs):
    """""
    Функция выводит измененные входные параметры
    """
    di = {"mandatory_position_argument": a}
    if args != ():
        di["additional_position_arguments"] = args
    di["mandatory_named_argument"] = {'name': name}
    if kwargs != ():
        di["additional_named_arguments"] = kwargs
    return di


result = func(1, 2, 3, name='test2', surname='test2', some='something')
print(result)

# 5. Работа с областями видимости
my_list = [1, 2, 3]


def change_list(my_list):
    """
    Функция добавляет элемент в список
    """
    change_list = my_list[:]
    change_list.append('a')
    return change_list


print(my_list)
print(change_list(my_list))

# 6. Функция проверяющая тип данных


def check_type(l6: list):
    """
    Функция проверяет тип данных
    """
    l6 = [1, 2, "a", (1, 2), "b"]
    i = 0
    type_int = 0
    type_str = 0
    type_tuple = 0
    di = []
    while i < len(l6):
        if type(l6[i]) == int:
            type_int += 1
            di.append(("int", type_int))
        elif type(l6[i]) == str:
            type_str += 1
            di.append(("str", type_str))
        elif type(l6[i]) == tuple:
            type_tuple += 1
            di.append(("tuple", type_tuple))
        elif i == len(l6) - 1:
            break
        i += 1
    return dict(di)
print(check_type([1, 2, "a", (1, 2), "b"]))

# 7. Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.
x = 257.0
y = 257

print(id(x), id(y))
print(hash(x), hash(y))

# 8. Написать функцию, которая проверяет есть ли в списке объект, который можно вызвать

l8 = [2, "n", 1995]


def check_object(l8):
    """
    Функция проверяет, есть ли в списке объект, который можно вызвать
    """
    a = 0
    for i, ob in enumerate(l8):
        if callable(ob) == True:
            a += 1
    if a == 0:
        print('Нет объектов, которые можно вызвать')
    else:
        print('Есть объекты, которые можно вызвать')


check_object(l8)
