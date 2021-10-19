"""Задачи на закрепление форматирования:
Есть переменные a=10, b=25
Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.'
При решении задачи использовать оба способа форматирования"""
a = 10
b = 25
print(f"Summ is {a+b} and diff = {a-b}")
print("Summ is {0} and diff = {1}".format(a+b,a-b))

"""Есть список list_of_children = [“Sasha”, “Vasia”, “Nikalai”]
Вывести “First child is <первое имя из списка>, second is “<второе>”, and last one – “<третье>””"""
list_of_children = ["Sasha", "Vasia", "Nikalai"]
print(f"First child is {list_of_children[0]}, second is {list_of_children[1]}, and last one – {list_of_children[2]}")