def summation(first: float, second: float):
    """
    Summation action
    """
    return first + second


def subtraction(first: float, second: float):
    """
    Subtraction action
    """
    return first - second


def multiple(first: float, second: float):
    """
    Multiple action
    """
    return first * second


def divide(first: float, second: float):
    """
    Divide action
    """
    if second == 0:
        print('ERROR: Division by Zero')
    else:
        return first / second


ACTIONS = (summation, subtraction, multiple, divide)


def validate_action(action_str: str):
    """
    Validate action input
    """
    return action_str.isdigit() or action_str.lower() == 'h'


def calc_action(action_index: int):
    """
    Run calc action
    """
    if callable(ACTIONS[action_index]):
        first = float(input('Enter first number: '))
        second = float(input('Enter second number: '))
        return ACTIONS[action_index](first, second)
    else:
        print("ERROR: Wrong action")


def action(action_str: str):
    """
    Run calc
    """
    if action_str.isdigit() and 0 < int(action_str) <= len(ACTIONS):
        return calc_action(int(action_str) - 1)
    if action_str.lower() == 'h':
        return """
-------------------
     Calc v0.1
-------------------
Available actions:
1 - Summation
2 - Subtraction
3 - Multiple
4 - Divide
h - Help
x - Exit
-------------------
"""
