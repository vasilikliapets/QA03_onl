import string


def check_special_character(character):
    """This function checks the argument is special character and returns true or false"""
    return character in list(string.punctuation)

