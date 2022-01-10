# 2
def encode(letter, shift):
  """
  Функция кодирует и декодирует фразу
  :param letter: фраза
  :param shift: значение шифрования
  :return: кодированая и декодированная фразы
  """
  first_code = None
  last_code = None

  if ord('a') <= ord(letter) <= ord('z'):
    first_code = ord('a')
    last_code = ord('z')
  elif ord('A') <= ord(letter) <= ord('Z'):
    first_code = ord('A')
    last_code = ord('Z')
  else:
    return letter

  letters_count = last_code - first_code + 1
  code = (ord(letter) - first_code + shift) % letters_count + first_code
  res1 = chr(code)

  letters_count_2 = last_code - first_code - 1
  code_2 = (ord(res1) - first_code - shift) % letters_count_2 + first_code
  res2 = chr(code_2)
  return res1, res2


message = input('Введите фразу: ')
shift = int(input('Значение шифрования: '))
for letter in message:
  res1, res2 = encode(letter, shift)
  print(res1, res2)
