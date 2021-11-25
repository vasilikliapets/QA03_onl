# 2. Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"

def counter(user_str):
    user_str = user_str + ' '
    str_new = ''
    i = 0
    while i < len(user_str) - 1:
        if user_str[i] == user_str[i + 1]:
            str_new = str_new + user_str[i]
            j = i
            for j in range(i, len(user_str)):
                if user_str[j] != user_str[j + 1]:
                    break
            str_new = str_new + str(user_str.count(user_str[i], i, j + 1))
            i = j + 1
        else:
            str_new = str_new + user_str[i]
            i += 1
    return str_new


user_str = str(input('Введите строку: '))
print(counter(user_str))
