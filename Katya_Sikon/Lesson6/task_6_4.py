# 4. Написать функцию с изменяемым числом входных параметров
# При объявлении функции предусмотреть один позиционный и один именованный аргумент, который по умолчанию равен None (в примере это аргумент с именем name).
# Также предусмотреть возможность передачи нескольких именованных и позиционных аргументов

# Функция должна возвращать следующее
# result = function(1, 2, 3, name=’test’, surname=’test2’, some=’something’)
# Print(result)
# 🡪 {“mandatory_position_argument”: 1, “additional_position_arguments”: (2, 3),
#      “mandatory_named_argument”: {“name”: “test2”}, “additional_named_arguments”:       {“surname”: “test2”, “some”: “something”}}


def function(first_position_argument, *args, name=None, **kwargs):
    result = {'mandatory_position_argument': first_position_argument, 'additional_position_arguments': args,
              'mandatory_named_argument': {'name': name}, 'additional_named_arguments': kwargs}
    return result


print(function(1, 2, 3, name='test', surname='test2', some='something'))
