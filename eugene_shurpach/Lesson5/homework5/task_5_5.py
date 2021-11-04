# Проверить, все ли элементы одинаковые
list_1 = ['F', 4, 4]
print(all(i == list_1[0] for i in list_1))  # Сравниваю первое значение с каждым последующим в списке

list_1 = ['F', 3, 4]
print( not all(i == list_1[0] for i in list_1))