# 1-Библиотека

class Book:
    def __init__(self, name_book, author_book, num_of_pages, isbn, status=True):
        self.name_book = name_book
        self.author_book = author_book
        self.num_of_pages = num_of_pages
        self.isbn = isbn
        self.status = status


class User:
    def __init__(self, name):
        self.name = name

    def take_book(self, book):
        if book.status == True:
            print(f"{self.name}, книга {book.name_book} автора {book.author_book} вами получена")
            book.status = False

        elif book.status == False:
            print(f"К сожалению Книга {book.name_book} автора {book.author_book} в данный момент недоступна к чтению")
        elif "Reserved" in book.status:
            if self in book.status:
                print(f"{self.name}, зарезервированная книга {book.name_book} вами получена")
                book.status = False
            else:
                print(f"К сожалению книга {book.name_book} автора {book.author_book} зарезервирована кем-то другим")

    def return_book(self, book):
        book.status = True
        print(f"{self.name}, Спасибо что вернули книгу {book.name_book}!")

    def do_reserve_book(self, book):
        if book.status == True:
            print(f"Книга {book.name_book} Вами зарезервирована")
            book.status = ['Reserved', self]
        elif book.status == False:
            print(f"Книга {book.name_book} зарезервирована кем-то другим")
        elif 'Reserved' in book.status:
            if self in book.status:
                print(f"Эта книга {book.name_book} уже была зарезервирована вами {self.name}")
            else:
                print(f"К сожалению книга {book.name_book} уже зарезервирована другим пользователем")


book1 = Book("World", "Pushkin", 100, 1234567890)
book2 = Book("Exit", "King", 300, 987654321)
book3 = Book("Enter", "Gypson", 500, 5678901233)

user1 = User("Vasya")
user2 = User("Petya")
user3 = User("Darya")
