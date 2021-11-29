def function(a, *args, name=None, **kwargs):
    """Выводит непонятную кашу аргументов неизвестно зачем"""
    di = {"mandatory_position_argument": a}
    if args != ():
        di["additional_position_arguments"] = args
    di["mandatory_named_argument"] = {'name': name}
    if kwargs != ():
        di["additional_named_arguments"] = kwargs
    return di


result = function(1, 2, 3, name='test', surname='test2', some='something')
print(result)
