from string import punctuation  # импорт спецсимволов


def check_punctuation(symbol):
    list_of_punctuation = list(punctuation)
    if symbol in list_of_punctuation:  # проверка на вхожесть символа в лист со спецсимволами
        return True
    else:
        return False
