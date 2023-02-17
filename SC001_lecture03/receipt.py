"""
File: receipt.py
Name:
-------------------------
This program calculates the meal cost
and prints the result on Console.
Students will learn variables, user inputs,
and concatenation
"""


def main():
    meal = int(input('How much was your meal?'))
    tax=float(input('Tax:'))
    total=meal*(1+tax)
    print('Total:'+str(total)+'!')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
