# Проверить, все ли элементы одинаковые

# [1, 1, 1] == True
# [1, 2, 1] == False
# ['a', 'a', 'a'] == True
# [] == True

a = [1, 2, 1]
b = set(a)       # убрала повторяющ. элементы
if len(set(a)) == 1 or a == []:
    print('True')
else:
    print('False')

