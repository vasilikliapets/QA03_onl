# создаём модуль с нужной функцией
def change_list(a):
    """
    This function returns new changed list
    """
    a_new = a[:]
    a_new.append('a')
    return a_new
