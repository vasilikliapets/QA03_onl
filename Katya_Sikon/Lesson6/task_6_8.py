# 8. написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать

def check_callable(list_obj):
    for i in range(len(list_obj)):
        if callable(list_obj[i]):
            return True
    return False


#list_obj = [1, sum, 'v', {1, 2, 3}, int, len, str]
list_obj = [1, 2, 'v', {1, 2, 3}, (2, 5)]
print(check_callable(list_obj))
