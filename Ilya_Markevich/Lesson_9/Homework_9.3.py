#Студенты

class Students:
    def __init__(self, surname, initials, group, academic_performance):
        self.surname = surname
        self.initials = initials
        self.group = group
        self.academic_performance = academic_performance
        print(f'Student {surname} was added')

class School:
    good_students = {}
    automat_students = {} 
    student_list = {}
    def __init__(self, surname, initials, group, academic_performance):
        self.surname = surname
        self.initials = initials
        self.group = group
        self.academic_performance = academic_performance
        self.student_list[self.surname] = self.group
        print(f'Student {surname} in the school now') 

        aver_score = sum(academic_performance) / len(academic_performance)

        for i in academic_performance:
            if i < 5 or i > 6:
                break
            else:
                self.good_students[self.surname] = self.group

        if aver_score >= 7:
            self.automat_students[self.surname] = self.group

    def student_from_group(self, group):
        students_from_group = []
        for k, v in self.student_list.items():
            if v == group:
                students_from_group.append(k)
        print(f'Студенты из группы {group}: {students_from_group}')
    

        


petrov = School('Petrov', 'I.I.', '1-a', [9, 6, 7, 9, 8])
sidorov = School('Sidorov', 'P.P', '1-a', [5, 5, 6, 5, 6])
ivanov = School('Ivanov', 'F.F.', '2-a', [6, 5, 6, 6, 5])

print(School.student_list)
print(School.good_students)
print(School.automat_students)
print(School.student_from_group(School, '1-a'))
