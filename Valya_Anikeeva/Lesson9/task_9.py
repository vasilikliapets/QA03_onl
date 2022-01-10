# 1 Library
class Book:
    def __init__(self, name, author, pages, isnb):
        """This is constructor of book"""
        self.name = name
        self.author = author
        self.pages = pages
        self.isnb = isnb
        self.status = True


class Users:
    def __init__(self, name):
        """This is constructor of reader"""
        self.name = name

    def get_book(self, book):
        """This function takes a book by reader"""
        if book.status == True:
            print('Книга ваша')
            book.status = False
        elif book.status == False:
            print('Книгу читает кто-то другой')
        elif 'Reserved' in book.status:
            if self == book.status[1]:
                print('Книга ваша')
                book.status = False
            else:
                print('Книга зарезервирована кем-то другим')

    def reserve_book(self, book):
        """This function reserves a book by reader"""
        if book.status == True:
            print('Книга зарезервирована вами')
            book.status = ['Reserved', self]
        elif book.status == False:
            print('Книгу читает кто-то другой')
        elif 'Reserved' in book.status:
            if self == book.status[1]:
                print('Книга уже была зарезервирована вами')
            else:
                print('Книга зарезервирована кем-то другим')

    def return_book(self, book):
        """This function returns a book by reader"""
        if book.status == False:
            print('Спасибо что вернули книгу')
            book.status = True
        elif book.status == True:
            print('Книга уже была возвращена, обратитесь к библиотекарю')
        else:
            print('Обратитесь к библиотекарю')


book1 = Book('The Shining', 'Stephen King', 544, '10364173')
book2 = Book('Inferno', 'Dan Brown', 546, '10289925')

user1 = Users('Дэн Перов')
user2 = Users('Алина Мацкевич')

user1.get_book(book1)
user2.get_book(book1)
user1.reserve_book(book2)
user2.get_book(book2)


# 2 Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
# прибавляются к сумме инвестиции ежемесячно)
class Investment:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    pass


class Bank:
    @staticmethod
    def deposit(investment):
        """Расчет процентов с капитализацией"""
        summ = investment.n * (1 + 10 / 100 / 12) ** (investment.r * 12)
        return summ


invest1 = Investment(2000, 3)

print(Bank.deposit(invest1))


# 3 Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (массив из пяти элементов)

class Students:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress


class School(Students):
    student_list = []

    @staticmethod
    def add_student(student):
        School.student_list.append(student)

    @staticmethod
    def get_student_with_5_or_6():
        students = {}
        for i in School.student_list:
            if set(i.progress) == {6} or set(i.progress) == {5} or set(i.progress) == {5, 6}:
                students[i.name] = i.group
        print(students)

    @staticmethod
    def get_students_group(group_number):
        stud = []
        for i in School.student_list:
            if i.group == group_number:
                stud.append(i.name)
        print(stud)

    @staticmethod
    def get_students_avt():
        stud = []
        for i in School.student_list:
            if sum(i.progress) / len(i.progress) >= 7:
                stud.append(i.name)
        print(stud)


student1 = Students('Guzin D.A.', 1, [5, 7, 6, 7, 7])
student2 = Students('Kruk B.B.', 2, [5, 5, 5, 5, 5])
student3 = Students('Ivanov I.I.', 2, [8, 7, 7, 9, 9])
student4 = Students('Antonova A.M.', 3, [7, 8, 8, 7, 8])

School.add_student(student1)
School.add_student(student2)
School.add_student(student3)
School.add_student(student4)

School.get_student_with_5_or_6()
School.get_students_group(1)
School.get_students_avt()
