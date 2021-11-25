class Book:
    def __init__(self, name, author, pages, isbn, status):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.status = Status.AVAILABLE


class Status:
    AVAILABLE = 'available'
    RESERVED = 'reserved'
    NOT_AVAILABLE = 'not_available'


class Reader:
    def __init__(self, full_name):
        self.full_name = full_name

    def reserve_book(self, book):
        if book.status != Status.AVAILABLE:
            print('Book not available')
            return
        book.status = Status.RESERVED

    def pick_up_book(self, book):
        if book.status != Status.AVAILABLE:
            print('Book not available')
            return
        book.status = Status.NOT_AVAILABLE

    def return_book(self, book):
        book.status = Status.AVAILABLE


book1 = Book('TheGreatGatsby', 'ScottFitzgerald', 458, '554-776-8887', 'available')
book2 = Book('Hamlet', 'WilliamShakespeare', 694, '343-34-342', 'available')

reader1 = Reader('Ivanov')
reader2 = Reader('Petrov')

reader1.reserve_book(book1)
print(book1.status)
reader2.reserve_book(book1)
print(book1.status)
reader1.pick_up_book(book2)
print(book2.status)
reader1.return_book(book1)
print(book1.status)


class Invest:
    def __init__(self, name, N, R):
        self.name = name
        self.N = N
        self.R = R


class Bank:

    def deposit(invest):
        amount = invest.N * (1 + 10 / 100 / 12) ** (invest.R * 12)
        return amount


vklad = Invest('Ivanov', 2000, 3)

print(Bank.deposit(vklad))


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


student_1 = Students('Ivanov I.', 1, [6, 6, 7, 7, 8])
student_2 = Students('Petrov P.', 2, [6, 5, 6, 5, 5])
student_3 = Students('Sidorov S.', 1, [7, 7, 8, 9, 9])

School.add_student(student_1)
School.add_student(student_2)
School.add_student(student_3)

School.get_student_with_5_or_6()
School.get_students_group(1)
School.get_students_avt()
