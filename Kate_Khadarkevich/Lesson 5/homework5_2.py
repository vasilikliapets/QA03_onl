# 2. Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).
print('Введите имена через запятую:')
a = input()
b = a.split(',')  # получаю список с разделителем запятой
if len(b) == 1 and b[0] != '':
    print(a, 'likes this')
elif len(b) == 2:
    print(b[0], 'and', b[1], 'like this')
elif len(b) == 3:
    print(b[0], ',', b[1], 'and', b[3], 'like this')
elif len(b) > 3:
    c = len(b) - 2  # узнаю сколько имен ввели после второго
    print(b[0], ',', b[1], 'and', c, 'others like this')
else:
    print('No one likes this')
