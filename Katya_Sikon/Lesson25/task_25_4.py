# * Напечатайте номер заказа
# * Напечатайте адрес отправки
# * Напечатайте описание посылки, ее стоимость и кол-во
import datetime
from pprint import pprint
import yaml

with open('order.yaml') as f:
    order = yaml.safe_load(f)


def print_invoice():
    pprint(order['invoice'])


print('Напечатайте номер заказа')
print_invoice()


def print_address():
    pprint(order['bill-to']['address'])


print('Напечатайте адрес отправки')
print_address()


def print_info_product():
    for i in order['product']:
        pprint(i)


print('Напечатайте описание посылки, ее стоимость и кол-во')
print_info_product()


# * Создайте свой yaml файл
def create():
    to_yaml = {'bill-to': {'address': {'city': 'Royal Oak',
                                       'lines': '458 Walkman Dr.\nSuite #292\n',
                                       'postal': 48046,
                                       'state': 'MI'},
                           'family': 'Dumars',
                           'given': 'Chris'},
               'comments': 'Late afternoon is best Backup contact is Nancy Billsmer @ '
                           '338-4338',
               'date': datetime.date(2001, 1, 23),
               'invoice': 34843,
               'product': [{'description': 'Basketball',
                            'price': 450.0,
                            'quantity': 4,
                            'sku': 'BL394D'},
                           {'description': 'Super Hoop',
                            'price': 2392.0,
                            'quantity': 1,
                            'sku': 'BL4438H'}],
               'ship-to': {'address': {'city': 'Royal Oak',
                                       'lines': '458 Walkman Dr.\nSuite #292\n',
                                       'postal': 48046,
                                       'state': 'MI'},
                           'family': 'Dumars',
                           'given': 'Chris'},
               'tax': 251.42,
               'total': 4443.52}
    with open('new_file.yaml', 'w') as f:
        yaml.dump(to_yaml, f)
    with open('new_file.yaml') as f:
        print(f.read())


print('Создайте свой yaml файл')
create()
