# 3 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# Использование метода join() для сбора строк списка в одну строку с разделителем,
# который указан перед join
string = " ".join(list)
print(string)