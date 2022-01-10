import random

import bank.deposit as bank_deposit
import encrypt.caesar as encrypt_caesar

ACTIONS = (bank_deposit.start, encrypt_caesar.start)


def start(program: int):
    """
    Start programs
    """
    if len(ACTIONS) >= program and callable(ACTIONS[program - 1]):
        ACTIONS[program - 1]()
        return True
    return False


attempts = 4

while bool(attempts):
    print("""
-------------------
     Programs
-------------------
Available actions:
1 - Bank Deposit Calc
2 - Caesar Cipher
3 - Exit
-------------------
""")
    action = input('Enter action: ')
    if action.isdigit():
        if start(int(action)):
            if input('Do you want to start another program, [y/n]: ').lower().startswith('y'):
                continue
            else:
                break
        elif int(action) == 3:
            print('Exited')
            break
    print("""
ERROR!
You must select an action from the available
""")
    attempts -= 1
else:
    random_action = random.randint(1, 2)
    print('Random program started:', random_action)
    start(random_action)
