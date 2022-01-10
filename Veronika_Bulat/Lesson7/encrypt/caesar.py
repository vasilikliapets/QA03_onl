from string import ascii_lowercase as lowercase, \
    ascii_uppercase as uppercase, \
    ascii_letters as letters, \
    punctuation


def encrypt(text: str, offset: int):
    """
    Encrypt function
    """
    alphabet_offset = offset % len(lowercase)
    punctuation_offset = offset % len(punctuation)
    displaced = \
        lowercase[alphabet_offset:] + lowercase[:alphabet_offset] \
        + uppercase[alphabet_offset:] + uppercase[:alphabet_offset] \
        + punctuation[punctuation_offset:] + punctuation[:punctuation_offset]
    translation = str.maketrans(letters + punctuation, displaced)
    return text.translate(translation)


def encode(text: str, offset: int):
    """
    Encode Caesar Cipher
    """
    return encrypt(text, offset)


def decode(text: str, offset: int):
    """
    Decode Caesar Cipher
    """
    return encrypt(text, -offset)


def start():
    """
    Start program
    """
    print("""
-------------------
   Caesar Cipher
-------------------
Available actions:
1 - Encode
2 - Decode
3 - Exit
-------------------
""")
    action = int(input('Enter action: '))

    if 1 <= action < 3:
        text = str(input('Enter text: '))
        offset = int(input('Enter offset: '))
        if action == 1:
            print('Encoded:', encode(text, int(offset)))
        elif action == 2:
            print('Decoded:', decode(text, int(offset)))
    elif action == 3:
        print('Exited')
    else:
        print("""
ERROR!
You must select an action from the available
""")
        start()


if __name__ == '__main__':
    start()
