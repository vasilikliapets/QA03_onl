#  1. Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

s1 = 'Robin Singh'
s2 = 'I love arrays they are my favorite'

s1_1 = s1.split()
s2_1 = s2.split()

print('\nпервая строка\n', s1, '\nмассив из первой строки\n', s1_1)
print('\nвторая строка\n', s2, '\nмассив из второй строки\n', s2_1)