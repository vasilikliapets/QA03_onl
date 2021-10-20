# Напишите код, который возьмет список строк и пронумерует их
# [] => []
# ["a", "b", "c"] => ["1: a", "2: b", "3: c"]

list_3 = []
for idx, val in enumerate(list_3):
    list_3.append(f"{idx}: {val}")
print(list_3)

list_1 = []
list_2 = ["a", "b", "c"]
# Добавление индекса значения в списке через функцию enumerate()
# Выбор начального индекса через 2-й необязательный аргумент функции enumerate()
for idx, val in enumerate(list_2, 1):
    # Запись полученных значений в пустой список через append()
    list_1.append((f"{idx}: {val}"))
print(list_1)
