a = [1, 2, 3]
b = [4, 5, 6]
print(a[1])      # извлекаем из 1 списка 2 элемент

b[2] = 8           # изменяем во 2 списке последний элемент
print(b)

c = a + b            # соединяем оба списка
print(c)

print(sorted(c[1:3:1] + c[-2:-4:-1]))

c.append('wow')           # добавляем два новых элемента
c.append('num')
print(c)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a).intersection(set(b))))    # выводим список из общих элементов

list_1= [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(list_1)))          # выводим только уникальные значения