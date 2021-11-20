# 2. Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его
one_list = ['4', '11', '5', '3', '77', '14']
sorted_list = sorted(one_list, key=lambda x: int(x[0:]))
print(sorted_list)


# 3. Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't',
# и отфильтруйте список имен с помощью функции filter

list_name = ['Katy', 'Natali', 'Alexandr', 'Anna', 'Kostya']
result = filter(lambda x: 't' in x, list_name)
print(list(result))
