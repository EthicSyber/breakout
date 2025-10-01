from turtle import Turtle

SHAPE = 'circle'
COLOR = 'red'
SIZE = (0.8, 0.8)
START_POS = (0, -298)
BOUNDARIES = 350
X_OFFSET = 45
Y_OFFSET = 25

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(SIZE[0], SIZE[1])
        self.penup()
        self.goto(START_POS[0], START_POS[1])
        self.dx = 2
        self.dy = 2

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def cb_detection(self):
        """A collision boundary placed on the object to ensure it cannot exit the screen"""
        if self.xcor() > BOUNDARIES or self.xcor() < -BOUNDARIES-10:
            self.bounce_x()
        if self.ycor() > BOUNDARIES+5:
            self.bounce_y()
    
    def ob_collision(self):
        """A out of bounds collision placed on the object for applying a flag for ball in play"""
        if self.ycor() < -BOUNDARIES:
            return True
        else:
            return False

