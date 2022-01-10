

# Задание 2
# Непонятно, зачем функция от функции, если можно сразу брать sorted()
li = ["Andrei", "Veronika", "Kotik"]
result_2 = lambda user_list: sorted(user_list, reverse=True)
print(result_2(li))


# Задание 3
names = ["Andrei", "Veronika", "Kotik"]
result_3 = filter(lambda x: 't' in x, names)  # Проверяет есть ли в имени t
print(list(result_3))
