# 5. Работа с областями видимости
# На уровне модуля создать список из 3-х элементов
# Написать функцию, которая принимает на вход этот список и добавляет в него элементы. Функция должна вернуть измененный список.
# При этом исходный список не должен измениться. Пример c функцией которая добавляет в список символ “a”:
#
# My_list = [1, 2, 3]
# Changed_list = change_list(My_list)
#
# Print(My_list) 🡪 [1, 2, 3]
#
# Print(Changed_list) 🡪 [1, 2, 3, “a”]

my_list = list(map(str, input('Введите список элементов через пробел: ').split(' ')))


def change_list(my_list):
    my_list_copy = list(my_list)
    new_elements = list(map(str, input('Введите список новых элементов через пробел: ').split(' ')))
    for i in range(len(new_elements)):
        my_list_copy.append(new_elements[i])
    return my_list_copy


print('измененный список: ', change_list(my_list))
print('первоначальный список: ', my_list)
