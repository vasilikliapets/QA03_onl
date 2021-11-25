# Реализуйте лямбда функцию, которая будет сортировать список по убыванию и
# возвращать его

my_list = [1, 3, 2, 5, 4]

lambda_func = lambda user_list: sorted(user_list, reverse=True)
lambda_result = lambda_func(my_list)

print(lambda_result)
