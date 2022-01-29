import yaml
from pprint import pprint
import json

with open('order.yaml') as f:
    order = yaml.safe_load(f)


# печатаем номер заказа
def print_invoice():
    print(order['invoice'])


# печатаем адресс доставки
def print_address():
    pprint(order['bill-to']['address'])


# печатаем описание товаров, цену и количество
def print_about_order():
    count = 0
    for i in order['product']:
        count += 1
        print(f"Product #{count}: {i['description']}, price {i['price']}, quantity {i['quantity']}")


# ковертируем yaml в json
def converter():
    with open('order.yaml', 'r') as yaml_in, open('order.json', 'w') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        yaml_object['date'] = str(
            yaml_object['date'])  # пришлось дату перевести в тип стринг, т.к. формат даты json не поддерживает
        json.dump(yaml_object, json_out)


# создать свой файл yaml
def create_yaml():
    my_own = {'stuff':
                  {'employer':
                       {'name': 'Denis Syraeshko', 'age': 32, 'email': 'denis@gmail.com'},
                   'employees': [{'name': 'Daria Tyupa', 'age': 28, 'position': 'QA', 'email': 'darya@gmail.com'},
                                 {'name': 'Pavel Nikolin', 'age': 35, 'position': 'DEV', 'email': 'pavel@gmail.com'}]}}
    with open('my_own.yaml', 'w') as f:
        yaml.dump(my_own, f)


# print_invoice()
# print_address()
# print_about_order()
# converter()
# create_yaml()
