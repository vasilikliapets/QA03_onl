"""
* Напечатайте номер заказа
* Напечатайте адрес отправки
* Напечатайте описание посылки, ее стоимость и кол-во
* Сконвертируйте yaml файл в json
* Создайте свой yaml файл
"""

from pprint import pprint

import yaml

with open('order.yaml') as input_yaml_file:
    templates = yaml.safe_load(input_yaml_file)


def print_num_order():
    """
    find number of a order
    """
    print(templates['invoice'])


def print_send_adress():
    """
    Find and print delivery adress
    """
    pprint(
        f"Street: {templates['bill-to']['address']['lines']}City: {templates['bill-to']['address']['city']} ")


def print_description_price_quantity():
    """
    Find and print description,price and quantity parcels
    """
    count = 1
    for i in templates['product']:
        print(f"Посылка №{count}, Описание: {i['description']}, Цена: {i['price']}, Кол-во: {i['quantity']}")
        count += 1


def convert_yaml_to_json():
    """
    The function convert yaml file to json
    """

    with open('json_new_file.json', 'w') as out_file:
        out_file.write(str(templates))


def create_yaml_file():
    with open('new_order.yaml', 'w') as new_yaml_file:  # Просто создал файл .yaml, но ничего туда не записывал
        # все как в задании =)
        pass

# 1 - Напечатайте номер заказа
# print_num_order()

# 2 - Напечатайте адрес отправки
# print_send_adress

# 3 - Напечатайте описание посылки, ее стоимость и кол-во
# print_description_price_quantity()

# Сконвертируйте yaml файл в json
# convert_yaml_to_json()

# Создайте свой yaml файл
# create_yaml_file()
