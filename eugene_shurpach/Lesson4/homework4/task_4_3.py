"""1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число"""
list_1 = [1, 5, 2, 9, 2, 9, 1]
import collections
count_qua = collections.Counter(list_1) # считаем количество каждого значения
print(min(count_qua, key=count_qua.get))

"""2) Дан текст, который содержит различные английские буквы и знаки препинания. 
Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре."""
text = "Giowdu iefhiwue. UGbibiuiygyuboniehfoieh kefh"
text_2 = text.lower()
list = list(text_2)
count_letter = collections.Counter(list)
print(max(count_letter, key=count_letter.get))
