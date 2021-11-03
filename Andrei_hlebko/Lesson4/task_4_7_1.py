#Есть переменные a=10, b=25
# Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.
#При решении задачи использовать оба способа форматирования


a,b = 10, 25
print(f"Summ is {a+b} and diff = {abs(a-b)}")
print("Summ is {} and diff = {}.".format(a+b, abs(a-b)))
