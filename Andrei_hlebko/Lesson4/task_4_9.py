#Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую
# частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a".
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
from collections import Counter


text1 = "The page object pattern intends to create an object for each part of a web page." \
        "This technique helps build a separation between the test code and the actual code " \
        "that interacts with the web page."

a = Counter(text1).most_common(2)
print(a[1])


