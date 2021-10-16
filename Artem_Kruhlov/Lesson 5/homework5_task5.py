list_1 = eval(input()) # вводим лист значений
result = True
for i in range(len(list_1)):
    if list_1[i] != list_1[0]: # проверяем что значение в листе не равно значние в лист_1
        result = False
        break

print(result)
