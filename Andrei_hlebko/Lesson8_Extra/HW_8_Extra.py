#Task 1



#TASK 2 -Реализуйте лямбда функцию, которая будет сортировать список по убыванию и возвращать его
spisok_task2 = lambda x: sorted(x)[::-1]
print(spisok_task2([1,7,5,4,3,267,6]))


#TASK 3 - Реализуйте лямбда функцию, которая проверяет есть ли в слове буква 't', и отфильтруйте список имен
                                                                                    #с помощью функции filter

names = ["Andry","Veronika","Katya","Sasha","Masha","Maxim","Konstantin"]
result = filter(lambda x: 't' in x, names)
print(list(result))


