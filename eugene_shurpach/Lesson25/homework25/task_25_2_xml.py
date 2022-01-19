import xml.etree.ElementTree as ET


def parseXML(xml_str):  # парсинг XML в dict
    with open(xml_str) as f:
        xml_string = f.read()
    root = ET.fromstring(xml_string)

    book_dict = {}  # создание дикта для каждой книги
    books = []  # лист с диктами по книгам
    for book in root:   # цикл для формирования ключ:значения по каждой книге
        for elem in book:
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            book_dict[elem.tag] = text

        if book.tag == "book":  # добавление диктов с книгами в лист
            books.append(book_dict)
            book_dict = {}
        # print(books)
    return books


var = parseXML("library.xml")

# Выбор пользователем типа поиска
choise_user = input(f"Выберите тип поиска:\n1.По автору (части имени)\n2.По описанию\n3.По заголовку\n4.По цене\n")
result = []
if choise_user not in ["1", "2", "3", "4"]:  # Проверка на входимость в список доступных операций
    print("Недопустимая операция")  # защита от ввода не из списка поиска
else:
    if choise_user == "1":
        search_request = input("Введите имя автора (или часть): ")
        for el in var:
            if search_request in el['author']:  # проверка на вхождение введенного значения в значения по ключу
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):  # вывод результата поиска
                print(result[i])
        else:
            print("К сожалению в библиотеке нет таких книг")  # вывод, если в результатах поиска пустой массив
    elif choise_user == "2":
        search_request = input("Введите описание или его часть: ")
        for el in var:
            if search_request in el['description']:
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению в библиотеке нет таких книг")
    elif choise_user == "3":
        search_request = input("Введите заголовок или его часть: ")
        for el in var:
            if search_request in el['title']:
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению в библиотеке нет таких книг")
    elif choise_user == "4":
        search_request = input("Введите цену: ")
        for el in var:
            if search_request in el['price']:
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению в библиотеке нет таких книг")


if __name__ == "__main__":
    parseXML("library.xml")
