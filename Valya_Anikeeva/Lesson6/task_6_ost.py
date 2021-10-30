# 4 написать функцию с изменяемым числом входных параметров

def function(a, *args, name=None, **kwargs):
    # Функция с переменным количеством входных параметров, возвращает результат в определенной форме

    diction = {"mandatory_position_argument": a}
    if args != ():
        diction["additional_position_arguments"] = args
    diction["mandatory_named_argument"] = {'name': name}
    if kwargs != ():
        diction["additional_named_arguments"] = kwargs
    return diction


itog = function(1, 2, 3, name='test', surname='test2', some='something')
print(itog)

# 5 создать список из 3-х элементов. Написать функцию, которая принимает на вход этот список и добавляет в него
# элементы. Функция должна вернуть измененный список. При этом исходный список не должен измениться

my_list = [1, 2, 3]


def change_list(my_list):
    # копия для редактирования,начальный лист не меняется
    list_change = my_list[:]
    list_change.append("a")
    return list_change


changed_list = change_list(my_list)
print(my_list)
print(changed_list)

# 6 Написать функцию которая принимает на вход список из чисел, строк и таплов
# Функция должна вернуть сколько в списке элементов приведенных данных

sp = [1, 2, "a", (1, 2), "b"]


def check_type(sp: list):
    d = []
    i = 0
    str_counter = 0
    tupl_counter = 0
    int_counter = 0
    while i < len(sp):
        if type(sp[i]) == str:
            str_counter += 1
            d.append(("str", str_counter))
        elif type(sp[i]) == tuple:
            tupl_counter += 1
            d.append(("tuple", tupl_counter))
        elif type(sp[i]) == int:
            int_counter += 1
            d.append(("int", int_counter))
        elif i == len(sp) - 1:
            break
        i += 1
    return dict(d)


print(check_type(sp))

# 7 написать пример, чтобы hash от объекта 1 и 2 были одинаковые, а id разные

a = 255.00
b = 255
print("Hash:", hash(a), hash(b))
print("Id:", id(a), id(b))

# 8 написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать

a = [1, 2, True, int]


def call(a):
    for i in a:
        if callable(i):
            return True
    return False


print(call(a))
