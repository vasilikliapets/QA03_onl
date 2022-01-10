class Students:
    def __init__(self, lastname_and_initials, num_group, rate):
        self.lastname_and_initials = lastname_and_initials
        self.num_group = num_group
        self.rate = rate


class School:
    students_list = []

    @staticmethod
    def add_to_school(student):  # Добавление студентов в группу
        School.students_list.append(student)

    @staticmethod
    def print_students_rate_5_6():  # Вывод фамилий и номеров групп имеющие оценки равные только 5 или 6
        for i in School.students_list:
            if set(i.rate) == {5} or set(i.rate) == {6}:
                print(f"Студент - {i.lastname_and_initials} из группы №{i.num_group} имеет только оценки 5 или 6")

    @staticmethod  # Добавить возможность вывода учеников заданной группы
    def print_student_group(numb):  # В numb входит нужное
        for i in School.students_list:
            if numb == i.num_group:
                print(i.lastname_and_initials)

    @staticmethod
    def print_automat_students():  # вывода учеников претендующих на автомат(средний балл >= 7)
        for i in School.students_list:
            if sum(i.rate) / len(i.rate) >= 7:
                print(i.lastname_and_initials)


student1 = (Students("Andry A.B", 3, [1, 2, 3, 4, 5]))
student2 = (Students("Vasya B.C", 3, [3, 4, 5, 4, 5]))
student3 = (Students("Olya K.C", 2, [5, 5, 5, 5, 5]))
student4 = (Students("Kirill P.A", 4, [3, 5, 4, 5, 5]))
student5 = (Students("Oleg M.P", 4, [5, 5, 5, 5, 5]))
student6 = (Students("Koc K.M", 2, [9, 8, 8, 8, 8]))
student7 = (Students("Mac Q.W", 1, [6, 6, 6, 6, 6]))
student8 = (Students("Kate X.Z", 1, [9, 7, 7, 6, 7]))

School.add_to_school(student1)
School.add_to_school(student2)
School.add_to_school(student3)
School.add_to_school(student4)
School.add_to_school(student5)
School.add_to_school(student6)
School.add_to_school(student7)
School.add_to_school(student8)

School.print_students_rate_5_6()
School.print_automat_students()
