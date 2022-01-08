class Book:
    def __init__(self, pages, year, author, price):
        if isinstance(pages, int):
            self.pages = pages
        else:
            raise MyException("Число страниц должно быть целым числом. Попробуй еще раз!")

        if isinstance(year, int) and len(str(year)) == 4:
            self.published_in = year
        else:
            raise MyException("Год издания должен состоять из 4-ех цифр. Попробуй еще раз!")

        if isinstance(author, str):
            self.author = author
        else:
            raise MyException("Автор должен указываться текстовой строкой")

        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise MyException("Цена должна быть числом.")


class MyException(Exception):
    def __init__(self, text):
        self.text = text


book_1 = Book(123, 1985, "Автор", 2.55)
book_2 = Book(12,  1985, "Автор", "f")