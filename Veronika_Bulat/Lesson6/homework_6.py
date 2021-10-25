from functools import reduce

import luhn

# 1.
def validate(card_num: str):
    """
    Validate card number
    """
    return luhn.verify(card_num)

print(validate('356938035643809'))


# 2.
def letters_count(string: str):
    """
    Letters count function
    """
    def reduce_func(prev, el):
        last = prev[-1]
        if last == el:
            return prev + str(2)
        elif last.isdigit() and prev[-2] == el:
            return prev[:-1:] + str(int(last) + 1)
        return prev + el

    return reduce(reduce_func, list(string))


print(letters_count('aacccdeesaaaddd'))

# 3.
import calc

action = 'h'
while calc.validate_action(action):
    print(calc.action(action))
    action = input('Select action: ')
else:
    print('Calc exited')


# 4.

def func(a, *args, name=None, **kwargs):
    """
    Function arguments
    """
    return {
        "mandatory_position_argument": a,
        "additional_position_arguments": args,
        "mandatory_named_argument": {
            "name": name
        },
        "additional_named_arguments": kwargs
    }


print(func(1, 2, 3, name='test', surname='test2', some='something'))


# 5.
def change_list(orig_list: list):
    """
    Add 'a' to list
    """
    return [*orig_list, 'a']


original_list = [1, 2, 5]
changed_list = change_list(original_list)
print(original_list, changed_list)

# 6.
from collections import Counter


def count_types(var_list: list):
    """
    Types counter
    """
    types = []
    for v in var_list:
        types.append(str(type(v)).replace("<class '", "").replace("'>", ""))
    return Counter(types)


print(count_types([1, 2, 'a', (1, 2), 'b']))

# 7.
first = 1
second = 1.0
print(hash(first), hash(second), id(first), id(second))


# 8.
def has_callable(l: list):
    """
    Check if list has callable
    """
    for v in l:
        if callable(v):
            return True
    return False


print(has_callable([1, 2, 'dd', count_types]))
