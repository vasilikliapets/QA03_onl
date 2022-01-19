import json

import yaml
from pprint import pprint

with open('order.yaml') as f:
    templates = yaml.safe_load(f)  # пасринг yml файла

# Вывод на печать параметров
pprint(f"Номер заказа: {templates['invoice']}")
pprint(f"Адрес доставки: {templates['ship-to']['address']['lines']}, "
       f"{templates['ship-to']['address']['city']}, "
       f"{templates['ship-to']['address']['state']}, "
       f"{templates['ship-to']['address']['postal']}")
for i in range(len(templates['product'])):
    # вывод по принципу (список диктов)(номер элемента в списке)(значение по ключу из дикта)
    pprint(f"Посылка {i+1}:{templates['product'][i]['description']}, "  
           f"{templates['product'][i]['price']}, "
           f"{templates['product'][i]['quantity']}")


templates['date']='23-01-2001' # дата распознается как объект и не сериализируется, подправляю файл для конвертации
with open('order.json', 'w') as fp:
    json.dump(templates, fp)

to_yaml = {'trunk': 2855, 'access': 12}  # рандомный дикт для конвертации

with open('file.yaml', 'w') as f:
    yaml.dump(to_yaml, f)  # запись в файл
