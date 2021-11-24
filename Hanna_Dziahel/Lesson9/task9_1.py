# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книга или нет. Создайте класс пользователь который может
# брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу (или которую уже кто-то читает) - надо ему про это
# сказать).

class Book:
    """Book description"""

    def __init__(self, name: str, author: str, pages: int, isbn: str):
        """Book properties"""
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved_by_user = None
        self.taken_by_user = None


class User:
    """User properties and methods"""

    def __init__(self, user_name: str):
        """Book properties"""
        self.user_name = user_name
        self.book_name = None

    def reserve_book(self, name: str):
        """
        This function reserves a book
        :param name: str
        :return:
        """
        # Ищем книгу с помощью функции find_book_by_name по name > book || null
        target_book = find_book_by_name(name)
        # Проверяем зарезервирована книга или нет по имени юзера
        # 1 случай - если книга уже зарегистрирована на юзере
        if target_book.reserved_by_user == self.user_name:
            print("You have reserved the book")
            return True
        # 2 случай - если книга зарегистрирована на другом юзере
        elif target_book.reserved_by_user != None:
            print("You can't reserve the book. The book is already reserved "
                  "by another user")
            return False
        # 3 и остальные случаи - резервируем книгу для юзера
        else:
            target_book.reserved_by_user = self.user_name
            print("You have reserved the book")
            return True

    def take_book(self, name: str):
        """
        This function takes a book
        :param name: str
        :return:
        """
        # Ищем книгу с помощью функции find_book_by_name по name > book || null
        target_book = find_book_by_name(name)
        # Проверяем взята книга или нет по имени юзера
        # 1 случай - если книга уже взята юзером
        if target_book.taken_by_user == self.user_name:
            print("You have taken the book before")
            return True
        # 2 случай - если книга взята другим юзером
        elif target_book.taken_by_user != None:
            print("The book is taken by another user")
            return False

        else:
            # 4 случай - если книга зарегистирована юзером или никем не зарегистрирована
            if target_book.reserved_by_user == self.user_name or target_book.reserved_by_user is None:
                # если условие выполнено, записываем имя юзера, что он взял книгу
                target_book.taken_by_user = self.user_name
                # записываем в книги пользователя искомую книгу
                self.book_name = target_book.name
                print("You have taken the book")
                return True

            # 5 случай и другие - если книга взята другим пользователем
            else:
                print(
                    "You can't take the book. The book is already reserved by another user")
                return False

    def return_book(self):
        """
        This function returns a book
        :return:
        """
        # Проверяем есть ли у нас книга
        if self.book_name == None:
            print("You don't have any book")
            return False
        # Если книга есть
        else:
            target_book = find_book_by_name(self.book_name)
            # Убираем флаг о том, что книга взята юзером
            target_book.taken_by_user = None
            # Убираем флаг о том, что книга зарезервирована юзером
            target_book.reserved_by_user = None
            # Убираем данные о том, что у юзера есть книги
            self.book_name = None
            print("You've returned the book")
            return True


books = [
    Book("Flowers for Algernon", "Daniel Keyes", 311, "9780156030083"),
    Book("A Man Called Ove", "Fredrik Backman", 384, "9785905891977")
]


def find_book_by_name(name):
    """
    This function searches book in list of books
    :param name:
    :return:
    """
    global books
    for book in books:
        # проверяем если имя искомой книги есть в списке книг
        if book.name == name:
            return book
        else:
            return None


user = User("Hanna")
user.reserve_book("Flowers for Algernon")
succeed = user.take_book("Flowers for Algernon")
# user.return_book()
user = User("Alex")
user.reserve_book("Flowers for Algernon")
