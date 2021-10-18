# создаём модуль с нужной функцией
def change_list(a):
    """
    This function returns new changed list
    """
    changed_list = a[:]
    changed_list.append('a')
    return changed_list
