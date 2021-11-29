# написать функцию, которая проверяет есть ли в списке объект, который можно вызвать

def my_func(list1):
    """
    This function checks if there is an item in the list that can be called
    """
    for i in list1:
        if callable(i):
            return True
    return False


print(my_func([1, 2, 5, int, list]))


