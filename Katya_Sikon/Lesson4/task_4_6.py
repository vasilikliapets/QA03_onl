# Создать список из элементов list_a = [1,2,3,4,4,5,2,1,8]
# Вывести только уникальные значения и сохранить их в отдельную переменную
# Добавить в полученный объект значение 22
# Сделать list_a неизменяемым
# Измерить его длинну

list_a = [1,2,3,4,4,5,2,1,8]

print('list_a = ',list_a)
uniq_list_a = set(list_a)

print('\nтолько уникальные элементы предыдущего списка\n', uniq_list_a)

uniq_list_a.add(22)
print('\nуникальные элементы + 22\n', uniq_list_a)

unchange_list_a = tuple(list_a)
print('\nнеизменяемый list_a\n', type(unchange_list_a))

print('\nдлина list_a\n', len(unchange_list_a))