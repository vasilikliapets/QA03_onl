def calc(deposit: float, period: int):
    """
    Calculate deposit
    """
    rate = 10
    return round(deposit * (1 + rate / 100) ** period, 2)


def start():
    """
    Start program
    """
    print("""
-------------------
 Bank Deposit Calc
-------------------
""")
    deposit = float(input('Enter deposit, $: '))
    years = int(input('Enter term, years: '))
    result = calc(deposit, years)
    period = f"{years} years" if years > 1 else f"a year"
    return print(f"In {period} you will have: {result}$")


if __name__ == '__main__':
    start()
