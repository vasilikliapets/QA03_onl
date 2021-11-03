# 4.При объявлении функции предусмотреть один позиционный и один именованный аргумент,
# который по умолчанию равен None (в примере это аргумент с именем name).
# Также предусмотреть возможность передачи нескольких именованных и позиционных аргументов
# Функция должна возвращать следующее
# result = function(1, 2, 3, name=’test’, surname=’test2’, some=’something’)
# Print(result)
# 🡪 {“mandatory_position_argument”: 1, “additional_position_arguments”: (2, 3),
#       “mandatory_named_argument”: {“name”: “test2”}, “additional_named_arguments”:       {“surname”: “test2”, “some”: “something”}}
def my_function(b, *args, name=None, **kwargs):
    """
    This function that returns a dictionary from parameters
    """
    result = dict(mandatory_position_argument=b)
    if args != ():
        result['additional_position_arguments'] = args  # добавляем в словарь только если аргументы есть
    result['mandatory_named_argument'] = {'name': name}
    if kwargs != {}:
        result['additional_named_arguments'] = kwargs  # добавляем в словарь только если аргументы есть
    return result


result = my_function(1, 2, 3, name='test', surname='test2', some='something')
print(result)
