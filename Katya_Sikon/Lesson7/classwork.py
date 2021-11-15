# 1. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# [1, 5, 2, 4, 3]  #=> [5, 4]
# [1, 2, 3, 4, 5] #=> [2, 3, 4, 5]

spis = [1, 2, 3, 4, 5]
for i in range(1, len(spis)):
    if spis[i] > spis[i - 1]:
        print(spis[i])

# 2. Напишите программу, принимающую зубчатый массив любого типа и возвращающего его "плоскую" копию.

jagged_array = [[1, 2], [3, 4, [5, 6], 7], 8, [[9, [10], 11], 12], 13]


# flat_list = []

# for i in range(0, len(jagged_array)):
#    if type(jagged_array[i]) is list:
#        for j in range(0, len(jagged_array[i])):
#            flat_list.append(jagged_array[i][j])
#    else:
#        flat_list.append(jagged_array[i])


# print(flat_list)

# Result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def flatten(jagged_array):
    if not jagged_array:
        return jagged_array
    if isinstance(jagged_array[0], list):
        return flatten(jagged_array[0]) + flatten(jagged_array[1:])
    return jagged_array[:1] + flatten(jagged_array[1:])


print(flatten(jagged_array))


# 3. Напишите функцию, которая принимает на вход одномерный массив и два числа - размеры выходной матрицы.
# На выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.
# reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
# [
#    [1, 2, 3],
#    [4, 5, 6]
# ]
# reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
# [
#    [1, 2],
#    [3, 4],
#    [5, 6],
#    [7, 8]
# ]

def reshape(elements, rows, columns):
    matr = []
    j = 0
    for i in range(0, len(elements), columns):
        if j < rows:
            matr.append(elements[i:i + columns])
            j += 1
    return matr


print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3))


# 1) Напишите функцию-генератор, которая вычисляет числа фибоначчи

def fibonacci(num):
    f1 = 0
    f2 = 1
    i = 0
    if num == 1:
        print(f2)
    else:
        print(f1)
        while i < num:
            f_sum = f1 + f2
            f1 = f2
            f2 = f_sum
            i += 1
            yield f1


fib = fibonacci(11)
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


# 2) Напишите генератор списка который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6,
# 12.7] и возвращает новый список только с положительными числами


def only_positive(numbers):
    positive_numbers = []
    for i in numbers:
        if i > 0:
            positive_numbers.append(i)
    return positive_numbers


numbers = [34.6, -203.4, -44.9, 68.3, -12.2, 44.6, 12.7]

print(only_positive(numbers))

# 3) Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = "the quick brown fox jumps over the lazy dog", но только если слово не "the".

sentence = "the quick brown fox jumps over the lazy dog"


def count_letter(sentense):
    list_from_sentence = sentence.split(' ')
    word_length = []
    for i in list_from_sentence:
        if i != 'the':
            word_length.append(len(i))
    return word_length


print(count_letter(sentence))
