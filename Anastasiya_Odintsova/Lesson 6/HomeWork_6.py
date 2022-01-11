# 1
def validate(card):
    """
    Функция проверяет введенный номер карты на наличение любых символов отличных от цифр
    """
    if card.isdigit() is True:
        check_card(card)
        print(card)
    else:
        print("Номер карты должен содержать только цифры")
        validate(input('Введите номер карты: '))



def check_card(a):
    """Функция проверяет номер карты на соотвествие алгоритму Луна"""
    a = list(map(int, str(a)))
    b = a[-2::-2]
    c = a[-1::-2]
    n = len(b)
    for i in range(0, n):
        if b[i] * 2 > 9:
            b[i] = b[i] * 2 - 9
        else:
            b[i] = b[i] * 2
    summa = sum(c) + sum(b)
    if summa % 10 == 0:
        print('Карта валидна')
    else:
        print('Карта невалидна')


a = input('Введите номер карты: ')
validate(a)

# 2
def count_text(a):
    """
    Функция считает количество букв в виде "cccbba" == "c3b2a"
    """
    count = 1
    x = 1
    y = a[x:x + 1]
    for i in a:
        if i in y:
            count += 1

        else:
            print(i, end='')
            if count > 1:
                print(count, end='')
                count = 1
        x += 1
        y = a[x:x + 1]

a = input("Введите любое значение:")
count_text(a)

# 3
def calc():
    while True:
        print("Выберите операцию:\n"
              "Сложение: 1\n"
              "Вычитание 2\n"
              "Умножение: 3\n"
              "Деление: 4\n")
        action = input("Введите номер пункта меню:\n")
        if action not in ('1', '2', '3', '4'):
            print("Фиг что посчитаешь")
            action = input("Выберите номер пункта меню еще раз:\n")
        if action in ('1', '2', '3', '4'):
            x = float(input("Введите первое число:\n"))
            y = float(input("Введите второе число:\n"))
            if action == '1':
                print(x+y)
                break
            elif action == '2':
                print(x-y)
                break
            elif action == '3':
                print(x*y)
                break
            elif action == '4':
                if y != 0:
                    print(x/y)
                    break
                else:
                    print("Делить на ноль нельзя!")
                    break

calc()

# 4
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

# 5
my_list = [1, 2, 3, 4] 

def change_list(my_list):
    """
    Функция создает копию листа и редактирует его не изменяя первоначальный лист
    """
    my_list_2 = my_list[:]
    my_list_2.append("a")
    return my_list_2


changed_list_2 = change_list(my_list)
print(my_list)
print(changed_list_2)

# 6
def my_function(list):
    count_int = 0
    count_str = 0
    count_tuple = 0

    for i in range(len(list)):
        if type(list[i]) == int:
            count_int += 1
        elif type(list[i]) == str:
            count_str += 1
        elif type(list[i]) == tuple:
            count_tuple += 1
        else:
            pass

    dict_counter = {'int': count_int, 'str': count_str, 'tuple': count_tuple}
    return dict_counter


print(my_function([1, 2, "a", (4, 5), "b", (6, 7), "с", 8, 9]))

# 7 Пример, где hash от объектов 1 и 2 одинаковые, а id разные
a = 1
b = 1.0

print(hash(a), "-> Hash от a")
print(hash(b), "-> Hash от b")
print(id(a), "-> ID от a")
print(id(b), "-> ID от b")

# 8
def check_func(list_obj):
    """
    Функция проверяет есть ли в списке объект, который можно вызвать
    """
    for i in range(len(list_obj)):
        if callable(list_obj[i]):
            return True
    return False

list_obj = [1, 2, "3", calc]
print(check_func(list_obj))
