# Есть переменные a=10, b=25
# Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.'
# При решении задачи использовать оба способа форматирования

a = 10
b = 25
print('Summ is {summ} and diff = {diff}.'.format(summ=a+b, diff=b-a))

summ = a + b
diff = b - a
print(f'Summ is {summ} and diff = {diff}.')

# Есть список list_of_children = [“Sasha”, “Vasia”, “Nikalai”]
# Вывести “First child is <первое имя из списка>, second is “<второе>”, and last one – “<третье>””

list_of_children = ['Sasha', 'Vasia', 'Nikalai']
print('First child is ',list_of_children[0],' second is ',list_of_children[1],', and last one – ',list_of_children[2])
