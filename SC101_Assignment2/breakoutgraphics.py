"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height - paddle_offset)

        # Width of the paddle (in pixels)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2,ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.vx = 0
        self.vy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)

        # Draw bricks
        xx = 0
        yy = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=xx, y=brick_offset+yy)
                self.brick.fill_color = 'blue'
                yy += self.brick.height + brick_spacing
            yy = 0
            xx += self.brick.width + brick_spacing

    def touch_ball(self):
        object_a = self.window.get_object_at(self.ball.x, self.ball.y)
        object_b = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        object_c = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        object_d = self.window.get_object_at(self.ball.x+ self.ball.width, self.ball.y + self.ball.width)

        if object_a is not None and object_a is not self.paddle:
            self.vy = -self.vy
            self.window.remove(object_a)
        elif object_b is not None and object_b is not self.paddle:
            self.vy = -self.vy
            self.window.remove(object_b)
        elif object_c is not None and object_c is not self.paddle:
            self.vy = -self.vy
            self.window.remove(object_c)
        elif object_d is not None and object_d is not self.paddle:
            self.vy = -self.vy
            self.window.remove(object_d)

        if object_a is self.paddle:
            self.vy = -self.vy
        elif object_b is self.paddle:
            self.vy = -self.vy
        elif object_c is self.paddle:
            self.vy = -self.vy
        elif object_d is self.paddle:
            self.vy = -self.vy

    def move_ball(self, mouse):
        self.vx = random.randint(1, MAX_X_SPEED)
        self.vy = INITIAL_Y_SPEED


    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
