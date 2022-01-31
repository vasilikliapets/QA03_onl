import xml.etree.ElementTree as ET

tree = ET.parse('library.xml')
root = tree.getroot()


def find_book_by_title():
    title = input('Введите название книги: ')
    for book in root:
        if title in book.find('title').text:
            print(f"id:{book.attrib['id']}, author:{book.find('author').text}, title:{book.find('title').text}")


book_by_title = root.find(
    "./book[title='Midnight Rain']")  # можно вот так осуществлять поиск, если знаешь название полностью


def find_book_by_price():
    price = input('Введите цену книги (прим. 44.95 или 7): ')
    for book in root:
        if price in book.find('price').text:
            print(f"id:{book.attrib['id']}, author:{book.find('author').text}, title:{book.find('title').text}")


book_by_price = root.find("./book[price='7']")  # можно ещё вот так искать


def find_book_by_author():
    author = input('Введите имя автора (прим. Matthew): ')
    for book in root:
        if author in book.find('author').text:
            print(f"id:{book.attrib['id']}, author:{book.find('author').text}, title:{book.find('title').text}")


def find_book_by_description():
    description = input('Введите описание книги: ')  # попробуйте 'society in England'
    for book in root:
        if description in book.find('description').text:
            print(book.find('title').text, ',', book.find('author').text)

#
# find_book_by_author()
# find_book_by_description()
# find_book_by_price()
# find_book_by_title()
