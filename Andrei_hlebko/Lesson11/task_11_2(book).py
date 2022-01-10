class Book:
    def __init__(self, pages, published_in, author, price):
        if isinstance(pages, int):
            self.pages = pages
        else:
            raise MyException("Wrong type for pages, please write correct data type: integer")

        if isinstance(published_in, int) and len(str(published_in)) == 4:
            self.published_in = published_in
        else:
            raise MyException("Wrong type for year, please write correct data type: integer")

        if isinstance(author, str):
            self.author = author
        else:
            raise MyException("Wrong type for name author, please write string format")

        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise MyException("Wrong type for price, please write correct data format: int or float ")


class MyException(Exception):
    def __init__(self, text):
        self.text = text


# Correct
book1 = Book(500, 1989, "Pushkin", 500)
book2 = Book(300, 1995, "Johnson", 900)
book3 = Book(800, 2020, "Pushkin", 1100)

# Incorrect
book4 = Book("500", 1989, "Pushkin", 500)  # fail1-pages
# book5 = Book(500, "hello", "Pushkin", 500)  # fail2-year
# book6 = Book(500, 1989, 999, 500)  # fail3-Author
# book7 = Book(500, 1989, "Pushkin", [1, 4, 5])  # fail4-price
