import turtle
from Archived.old_ball import Ball
from paddle import Paddle
from Archived.old_game import Collisions


def game_loop():
    screen.update()
    ball.move()
    collide.walls(obj=ball, right=360, top=350, left=-370)
    if paddle.distance(ball) < 20:
        paddle.bounce(ball)

    if ball.distance(wall) < 35:
        # Check for vertical collsion first:
        print(f"Collision Detected - ball xcor:{ball.xcor()} ball ycor:{ball.ycor()}")
        if abs(ball.xcor()- wall.xcor()) < 50:
            print("Vertical Bounce")
            # if the ball hits the top of the wall move it to the top edge
            if ball.ycor() > wall.xcor():
                ball.sety(wall.ycor() + 70)
            # if the ball hits the bottom of the wall, move it to the bottom edge
            else:
                ball.sety(wall.ycor() - 70)
            ball.bounce_y()
            
        # check for horizontal collision
        else:
            print("Horizontal Bounce")
            if ball.xcor() > wall.xcor():
                # if ball hits the right side of the wall
                ball.setx(wall.xcor() + 70)
            else:
                # if ball hits the left side of the wall
                ball.setx(wall.xcor() - 70)

            ball.bounce_x()
        wall.hideturtle()


        
    screen.ontimer(game_loop, 15)

# TODO: Start with the ball, work up to the wall, then start defining game features
# TODO: Set the Screen (Check)
screen = turtle.Screen()
screen.tracer(0)

collide = Collisions()
# TODO: Create the paddle object (Check)
# # TODO: Set the paddle at the bottom location for starting game (Check)
paddle = Paddle()

# TODO: Create the breakout game ball to shoot at the wall  (Check)
# TODO: Define movements for the paddle (Check)
# TODO: Define the movements for the ball (Check)
ball = Ball()

# TODO: Create Wall Objects [Multiple Rectangular Turtles, Different Colors, Side by Side at the Top]
##
# !!Code here!!!
wall = turtle.Turtle(shape='square')
wall.penup()
wall.goto(0, 300)
wall.shapesize(stretch_wid=1, stretch_len=5)






##
# !!Code here!!!
##

# TODO: Create some test events (Check)
screen.listen() # this is to listen for the event / e.g., key presses
screen.onkeypress(paddle.move_left, "a") # this is to handle the paddle moving left
screen.onkeypress(paddle.move_right, "d") # this is to hanlde the paddle moving right
# screen.onkeypress(move_ball, "space")

# TODO: Create events to listen for when the ball is moved (INCOMPLETE)
screen.onkeyrelease(fun=ball.move, key="space")


game_loop()
screen.mainloop()