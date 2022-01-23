"""
Разработайте поиск книги в библиотеке по:
1) автору(часть имени)
2) цене
3) заголовку
4) описанию.

"""

import xml.etree.ElementTree as ET

with open("library.xml", "r") as f:
    xml_string = f.read()
    root = ET.fromstring(xml_string)


def find_by_author():
    """
    Find book by author
    """
    name_author = input('Введите имя автора:')

    for book in root.findall('book'):
        if name_author in book.find('author').text:
            author = book.find('author').text
            title = book.find('title').text
            print(f"Автор: {author}. Название книги: {title}")


def find_by_price():
    """
    Find book by price
    """

    price_book = input('Введите стоимость книги(прим: 36.75):')
    for book in root.findall('book'):
        if price_book in book.find('price').text:
            author = book.find('author').text
            title = book.find('title').text
            price = book.find('price').text
            print(f"Автор: {author}. Название книги: {title}. Цена: {price}")


def find_by_title():
    """
    Find book by Title Eng
    """
    title_book = input('Введите название книги (Eng):')
    for book in root.findall('book'):
        if title_book in book.find('title').text:
            author = book.find('author').text
            title = book.find('title').text
            print(f"Автор: {author}. Название книги: {title}")


def find_by_description():
    """
    Find book by description (Eng)
    """
    descript_book = input('Введите описание необходимой книги (Eng):')
    for book in root.findall('book'):
        if descript_book in book.find('description').text:
            author = book.find('author').text
            title = book.find('title').text
            description = book.find('description').text
            print(f"Автор: {author}. Название книги: {title}. Описание: {description}")

# 1 Поиск по имени автора или части имени
# find_by_author()

# 2 Поиск книги по цене
# find_by_price()

# 3 Поиск книги по Названию
# find_by_title()

# 4 Поиск книги по Описанию
# find_by_description()
