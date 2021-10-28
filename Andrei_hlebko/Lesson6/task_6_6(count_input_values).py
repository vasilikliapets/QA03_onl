def check_input(types):
    """
    This function count types input values
    {'str': 2, 'int': 2, 'tuple': 1}
    """
    count_types = {}
    type_str = []
    type_111 = ["str", "int", 'float', 'tuple', 'list', 'dict']
    for i in types:
        type_str.append(str(type(i)))
    type_str = str(type_str)  # [<class 'int'>, <class 'int'>, <class 'str'>, <class 'tuple'>, <class 'str'>]
    for i in type_111:
        if i in type_str:
            count_types[i] = type_str.count(i)
    return count_types


print(check_input([1, 2, "a", (1, 2), "b"]))
