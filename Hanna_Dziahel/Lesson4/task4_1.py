# 1 - Перевести строку в массив
#"Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

string_1 = "Robin Singh"
string_2 = "I love arrays they are my favorite"
# Использование метода split() для перевода строки в список (list)
list_1 = string_1.split()
list_2 = string_2.split()
print(list_1)
print(list_2)
