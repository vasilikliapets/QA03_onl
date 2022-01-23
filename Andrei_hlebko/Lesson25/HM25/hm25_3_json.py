"""
Разработайте поиск:
1) Учащихся в одном классе
2) Посещающих одну секцию.
3) Фильтрацию учащихся по их полу.
4) Поиск ученика по имени(часть имени)

"""

import json

with open('students.json', 'r') as f:
    text_students = json.load(f)


# 1
def find_students_by_class():
    """
    The function find student by input value number of class(e.g. 3a or 1b)
    """
    class_num_student = input("Введите номер класса(Прим:3a,1b):")
    for student in text_students:
        if class_num_student == student["Class"]:
            print(f"ID студента: {student['ID']}, Имя и Фамилия: {student['Name']}, Номер Класса: {student['Class']}")


# 2
def find_students_by_club():
    """
    The function find student by input value club(e.g. Football or Chess)
    """
    class_num_student = input("Введите название секции учеников(Прим: Football, Chess):")
    for student in text_students:
        if class_num_student == student["Club"]:
            print(f"ID студента: {student['ID']}, Имя и Фамилия: {student['Name']}, Тип секции: {student['Club']}")


# 3
def find_students_by_gender():
    """
    The function find student by input gender(e.g. M or W)
    """
    class_num_student = input("Введите пол учеников(M or W):")
    for student in text_students:
        if class_num_student == student["Gender"]:
            print(f"ID студента: {student['ID']}, Имя и Фамилия: {student['Name']}, Пол ученика: {student['Gender']}")


# 4
def find_student_by_name():
    """
    The function find student by input name or part of name(e.g. Senpai or enp)
    """
    name_student = input("Введите имя ученика или часть имени:")
    for student in text_students:
        if name_student in student["Name"]:
            print(f"ID студента: {student['ID']}, Имя и Фамилия: {student['Name']}")

# 1 - Поиск ученика по номеру класса прим 3a
# find_students_by_class()

# 2 - Поиск ученика Посещающих одну секцию
# find_students_by_club()

# 3 - Поиск ученика по полу
# find_students_by_gender()

# 4 - Поиск ученика по имени или части имени
# find_student_by_name()
