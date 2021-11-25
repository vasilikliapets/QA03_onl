# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

names = list(input('Введите имена через запятую:').split(', '))

if len(names) == 1 and names[0] == '':
    print('No one likes this')
elif len(names) == 1:
    print('{name1} likes this'.format(name1=names[0]))
elif len(names) == 2:
    print('{name1} and {name2} like this'.format(name1=names[0], name2=names[3]))
elif len(names) == 3:
    print('{name1}, {name2} and {name3} like this'.format(name1=names[0], name2=names[1], name3=names[2]))
elif len(names) > 3:
    print('{name1}, {name2} and {count} others like this'.format(name1=names[0], name2=names[2], count=len(names)-2))
