# В данной подстроке проверить все ли буквы в строчном регистре или нет
# и вернуть список не подходящих

# Проверка через функцию isupper(), что буквы находятся в верхнем регистре
string_1 = 'dogcat'
if string_1.lower() in string_1:
 a = [i for i in string_1 if i.isupper()]
 print(True, a)
else:
 a = [i for i in string_1 if i.isupper()]
 print(False, a)

 string_2 = 'doGCat'
 if string_2.lower() in string_2:
  a = [i for i in string_2 if i.isupper()]
  print(True, a)
 else:
  a = [i for i in string_2 if i.isupper()]
  print(False, a)


