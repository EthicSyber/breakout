from turtle import Turtle

# PADDLE CONSTANTS
START_POS = (0, -320)
MOVE = 30
SHAPE = 'square'
SIZE = (0.8, 4)
COLOR = "#FFFFFF"
XOFFSET = 20
BOUNDARIES = 380
BOUNDARY_OFFSET = 25
OBJ_BOUNDARY = 350


class Paddle(Turtle):
    """Paddle object to deflect the ball"""
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(SIZE[0], SIZE[1])
        self.color(COLOR)
        self.penup()
        self.goto(START_POS[0], START_POS[1])

    def move_left(self):
        """Move the paddle to the left of the screen"""
        self.setx(self.xcor() - MOVE)
    
    def move_right(self):
        """Move the paddle to the right of the screen"""
        self.setx(self.xcor() + MOVE)
    
    def cb_detection(self):
        """A collision boundary placed on the object to ensure it cannot exit the screen"""
        if self.xcor() < -BOUNDARIES + BOUNDARY_OFFSET:
            self.setx(self.xcor() + XOFFSET)
        if self.xcor() > BOUNDARIES - BOUNDARY_OFFSET:
            self.setx(self.xcor() - XOFFSET)
    
    def hold(self, obj):
        if self.xcor() < OBJ_BOUNDARY:
            obj.setx(self.xcor())
        if self.xcor() > -OBJ_BOUNDARY:
            obj.setx(self.xcor())
 