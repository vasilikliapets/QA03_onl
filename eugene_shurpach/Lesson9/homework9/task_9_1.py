# Библиотека
class Book:
    book_count = 0

    def __init__(self, name, author, q_pages, isbn, booking=False, taking=False):
        print("Книга добавлена в библиотеку!")
        Book.book_count += 1
        self.booking = booking
        self.isbn = isbn
        self.q_pages = q_pages
        self.author = author
        self.name = name
        self.taking = taking

    pass


class User:
    user_count = 0

    def __init__(self, name):
        self.name = name

    def booking(self, Book):
        """Бронирование книги пользователем"""
        if Book.booking is not True and Book.taking is not True:
            print("Книга зарезервирована!")
            Book.booking = True
            return self
        else:
            print("Эта книга зарезервирована! Стоит почитать что-нибудь другое.")

    def taking(self, Book):
        """Пользователь берет книгу"""
        if Book.taking is not True and Book.booking is not True:
            print("Книга взята!")
            Book.taking = True
            return self
        else:
            print("Книги нет в наличии!")

    def returning(self, Book):
        """Пользователь возвращает книгу"""
        Book.taking = False
        print("Книга возвращена!")
        return self

    pass


a = Book("Остров сокровищ", "Роберт Стивенсон", 154, 5042429921)  # добавление книги в библиотеку
# print(a.name)

user = User("Шурпач Евгений")
# print(user.name)
# print(Book.book_count)

user_2 = User("Иванов Ванятко")

user_2.taking(a)  # Книга взята!

user.taking(a)  # Книги нет!
