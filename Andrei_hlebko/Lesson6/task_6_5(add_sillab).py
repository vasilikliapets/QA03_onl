my_list = [1, 2, 3]


def func_add_items(spisok):
    """
    Function add "a" in list
    """
    change_list = spisok[:]
    change_list.append("a")
    return change_list


print(my_list)
print(func_add_items(my_list))
