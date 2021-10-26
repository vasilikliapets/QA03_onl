# Из заданной строки получить нужную строку:
# "String" => "SSttrriinngg"
# "Hello World" => "HHeelllloo  WWoorrlldd"
# "1234!_ " => "11223344!!__  "

a = 'String'
for i in a:
    print(i * 2, end='')

# Если х в квадрате больше 1000 - пишем "Hot" иначе - "Nope"
# '50' == "Hot"
# 4 == "Nope"
# "12" == "Nope"
# 60 == "Hot"

x = 4
if x ** 2 > 1000:
    print('\n Hot')
else:
    print('\n Nope')

# Подсчет букв
# Дано строка и буква => "fizbbbuz","b", нужно подсчитать сколько раз буква b встречается в заданной строке 3
# "Hello there", "e" == 3
# "Hello there", "t" == 1
# "Hello there", "h" == 2
# "Hello there", "L" == 2
# "Hello there", " " ==
word = 'Hello there'
letter = 'L'
count = 0
i = 0
while i < len(word):
    if letter.lower() == word[i].lower():
        count = count + 1
        i = i + 1
    else:
        i = i + 1
print('Буква', letter, 'встречается', count, 'раз')

# Напишите программу. Есть 2 переменные salary и bonus. Salary - integer, bonus - boolean.
# Если bonus - true, salary должна быть умножена на 10. Если false - нет
# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
# 2, True == '$20'
# 78, False == '$78'
# 67890, True == '$678900'

bonus = bool(1)
salary = 10000

if bonus == True:
    salary = salary * 10
    print('Зарплата:', salary)
else:
    print('Зарплата:', salary)

# Суммирование. Необходимо подсчитать сумму всех чисел до заданного:
# дано число 2, результат будет -> 3(1+2)
# дано число 8, результат будет -> 36(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
# 1 == 1
# 8 == 36
# 22 == 253
# 100 == 5050

n = 100
sum = 0
for i in range(n+1):
    sum = sum + i
    i = i+1
print(sum)
