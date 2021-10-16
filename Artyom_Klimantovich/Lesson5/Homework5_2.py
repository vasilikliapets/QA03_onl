name = input('Ввудите имена через запятую:')
list = name.split(',')

if len(list) == 1 and list[0] != '':
    print(list[0] + " likes this")
elif len(list) == 2:
    print(list[0] + ' and ' + list[1] + " like this")
elif len(list) == 3:
    print(list[0] + ',' + list[1] + ' and ' + list[2] + " like this")
elif len(list) >= 4:

    print(list[0] + ',' + list[1] + ' and ' + str(len(list[2:])) + " others like this")
else:
    print("No one likes this")



