# Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': “”}
#
# 1. Создайте словарь, который будет содержать в себе все элементы обоих словарей
# 2. Обновите словарь “a” элементами из словаря “b”
# 3. Проверить что все значения в словаре “a” не пустые либо не равны нулю
# 4. Проверить что есть хотя бы одно пустое значение (результат выполнения должен быть True)
# 5. Отсортировать словарь по алфавиту в обратном порядке
# 6. Изменить значение под одним из ключей и вывести все значения

slovar_a = {'a': 1, 'b': 2, 'c': 3}
slovar_b = {'c': 3, 'd': 4, 'e': ""}
slovar_all = {**slovar_a, **slovar_b}  # 1

slovar_a.update(slovar_b)  # 2

print("3-",all(slovar_a.values()))#3
# print(all(val in zna4_empty for val in slovar_a.values()))# 3 -Версия сложнее c for

print("4-", "" in slovar_a.values() or [] in slovar_a.values() or {} in slovar_a.values())#4

# print(any(val in zna4_empty for val in slovar_b.values()))# 4 - Версия сложнее с for

zna4_empty = ["", [], {}]#4 - версия с list
print("4(2)-",zna4_empty[0] in slovar_a.values() or zna4_empty[1] in slovar_a.values() or zna4_empty[2]
      in slovar_all.values()) #4 - версия с list


for i, l in sorted(slovar_a.items(), reverse=True): #5
      print(i, l)


slovar_a['b'] = 222#6
print(slovar_a.values())#6
