# Проверить, все ли элементы одинаковые

list_1 = [1, 1, 1]
list_2 = [1, 2, 1]
list_3 = ['a', 'a', 'a']
list_4 = []

# Создаем переменную с первым значением списка
ele_1 = list_1[0]
chk_1 = True

# Сравниваем каждое значение из списка с первым значением списка через цикл for
for item in list_1:
    if ele_1 != item:
         chk_1 = False
print(chk_1)

# Создаем переменную с первым значением списка
ele_2 = list_2[0]
chk_2 = True

# Сравниваем каждое значение из списка с первым значением списка через цикл for
for item in list_2:
    if ele_2 != item:
         chk_2 = False
print(chk_2)

# Создаем переменную с первым значением списка
ele_3 = list_3[0]
chk_3 = True

# Сравниваем каждое значение из списка с первым значением списка через цикл for
for item in list_3:
    if ele_3 != item:
         chk_3 = False
print(chk_3)

ele_4 = list_4
chk_4 = True

for item in list_4:
    if ele_4 != item:
         chk_4 = False
print(chk_4)




