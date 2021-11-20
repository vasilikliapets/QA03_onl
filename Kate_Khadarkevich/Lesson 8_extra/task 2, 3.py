# 2. Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его
one_list = [4, 11, 5, 3, 7, 14]
sorteist = lambda x: sorted(x)[::-1]
print(sorted_list(one_list))


# 3. Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't',
# и отфильтруйте список имен с помощью функции filter

list_name = ['Katy', 'Natali', 'Alexandr', 'Anna', 'Kostya']
result = filter(lambda x: 't' in x, list_name)
print(list(result))
