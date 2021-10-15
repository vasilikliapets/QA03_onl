# Есть переменные
a = 10
b = 25
sum_a_b = a + b
diff_a_b = a - b
# Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.'
# При решении задачи использовать оба способа форматирования
# Форматирование через метод format()
print("Summ is {sum} and diff = {diff}".format(sum=sum_a_b, diff=diff_a_b))
# Форматирование через метод f-strings
print(f"Summ is {sum_a_b} and diff = {diff_a_b}")

