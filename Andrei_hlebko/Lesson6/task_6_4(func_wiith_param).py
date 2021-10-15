def function_argum(a1, *args, name=None, **kwargs):
    """
    This function get arguments and return dict with added arguments
    """
    dicts = {
        "mandatory_position_argument": a1
    }
    if args != ():
        dicts["additional_position_arguments"] = args
    dicts["mandatory_named_argument"] = {'name': name}
    if kwargs != ():
        dicts["additional_named_arguments"] = kwargs

    return dicts


result = function_argum(1, 2, 3, name='test', surname="test2", some="something")
print(result)
