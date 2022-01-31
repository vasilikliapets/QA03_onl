import json

with open('students.json') as f:
    students = json.load(f)


# поиск учащихся в одном классе
def find_classmates():
    class_number = input('Введите класс (5а, 3b, 1a, 3a, 1b): ')
    for i in students:
        if i['Class'] == class_number:
            print(i['Name'])


# поиск учащихся в одной секции
def find_clubmates():
    club = int(input("""Выберите секцию:
    1) Chess
    2) Box
    3) Football 
    """))
    if club == 1:
        for i in students:
            if i['Club'] == 'Chess':
                print(i['Name'])
    elif club == 2:
        for i in students:
            if i['Club'] == 'box':
                print(i['Name'])
    elif club == 3:
        for i in students:
            if i['Club'] == 'Football':
                print(i['Name'])
    else:
        print('There is no such option')


# фильтруем по полу
def find_by_gender():
    gender = input('Введите пол ребёнка (M or W): ')
    for i in students:
        if i['Gender'] == gender:
            print(i['Name'])


# находим по имени
def find_by_name():
    name = input('Введите имя или часть имени ребёнка: ')
    for i in students:
        if name in i['Name']:
            print(f"{i['Name']} at {i} in students")

# find_classmates()
# find_clubmates()
# find_by_gender()
# find_by_name()
