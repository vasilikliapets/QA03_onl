# 6. Функция проверяющая тип данных
# Написать функцию которая принимает на вход список из чисел, строк и тюплов
# Функция должна вернуть сколько в списке элементов приведенных данных
#
# print(my_function([1, 2, “a”, (1, 2), “b”])
# 🡪 {“int”: 2, “str”: 2, “tuple”: 1}

def counter(list):
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


print(counter([1, 2, "a", (1, 2), "b", (2, 3), "fff", 2.3, 23]))
