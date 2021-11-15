class Book:
    def __init__(self, name, author, pages, isnb):
        """This is constructor of book"""
        self.name = name
        self.author = author
        self.pages = pages
        self.isnb = isnb
        self.status = True


class Reader:
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


# создаём объекты в классе Book
book_1 = Book('Glue', 'Irvine Welsh', 720, '978-5-699-24900-8')
book_2 = Book('Осени не будет никогда', 'Дмитрий Липскеров', 320, '5-17-041211-2')
book_3 = Book('Pornographer\'s Poem', 'Michael Turner', 270, '5-17-020508-2')

# создаём читателей
reader_1 = Reader('Иван Иванов')
reader_2 = Reader('Петр Петров')
reader_3 = Reader('Сидр Сидоров')

reader_1.get_book(book_1)  # книга ваша
reader_2.get_book(book_1)  # книгу читает кто-то другой
reader_3.reserve_book(book_2)  # книга зарезервирована вами
reader_2.get_book(book_2)  # Книга зарезервирована кем-то другим
