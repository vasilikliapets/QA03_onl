# Ваша задача написать программу, принимающее число - номер кредитной карты(число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
# validate(4561261212345464)  # => False
# validate(4561261212345467)  # => True

def validate(kart_numb):
    """
    This Function check credict card validate
    """

    if len(str(kart_numb)) < 15 or not str(kart_numb).isdigit():
        return False
    else:
        kart_numb = str(kart_numb)
        c = [int(x) for x in kart_numb[::-2]]  # в с заходит лист со значениями с конца через 1
        u2 = [(2 * int(y)) // 10 + (2 * int(y)) % 10 for y in kart_numb[-2::-2]]  # проходимся по цифрам в
                                                                        # перевернутом списке начиная со 2-го и через 1
        return sum(c + u2) % 10 == 0  # Результат суммы без остатка делится на 10, тогда True


print(validate(4561261212345464))
print(validate(4561261212345467))
