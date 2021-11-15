import decorators


@decorators.duration_decorator
@decorators.name_decorator
def fibonacci(n: int):
    """

    """
    a = b = 1
    n = n - 2
    while n > 0:
        a, b = b, a + b
        n -= 1
    return b


@decorators.increment_decorator
@decorators.before_and_after_decorator
def math_expression():
    """

    """
    return 7 * (12 ** (2 + 1) // (4 - 1)) / ((2 + 4) * 2) - (3 * 110 + 6)


@decorators.reverse_decorator
def args_list(*args):
    """

    """
    return args


@decorators.uppercase_decorator
def text_uppercase(text: str):
    """

    """
    return text


print("""
--------------------
    Run Function
--------------------
1 - Fibonacci
2 - Math Expression
3 - Reversed Args
4 - Uppercase
5 - Exit
--------------------
""")

action = input('Select action: ')

if action.isdigit() and 1 <= int(action) <= 5:
    action = int(action)
    if action == 1:
        print(fibonacci(10))
    elif action == 2:
        print(math_expression())
    elif action == 3:
        print(args_list(1, 2, 3, 4, 5))
    elif action == 4:
        print(text_uppercase('To uppercase'))
    elif action == 5:
        print('Exited')
else:
    print('ERROR: You must select an action from the available')
