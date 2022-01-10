from statistics import mean


class Students:

    def __init__(self, name, group, marks):
        """This is constructor of student"""
        self.name = name   #фамилия и инициалы студента
        self.group = group    #номер группы
        self.marks = marks    #массив из пяти оценок


class School(Students):
    list_of_students = []

    @staticmethod
    def add_student(student):
        """This function adds student to the list"""
        School.list_of_students.append(student)

    @staticmethod
    def get_names_and_groups():
        """This function prints the students with only marks 5 or 6"""
        stud = {}
        for i in School.list_of_students:
            set_mark = set(i.marks)
            if set_mark == {6} or set_mark == {5} or set_mark == {5, 6} or set_mark == {6, 5}:
                stud[i.name] = i.group
        print(stud)

    @staticmethod
    def get_students_by_group(number_of_group):
        """This function prints the students of one particular group"""
        stud = []
        for i in School.list_of_students:
            if i.group == number_of_group:
                stud.append(i.name)
        print(stud)

    @staticmethod
    def get_students_by_pass():
        """This function prints students who has good marks"""
        stud = []
        for i in School.list_of_students:
            if mean(i.marks) >= 7:
                stud.append(i.name)
        print(stud)


# создаём студентов в классе Students
student_1 = Students('Тюпа Д.И.', 101, [4, 6, 8, 9, 7])
student_2 = Students('Коваленко A.B.', 101, [4, 4, 8, 8, 10])
student_3 = Students('Гайдук T.A.', 103, [5, 5, 5, 5, 6])
student_4 = Students('Иванова О.Н.', 103, [9, 9, 8, 9, 6])

# добавляем студентов в школу
School.add_student(student_1)
School.add_student(student_2)
School.add_student(student_3)
School.add_student(student_4)

# запускаем методы класса School
School.get_names_and_groups()
School.get_students_by_group(101)
School.get_students_by_pass()
