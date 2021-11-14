def check_types(li: list):
    """Считает переменные каждого типа и выдает дикт с ними"""
    i = 0
    type_str = 0
    type_int = 0
    type_tuple = 0
    di = []
    while i < len(li):
        if type(li[i]) == str:
            type_str += 1
            di.append(("str", type_str))
        elif type(li[i]) == tuple:
            type_tuple += 1
            di.append(("tuple", type_tuple))
        elif type(li[i]) == int:
            type_int += 1
            di.append(("int", type_int))
        elif i == len(li) - 1:
            break
        i += 1
    return dict(di)


print(check_types([1, 2, "a", (1, 2), "b"]))
