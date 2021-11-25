list_1 = list(input())
list_2 = []
for i in range(len(list_1)):
     # находит символ по юникоду
    if list_1[i].isupper(): # в этих пределах находятся все заглавные буквы
        list_2.append(list_1[i]) # если список в пределах от 65 до 90, добавляет это значение в list_2
result = len(list_2) == 0 # если длинна списка равно 0 выводит True
print([result, list_2])
