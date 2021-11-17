#1

"""
Library
"""

class Book:
    """
    Класс Книга
    """
    book_count = 0
    def __init__(self, name, author, pages, isbn, flag = 0, reserved = 0):
        print(f'Book {name} was added')
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag = flag
        self.reserved = reserved
        Book.book_count += 1


moby_dick = Book('Moby Dick', 'German Melvill', '842', '978-5-04-118395-0')
pinocchio = Book('Pinocchio', 'Carlo Collodi', '72', '978-5-699-88892-4')

class User:
    """
    Класс Пользователь
    """
    def __init__(self, name):
        self.name = name
        print(f'User {name} was added')

    def get_book(self, book):
        if book.flag == 0 and book.reserved == 0:
            print(f'Book {book.name} was taken by {self.name}')
            book.flag = 1
            book.reserved = 1
        elif book.flag == 1:
            print(f'Not possible to take {book.name} by {self.name}')
        elif book.flag == 0 and book.reserved == 1:
            print(f'{self.name} trying to take reserved book {book.name}')
            book.reserved = 0

    def ret_book(self, book):
        if book.flag == 0:
            print(f'Book {book.name} already in library')
        elif book.flag == 1:
            print(f'{self.name} return book {book.name} in library')
            book.flag = 0
            book.reserved = 0

    def res_book(self, book):
        if book.flag == 0 and book.reserved == 0:
            print(f'{self.name} reserved book {book.name}')
            book.reserved = 1
        elif book.flag == 1:
            print(f'Not possible to reserved book {book.name}')
        elif book.reserved == 1:
            print(f'Book {book.name} is reserved by another person')


pavel = User('Pavel')
dima = User('Dima')
pavel.get_book(moby_dick)
dima.get_book(moby_dick)
pavel.ret_book(moby_dick)
dima.get_book(moby_dick)
pavel.res_book(pinocchio)
dima.res_book(pinocchio)
pavel.get_book(pinocchio)
pavel.get_book(pinocchio)


#2

class Bank:    
    def __init__(self, name):
        self.name = name
        print(f'Client {name} was added')

    def deposit(self, amount, term, percent = 10):
        procent_amount = 0
        for i in range(term):
            procent_amount = (amount * percent) / 100
            amount = amount + procent_amount
        return print(f'Deposit for {self.name} will be {amount}')

pavel = Bank('Pavel')
pavel.deposit(100, 7)


#3

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
