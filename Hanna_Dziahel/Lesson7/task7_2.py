# Шифр Цезаря — один из древнейших шифров.
# При шифровании каждый символ заменяется другим, отстоящим от него
# в алфавите на фиксированное число позиций.
# Есть две функции - encode и decode,
# принимающие как параметры строку и число-сдвиг.
# Encode смещает значение вперед, Decode - назад.


# Импортируем модуль string, для дальнейшего вызова функции,
# в результате которой получим строку, содержащую символы алфавита
import string

# list(string.ascii_lowercase)
#ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


def encode(phrase, offset):
    """
    This function offsets letters forward to encode phrase
    :param phrase: str
    :param offset: int
    :return: encoded_phrase
    """
    encoded_phrase = ''
    encoded_element_index = 0

    # Создаем строку, содержащую значения алфавита, с помощью модуля string
    alphabet = string.ascii_lowercase

    # Узнаем длину alphabet для дальнейшего использования в сценариях,
    # когда буквы после смещения выходят за рамки значений в alphabet
    length = len(alphabet)

    for element in phrase:
        element_index = alphabet.index(element)
        if element_index == -1:
            encoded_phrase += element
        else:
            encoded_element_index = element_index + int(offset)

            # Если индекс зашифрованного элемента не в рамках alphabet,
            # присваиваем encoded_element_index значение, полученное
            # в результате обработки функцией change_index_to_correct
            if encoded_element_index >= length or encoded_element_index < 0:
                encoded_element_index = change_index_to_correct(
                    encoded_element_index, alphabet)

            # Записываем значения, полученные в результате шифрования
            encoded_phrase += alphabet[encoded_element_index]
    return encoded_phrase


def decode(phrase, offset):
    """
    This function offsets letters back to decode phrase
    :param phrase: str
    :param offset: int
    :return:
    """
    decoded_phrase = ''

    # Создаем строку, содержащую значения алфавита, с помощью модуля string
    alphabet = string.ascii_lowercase

    # Узнаем длину alphabet для дальнейшего использования в сценариях,
    # когда буквы после смещения выходят за рамки значений в alphabet
    length = len(alphabet)

    for element in phrase:
        element_index = alphabet.index(element)
        if element_index == -1:
            decoded_phrase += element
        else:
            decoded_element_index = element_index - int(offset)

            # Если индекс расшифрованного элемента не в рамках alphabet,
            # присваиваем decoded_element_index значение, полученное
            # в результате обработки функцией change_index_to_correct
            if decoded_element_index >= length or decoded_element_index < 0:
                decoded_element_index = change_index_to_correct(
                    decoded_element_index, alphabet)

                # Записываем значения, полученные в результате расшифровки
        decoded_phrase += alphabet[decoded_element_index]
    return decoded_phrase


def change_index_to_correct(changed_element_index, alphabet):
    """
    This function changes element index to index that is not out of range
    :param changed_element_index: int
    :param alphabet: str
    :return: changed_element_index
    """

    # Узнаем длину alphabet для дальнейшего использования в сценариях,
    # когда буквы после смещения выходят за рамки значений в alphabet
    length = len(alphabet)

    # В случае если индекс зашифрованной буквы выходит за пределы alphabet,
    # отнимаем от индекса зашифрованной буквы длину alphabet, что будет
    # аналогично прохождению alphabet с начала
    while changed_element_index >= length:
        changed_element_index -= length

    # В случае если индекс зашифрованной буквы меньше 0,
    # прибавляем к индексу зашифрованной буквы длину alphabet, что будет
    # аналогично прохождению alphabet с конца
    while changed_element_index < 0:
        changed_element_index += length
    return changed_element_index


def run_ceasar():
    """
    This function runs program Caesar cipher
    :return:
    """
    print("""Выберите операцию:
    1) Encode
    2) Decode""")
    user_action = int(input("Выбранная операция: "))
    user_phrase = input("Введите фразу: ")
    user_offset = int(input("Введите число-сдвиг для шифра: "))
    if user_action == 1:
        print(encode(user_phrase, user_offset))
    elif user_action == 2:
        print(decode(user_phrase, user_offset))


if __name__ == '__main__':
    run_ceasar()

