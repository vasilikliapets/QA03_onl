# Создайте программу, которая, принимая массив имён,
# возвращает строку описывающая количество лайков (как в Facebook).

name = input('Who likes ')
# Через метод split() разбиваю строку на части, используя как разделитель ','
# и создаю на основе этого список
list = name.split(',')

# Через метод len() узнаю количество элементов в листе
# и на основании этого формирую условия и шаблоны сообщений
if len(list) == 1 and list[0] != '':
    print(list[0] + " likes this")
elif len(list) == 2:
    print(list[0] + ' and' + list[1] + " like this")
elif len(list) == 3:
    print(list[0] + ',' + list[1] + ' and' + list[2] + " like this")
elif len(list) >= 4:
# Через использование индексов и срезов в списке узнаем количество others
    print(list[0] + ',' + list[1] + ' and ' + str(len(list[2:])) + " others like this")
else:
    print("No one likes this")
