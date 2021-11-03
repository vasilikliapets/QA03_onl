def count_letters(a):
    """Считает количество букв в строке и выводит числа за буквами"""
    count = 1  # Счетчик для букв
    result = [a[0]]  # Итоговый лист, куда падают пары БукваЧисло
    for i in range(0, len(a) - 1):
        if a[i] == a[i+1]:
            # если элемент равен следующему, то плюсуем в счетчик
            count += 1
        else:
            if count == 1:
                # Если элемент не равен, то не пишем единицу, докидываем букву, сбрасываем счетчик
                result.append(a[i + 1])
                count = 1
            else:
                # Докидываем количество букв, докидываем следующую букву, сбрасываем счетчик
                result.append(count)
                result.append(a[i+1])
                count = 1
    if count > 1:
        result.append(count)  # Докидываем число последней буквы
    result = ''.join(str(i) for i in result)  # из листа делаем строку без пробелов
    return print(result)


a = "ffffckk"
count_letters(a)

