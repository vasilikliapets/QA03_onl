school = {'1a': 15, '1b': 20, '2b': 21, '7a': 15, '9b': 10}

print(school['1a'])     # узнаем сколько учащихся 1a классе
school['1a'] = 25
school['1b'] = 15
school['2b'] = 17         # меняем колчество учащихся
school['8g'] = 14
school['10b'] = 18         # добавляем новый класс
del school['7a']        # удаляем класс
print(school)