# Разработайте поиск учащихся в одном классе, посещающих одну секцию.
# Фильтрацию учащихся по их полу.
# Поиск ученика по имени(часть имени)

import json

with open('students.json') as f:
    file_content = f.read()
    students_info = json.loads(file_content)


def search_by_class():
    class_school = input('Введите класс:')
    for i in students_info:
        if class_school in i['Class']:
            print(i['Name'] + ' ' + i['Class'])


print('поиск учащихся в одном классе')
search_by_class()


def search_by_club():
    club = input('Введите секцию:')
    for i in students_info:
        if club in i['Club']:
            print(i['Name'] + ' ' + i['Class'] + ' ' + i['Club'])


print('\nпоиск учащихся, посещающих одну секцию')
search_by_club()


def filter_by_gender():
    gender = input('Введите пол ученика: \nВозможные варианты:\n-M - мальчик\n-W - девочка\n')
    for i in students_info:
        if gender == i['Gender']:
            print(i['Name'] + ' ' + i['Gender'] + ' ' + i['Class'])


print('\nФильтрация учащихся по их полу')
filter_by_gender()


def search_by_name():
    name = input('Введите имя ученика:')
    for i in students_info:
        if name in i['Name']:
            print(i['Name'] + ' ' + i['Class'])


print('\nПоиск ученика по имени(часть имени)')
search_by_name()
