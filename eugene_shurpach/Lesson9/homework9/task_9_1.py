# Библиотека
class Book:
    book_count = 0

    def __init__(self, name, author, q_pages, isbn, booking=None, taking=None):
        print("Книга добавлена в библиотеку!")
        Book.book_count += 1
        self.booking = booking
        self.isbn = isbn
        self.q_pages = q_pages
        self.author = author
        self.name = name
        self.taking = taking


class User:
    user_count = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def booking(self, book, user):
        """Бронирование книги пользователем"""
        if book.booking is not None:
            if book.booking != user.id:
                print(f"Книга {book.name} зарезервирована! Стоит почитать что-нибудь другое.")
        elif book.booking is None and book.taking is None:
            print(f"Книга {book.name} вами зарезервирована!")
            book.booking = user.id

    def taking(self, book, user):
        """Пользователь берет книгу"""
        if book.taking is None and book.booking in {None, user.id}:
            print(f"Книга {book.name} успешно взята!")
            book.taking = user.id
        elif book.booking != user.id:
            print(f"Книги {book.name} сейчас нет в наличии или она зарезервирована другим читателем!")


    def returning(self, book, user):
        """Пользователь возвращает книгу"""
        if book.taking == user.id:
            book.booking = None
            book.taking = None
            print(f"Книга {book.name} возвращена!")
        else:
            print("Нельзя вернуть книгу, которую не брал!")


b_1 = Book("Остров сокровищ", "Роберт Стивенсон", 154, 5042429921)
b_2 = Book("book2", "Роберт Стивенсон", 154, 5042429921)

user_1 = User(1, "Шурпач Евгений")
user_2 = User(2, "Иванов Ванятко")
user_1.booking(b_1, user_1)
user_2.taking(b_1, user_2)
user_2.booking(b_1, user_2)
user_2.returning(b_1, user_2)
user_1.taking(b_1, user_1)
user_1.returning(b_1, user_1)
user_2.taking(b_1, user_2)
