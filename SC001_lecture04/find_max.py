"""
File: find_max.py
Name:
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program print max')
    data = int(input('Data:'))
    if data == EXIT:
        print('no data')
    else:
        maximum = data
        while True:
            data = int(input('Data:'))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print('Max:'+str(maximum))






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
