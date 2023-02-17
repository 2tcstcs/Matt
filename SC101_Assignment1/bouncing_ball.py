"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


DELAY = 50
GRAVITY = 5
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
VX = 5
window = GWindow(800, 500, title='bouncing_ball.py')



oval = GOval(SIZE, SIZE)
oval.filled = True
window.add(oval, START_X, START_Y)
count = 0
def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(ball)


def ball(event):
    t = 0
    global count
    if oval.x == START_X and count < 3:
        while True:
            oval.move(VX, t)
            t += 2*GRAVITY
            # 碰底反彈
            if oval.y+oval.height >= window.height:
                t = -t * REDUCE
            if oval.x+oval.width >= window.width:
                oval.x = START_X
                oval.y = START_Y
                break
            pause(DELAY)
        count += 1


if __name__ == "__main__":
    main()
