# 6. Функция проверяющая тип данных
# Написать функцию которая принимает на вход список из чисел, строк и таплов
# Функция должна вернуть сколько в списке элементов приведенных данных
# print(my_function([1, 2, “a”, (1, 2), “b”])
# 🡪 {“int”: 2, “str”: 2, “tuple”: 1}

def my_function(examp):
    """
    The function checks the data type
    """
    count_int = 0
    count_str = 0
    count_tuple = 0
    for i in examp:
        if type(i) == int:      #проверяю на целочисленные значения
            count_int += 1
        elif type(i) == str:    #проверяю на строки
            count_str += 1
        elif type(i) == tuple:  #проверяю на таплы
            count_tuple += 1

    return ({'int': count_int, 'str': count_str, 'tuple': count_tuple})


print(my_function([1, 2, "a", (1, 2), "b"]))