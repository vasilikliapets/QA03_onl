# Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't',
# и отфильтруйте список имен с помощью функции filter

my_list = ["Tolik", "Anya", "Katya", "Alex"]

result = filter(lambda name: 't' in name, my_list)
print(list(result))