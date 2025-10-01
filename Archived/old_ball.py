from turtle import Turtle, ontimer

DEFAULT_SHAPE = 'circle'


# TODO: Once completed in main, create Ball object Here

class Ball(Turtle):
    def __init__(self, color:str='#000000', size:tuple[float, float]=(0.8, 0.8), start_pos:tuple[int, int]=(0, -280)):
        super().__init__()
        self.penup()
        self.shape(DEFAULT_SHAPE)
        self.shapesize(size[0], size[1])
        self.color(color)
        self.goto(start_pos)
        self.x_move = 5
        self.y_move = 5

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto((x_cor, y_cor))

    def bounce_x(self):
        self.x_move *= -1
       

    def bounce_y(self):
        self.y_move *= -1
       


