import random
def summa(a, b):
    """Считает сумму"""
    return print(a + b)


def diff(a, b):
    """Считает разность"""
    return print(a - b)


print(random.choice((summa, diff))(4, 4))