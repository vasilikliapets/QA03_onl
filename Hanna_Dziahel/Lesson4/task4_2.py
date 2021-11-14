# 2 - Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
list_1 = ["Ivan", "Ivanou"]
string_1 = "Minsk"
string_2 = "Belarus"
# Использование метода join() для сбора строк списка в одну строку с разделителем,
# который указан перед join
print("Привет, " + ' '.join(
    list_1) + "! Добро пожаловать в " + string_1 + " " + string_2)

