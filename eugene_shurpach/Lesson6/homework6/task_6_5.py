My_list = [1, 2, 3]

def change_list(My_list):
    """создает копию листа с возможностью редактировать без редактирования начального листа"""
    my_list_2 = My_list[:]
    my_list_2.append("a")
    return my_list_2


Changed_list = change_list(My_list)
print(My_list)
print(Changed_list)
