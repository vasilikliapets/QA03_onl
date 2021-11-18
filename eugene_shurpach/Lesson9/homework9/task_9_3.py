# Students
import statistics

class Students:
    def __init__(self, name, group, performance):
        """Конструктор класса Students"""
        self.name = name
        self.group = group
        self.performance = performance


class School:
    list_of_student = []

    @staticmethod
    def add_student(Students):
        School.list_of_student.append(Students)
        pass

    def print_name():
        a = []
        for i in School.list_of_student:
            a.append(i.name + str(i.group))
        return a

    def get_name_and_group():
        """Отбор по успеваемости - оценки 5 и 6 - имени и группы студента"""
        list_stud_perf = []  # Список студентов, куда добавляются на основе отбора
        for i in School.list_of_student:
            a = i.performance  # списки с успеваемостью для каждого студента
            if all(b in {5, 6} for b in a):
                list_stud_perf.append(i.name + ";Группа " + str(i.group))
        return list_stud_perf

    def get_stud_of_group(b):
        grouplist = []
        for i in School.list_of_student:
            a = i.group
            if a == b:
                grouplist.append(i.name)
        return grouplist

    def stud_auto():
        list_auto = []
        for i in School.list_of_student:
            a = i.performance
            if statistics.mean(a) >= 7:
                list_auto.append(i.name)
        return list_auto


stud_1 = Students("Шурпач ЕА", 2, [5, 5, 5, 6, 5])
stud_2 = Students("Иванов ЕА", 3, [8, 10, 8, 10, 9])

School.add_student(stud_1)
School.add_student(stud_2)

print(School.stud_auto())
