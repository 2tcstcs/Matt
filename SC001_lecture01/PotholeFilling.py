"""
File: PotholeFilling.py
Name: Ｍatt
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def turn_right():
    """
    pre-condition:karel左轉三次
    post-condition:
    """
    for i in range(3):
        turn_left()


def put99():
    for i in range(99):
        put_beeper()


def go_in():
    move()
    turn_right()
    move()


def go_out():
    turn_right()
    turn_right()
    move()
    turn_right()


def work():
    go_in()
    put99()
    go_out()
    move()

def work3():
    for ii in range(3):
        work()


def main():
    work3()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
