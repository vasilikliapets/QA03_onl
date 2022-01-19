import json

with open('students.json') as f:
    var = json.load(f)  # парсинг json-файла


# выбор пользователем операции
choise_user = input(f"Выберите тип фильтрации:\n1.По классу\n2.По секции\n3.По полу\n4.По имени (части имени)\n")
result = []  # массив куда записываются найденные результаты
if choise_user not in ["1", "2", "3", "4"]:  # Проверка на входимость в список доступных операций
    print("Недопустимая операция")
else:
    if choise_user == "1":
        search_request = input("Введите номер класса: ")
        for el in var:
            if search_request in el['Class']:  # проверка на вхождение введенного значения в значения по ключу
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению поиск не дал результатов")
    elif choise_user == "2":
        search_request = input("Введите название секции (или часть названия): ")
        for el in var:
            if search_request in el['Club']:
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению поиск не дал результатов")
    elif choise_user == "3":
        search_request = input("Введите пол (M или W): ")
        for el in var:
            if search_request in el['Gender']: # проверка на вхождение введенного значения в значения по ключу
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению поиск не дал результатов")
    elif choise_user == "4":
        search_request = input("Введите имя или его часть: ")
        for el in var:
            if search_request in el['Name']: # проверка на вхождение введенного значения в значения по ключу
                result.append(el)
        if len(result) > 0:
            for i in range(len(result)):
                print(result[i])
        else:
            print("К сожалению поиск не дал результатов")
