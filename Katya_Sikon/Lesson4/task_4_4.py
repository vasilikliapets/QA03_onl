# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6

s4 = [1,2,4,5,6,6,7,8,9,10]

print('\nсписок из 10 элементов\n', s4)

s4.insert(2, 3)
del s4[6]

print('\nсписок с изменениями\n', s4)