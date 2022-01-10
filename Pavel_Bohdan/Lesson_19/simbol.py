import string

def is_simbol(simbol):
    """
    Function for checking that input simbol is specsimbol
    """
    s = string.punctuation
    if len(simbol) == 1:
        for i in simbol:
            if i in s:
                return True
            else:
                return False
    else:
        return False

