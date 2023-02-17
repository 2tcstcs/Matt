"""
File: 
Name:Matt
-------------------------
TODO:
"""
SIZE = 10
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(width=600, height=600, title='a')
poval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(oval)


def oval(mouse):
    poval.filled = True
    poval.fill_color = 'white'
    poval.color = 'black'
    window.add(poval, mouse.x-SIZE/2, mouse.y-SIZE/2)
    onmouseclicked(line)


def line(p):
    window.remove(poval)
    pline = GLine(poval.x-SIZE/2, poval.y-SIZE/2, p.x, p.y)
    window.add(pline)
    onmouseclicked(oval)


if __name__ == "__main__":
    main()
