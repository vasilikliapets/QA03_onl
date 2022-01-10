class Book:
    def __init__(self, pages, year, author, price):
        if isinstance(pages, int):
            self.pages = pages
        else:
            raise PagesNumberError
        if isinstance(year, int) and len(str(year)) == 4:
            self.year = year
        else:
            raise PublicationYearError
        if isinstance(author, str) and author != '':
            self.author = author
        else:
            raise AuthorNameError
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise PriceValueError


class MyExceptions(Exception):  # в этом классе я создаю пользовательские ошибки
    """This is basic class for exceptions"""


class PagesNumberError(MyExceptions):
    def __init__(self, message='The number of pages must be an integer'):
        super().__init__(message)


class PublicationYearError(MyExceptions):
    def __init__(self, message='Year of publication must be a four-digit integer'):
        super().__init__(message)


class AuthorNameError(MyExceptions):
    def __init__(self, message='The author name is mandatory and must only be set as string type'):
        super().__init__(message)


class PriceValueError(MyExceptions):
    def __init__(self, message='The price must be specified as an integer or floating point number'):
        super().__init__(message)
