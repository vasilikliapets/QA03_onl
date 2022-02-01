# Разработайте поиск книги в библиотеке по ее автору(часть имени)/цене/заголовку/описанию.

import xml.etree.ElementTree as ET

with open("library.xml", "r") as f:
    xml_string = f.read()

root = ET.fromstring(xml_string)


def search_by_author():
    author = input('Введите автора книги:')

    for book in root.findall('book'):
        if author in book.find('author').text:
            print(book.find('author').text + ' ' + book.find('title').text + ' ' + '\ngenre:' + book.find('genre').text
                  + '\nprice:' + book.find('price').text + '\npublish date:' + book.find('publish_date').text +
                  '\ndescription:' + book.find('description').text)


print('поиск книги по ее автору(часть имени)')
search_by_author()


def search_by_price():
    price = float(input('Введите стоимость книги:'))

    for book in root.findall('book'):
        if price == float(book.find('price').text):
            print(book.find('author').text + ' ' + book.find('title').text + ' ' + '\ngenre:' + book.find('genre').text
                  + '\nprice:' + book.find('price').text + '\npublish date:' + book.find('publish_date').text +
                  '\ndescription:' + book.find('description').text)


print('\nпоиск книги по ее цене')
search_by_price()


def search_by_title():
    title = input('Введите заголовок книги:')

    for book in root.findall('book'):
        if title in book.find('title').text:
            print(book.find('author').text + ' ' + book.find('title').text + ' ' + '\ngenre:' + book.find('genre').text
                  + '\nprice:' + book.find('price').text + '\npublish date:' + book.find('publish_date').text +
                  '\ndescription:' + book.find('description').text)


print('\nпоиск книги по ее заголовку')
search_by_title()


def search_by_description():
    description = input('Введите описание книги:')

    for book in root.findall('book'):
        if description in book.find('description').text:
            print(book.find('author').text + ' ' + book.find('title').text + ' ' + '\ngenre:' + book.find('genre').text
                  + '\nprice:' + book.find('price').text + '\npublish date:' + book.find('publish_date').text +
                  '\ndescription:' + book.find('description').text)


print('\nпоиск книги по ее описанию')
search_by_description()
