list_1 = list(input()) # вводим лист значений
result = list_1[0]
for i in range(len(list_1)):
    if list_1[i] != result: # проверяем что значение в листе не равно значние в лист_1
        print(False)
        break
else:
 print(True)