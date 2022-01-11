# 1. Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом, зарезервирована ли книга или нет.
# Создайте класс пользователь который может брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, page_count, isbn, status=True):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.status = status


class Reader:
    def __init__(self, name):
        self.name = name

    def reserved_book(self, book):
        if book.status == True:
            print(f"{self.name}, книга {book.name} Вами зарезервирована")
            book.status = ("Reserved", self)
        elif book.status == False:
            print(f"Книга {book.name} зарезервирована кем то")
        elif 'Reserved' in book.status:
            if self in book.status:
                print(f"{self.name}, книга {book.name} уже зарезервирована Вами")
            else:
                print(f"{self.name}, извините, книга {book.name} уже зарезервирована кем то")

    def take_book(self, book):
        if book.status == True:
            print(f"{self.name}, Вы взяли книгу {book.name}")
            book.status = False
        elif book.status == False:
            print(f"Книгу {book.name} читают")
        elif "Reserved" in book.status:
            if self in book.status:
                print(f"{self.name}, Вы получили зарезервированную Вами книгу {book.name}")
                book.status = False
            else:
                print(f"{self.name}, извините, книга {book.name} уже зарезервирована кем то")

    def return_book(self, book):
        book.status = True
        print(f"{self.name}, Вы вернули книгу {book.name}")


book_1 = Book("Гарри Поттер 1", "Дж.Роулинг", 432, "978-5-389-07435-4")
book_2 = Book("Игра престолов", "Джордж Р.Р. Мартин", 768, "978-5-17-114463-0")

reader1 = Reader("Сергей")
reader2 = Reader("Ирина")

reader1.reserved_book(book_1)
reader2.take_book(book_1)
reader1.take_book(book_1)
reader2.take_book(book_1)
reader1.return_book(book_1)
reader2.take_book(book_1)

# 2. Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью
# ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.

class Investment:
    def __init__(self, n, r):
        self.n = n
        self.r = r


class Bank:

    def deposit(investment):
        result = investment.n * ((1 + 10 / 100 / 12) ** (investment.r * 12))
        return round(result, 2)


invest1 = Investment(200, 5)
print(Bank.deposit(invest1))

# 3. Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов)

# Создать класс School:
# Добавить возможность для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

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


student_1 = Students('Иванов И.И.', 1, [6, 5, 9, 10, 8])
student_2 = Students('Мохарев П.А.', 2, [6, 6, 6, 6, 5])
student_3 = Students('Козлов С.А.', 1, [7, 7, 8, 9, 9])

School.add_student(student_1)
School.add_student(student_2)
School.add_student(student_3)

School.get_student_with_5_or_6()
School.get_students_group(1)
School.get_students_avt()