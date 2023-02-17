"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

is_moving = True


def main():
    life = NUM_LIVES
    g = BreakoutGraphics()

    while True:
        if life >= 0:
            g.ball.move(g.vx, g.vy)
            g.touch_ball()
            if g.ball.x < 0 or g.ball.x + g.ball.width > g.window.width:
                g.vx = -g.vx
            if g.ball.y < 0:
                g.vy = -g.vy
            if g.ball.y + g.ball.height > g.window.height:
                g.ball.x = (g.window.width-g.ball.width)/2
                g.ball.y = (g.window.height-g.ball.height)/2
                #速度歸零停止，讓後台可以再給速度產生移動
                g.vx = 0
                g.vy = 0
                life -= 1
        else:
            break
        pause(FRAME_RATE)






if __name__ == '__main__':
    main()
