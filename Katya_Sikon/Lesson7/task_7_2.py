# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
#
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
#
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Все взаимодействие с программой должно производиться через терминал!
#
# Пример:
# Выберите операцию:
# 1) Encode
# 2) Decode
#
# 2
# Введите фразу:
#
# И так далее!

alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()


def encode(language, message, step):
    """
    Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
    отстоящим от него в алфавите на фиксированное число позиций.

    :param language: язык фразы для шифрования
    :param message: фраза для шифрования
    :param step: шаг шифрования
    :return: зашифрованная фраза
    """
    encode_message = ''
    if language.upper() == 'RU':
        for i in message.lower():
            letter = alphabet_RU.find(i)
            new_letter = letter + step
            if i in alphabet_RU:
                encode_message += alphabet_RU[new_letter]
            else:
                encode_message += i
    elif language.upper() == 'EN':
        for i in message.lower():
            letter = alphabet_EN.find(i)
            new_letter = letter + step
            if i in alphabet_EN:
                encode_message += alphabet_EN[new_letter]
            else:
                encode_message += i
    return encode_message


def decode(language, message, step):
    """
    Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
    отстоящим от него в алфавите на фиксированное число позиций.

    :param language: язык зашифрованной фразы
    :param message: зашифрованная фраза
    :param num: шаг шифрования
    :return: расшифрованая фраза
    """
    decode_message = ''
    if language.upper() == 'RU':
        for i in message.lower():
            letter = alphabet_RU.find(i)
            new_letter = letter - step
            if i in alphabet_RU:
                decode_message += alphabet_RU[new_letter]
            else:
                decode_message += i
    elif language.upper() == 'EN':
        for i in message.lower():
            letter = alphabet_EN.find(i)
            new_letter = letter - step
            if i in alphabet_EN:
                decode_message += alphabet_EN[new_letter]
            else:
                decode_message += i
    return decode_message


def caesar_shift():
    operation = int(input('Выберите операцию:\n1) Зашифровать сообщение\n2) Расшифровать сообщение\n'))
    if operation == 1:
        language = input('Выберите язык: введите RU или EN\n')
        message = input('Введите сообщение для шифровки: ')
        step = int(input('Введите шаг шифровки: '))
        print('Зашиврованное сообщение:', encode(language, message, step))
    elif operation == 2:
        language = input('Выберите язык: введите RU или EN\n')
        message = input('Введите сообщение для дешифровки: ')
        step = int(input('Введите шаг шифровки: '))
        print('Расшиврованное сообщение:', decode(language, message, step))
    else:
        print('\nВведите номер выбранной операции из предложенных!')

caesar_shift()