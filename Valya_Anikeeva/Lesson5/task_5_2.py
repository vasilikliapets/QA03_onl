# 2  программа, которая, принимая массив имён, возвращает строку описывающая количество лайков
name = input('Введите имена через запятую ')
n = name.split(',')
if len(n) == 1 and n[0] != '':
    print(n[0] + " likes this")
elif len(n) == 2:
    print(n[0] + ' and' + n[1] + " like this")
elif len(n) == 3:
    print(n[0] + ',' + n[1] + ' and' + n[2] + " like this")
elif len(n) >= 4:
    print(n[0] + ',' + n[1] + ' and ' + str(len(n[2:])) + " others like this")
else:
    print("No one likes this")

