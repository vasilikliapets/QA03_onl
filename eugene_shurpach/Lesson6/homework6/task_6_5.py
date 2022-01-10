my_list = [1, 2, 3]

def change_list(my_list):
    """создает копию листа с возможностью редактировать без редактирования начального листа"""
    my_list_2 = my_list[:]
    my_list_2.append("a")
    return my_list_2


changed_list_var = change_list(my_list)
print(my_list)
print(changed_list_var)
