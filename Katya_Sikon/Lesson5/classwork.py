# Из заданной строки получить нужную строку:
# "String" => "SSttrriinngg"
# "Hello World" => "HHeelllloo  WWoorrlldd"
# "1234!_ " => "11223344!!__  "

str = (input('Введите строку: '))

for i in str:
    print(i * 2, end='')

# Если х в квадрате больше 1000 - пишем "Hot" иначе - "Nope"
# '50' == "Hot"
# 4 == "Nope"
# "12" == "Nope"
# 60 == "Hot"

x = float(input('\n\nВведите число: '))
if x**2 >= 1000:
    print('Hot')
else:
    print('Nope')

# Подсчет букв
# Дано строка и буква => "fizbbbuz","b", нужно подсчитать сколько раз буква b встречается в заданной строке 3
#
# "Hello there", "e" == 3
# "Hello there", "t" == 1
# "Hello there", "h" == 2
# "Hello there", "L" == 2
# "Hello there", " " == 1

str1 = input('\n\nВведите строку: ')
letter = input('Введите букву: ')

count_letter = 0
i = 0

while i < len(str1):
  if letter.lower() == str1[i].lower():
      count_letter = count_letter + 1
      i = i + 1
  else:
      i = i + 1

print('Количество букв', letter, 'в строке', str1, ':', count_letter)

# Напишите программу, которая по данному числу n от 1 до n выводит на экран n флагов.
# Изображение одного флага имеет размер 4×4 символов. Внутри каждого флага должен быть записан его номер — число от 1 до n.

n = int(input('\n\nВведите киличество флагов: '))

i = 0

while i < n:
    print('+__ ')
    print('|{i} /'.format(i=i+1))
    print('|__\ ')
    print('|   ')
    print("\n")
    i = i+1

# Напишите программу. Есть 2 переменные salary и bonus. Salary - integer, bonus - boolean.
# Если bonus - true, salary должна быть умножена на 10. Если false - нет

# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
# 2, True == '$20'
# 78, False == '$78'
# 67890, True == '$678900'

salary = int(input('\n\nВведите salary: '))
bonus = bool(int(input('Есть ли бонус? (Введите 0 или 1): ')))

if bonus == True:
    salary = salary * 10

print(salary)

# Суммирование. Необходимо подсчитать сумму всех чисел до заданного:
# дано число 2, результат будет -> 3(1+2)
# дано число 8, результат будет -> 36(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# 1 == 1
# 8 == 36
# 22 == 253
# 100 == 5050

n = int(input('\n\nВведите число: '))
sum = 0

for i in range(1, n+1):
    sum = sum + i
    i = i + 1

print('Сумма всех чисел до', n,': ',sum)