
# 2
def encode(letter, shift):
    """
    Функция кодирует фразу
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
  result = chr(code)
  return result

def decode(letter, shift):
    """
    Функция декодирует фразу
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

  letters_count = last_code - first_code - 1
  code = (ord(letter) - first_code - shift) % letters_count + first_code
  result = chr(code)
  return result

def choice_user():
    """
    Функция выбора действия кодировать/декодировать
    """
  while True:
    print("Выберите операцию:\n1.Кодировать:\n2.Декодировть:\n")
    choice = input("Введите номер пункта меню: \n")
    if choice not in ("1", "2"):
        print("Мимо, попробуй еще раз!")
        choice = input(f"Выберите операцию:\n1.Кодировать:\n2.Декодировть:\n")
    if choice == "1":
        message = input('Введите фразу: ')
        shift = int(input('Значение шифрования: '))
        for letter in message:
          print(encode(letter, shift))
    if choice == "2":
        message = input('Введите фразу: ')
        shift = int(input('Значение шифрования: '))
        for letter in message:
          print(decode(letter, shift))

choice_user()
