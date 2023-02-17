"""
File: 
Name:Matt
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect,GArc,GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    這個是我小時候的地鼠，一起成為神奇寶貝大師吧～
    """
    window = GWindow(width=600, height=600, title='a')
    head =GOval(300,300,x=150, y= 50)
    head.filled = True
    head.fill_color = 'peru'  # 填色
    head.color = 'peru'  # 外框
    window.add(head)

    head2 = GRect(300, 300, x=150, y=200)
    head2.filled = True
    head2.fill_color = 'peru'  # 填色
    head2.color = 'peru'  # 外框
    window.add(head2)

    le = GOval(50,80,x=200, y=150)
    le.filled = True
    le.fill_color = 'black'  # 填色
    le.color = 'black'  # 外框
    window.add(le)

    lew = GOval(20, 30, x=200, y=150)
    lew.filled = True
    lew.fill_color = 'white'  # 填色
    lew.color = 'white'  # 外框
    window.add(lew)

    re = GOval(50, 80, x=300, y=150)
    re.filled = True
    re.fill_color = 'black'  # 填色
    re.color = 'black'  # 外框
    window.add(re)

    rew = GOval(20, 30, x=300, y=150)
    rew.filled = True
    rew.fill_color = 'white'  # 填色
    rew.color = 'white'  # 外框
    window.add(rew)

    mouth = GOval(100,50,x=230,y=270)
    mouth.filled = True
    mouth.fill_color = 'salmon'  # 填色
    mouth.color = 'salmon'  # 外框
    window.add(mouth)




if __name__ == '__main__':
    main()
