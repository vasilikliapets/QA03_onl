"""написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать"""

def check_call(li: list):
    """проверяет есть ли в списке объект, которые можно вызвать"""
    for i in li:
        if callable(i):
            return True
    return False


print(check_call([1, 2, "a", (1, 2), "b", int]))

