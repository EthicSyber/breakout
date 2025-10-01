from turtle import Turtle

# TODO: Once Completed in main, Create paddle object here

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto((0, -300))

    def move_left(self):
        """Moves the paddles position to the left"""
        self.back(30)

    def move_right(self):
        """Moves the paddle position to the right"""
        self.forward(30)

    def bounce(self, obj):
        if abs(obj.xcor() - self.xcor()) < 50:
             obj.sety(obj.ycor() + 25)
             obj.bounce_y()
        else:
            obj.setx(obj.xcor() + 50 if obj.xcor() > self.xcor() else self.xcor() - 50)
            obj.bounce_x()