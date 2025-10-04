import turtle
from paddle import Paddle
from ball import Ball
from design.level_designer import LevelDesign
import time

#############  ##############
######  GAME SETTINGS  ######
#############  ##############
DISTANCE_CHECK = 30
SPACEBAR = 'space'
A_KEY = 'a'
D_KEY = 'd'
background_color = "#1D1C1C"

### GAME FLAGS ###
game_on = True
follow = True
rate = 0.009
level = 1
# GAME FUNCTIONS
def game_start():
    global game_on, follow
    game_on = True
    follow = False

def is_ball_and_paddle_collided(ball, paddle):
    # if the ball is reversed (i.e., coming downward) | ball is in vertical collision
    if ball.ycor() < paddle.ycor() + 20 and ball.dy < 0:
        # ball x coor in horizontal 
        if (ball.xcor() < paddle.xcor() + 30 and ball.xcor() > paddle.xcor() - 30):
            ball.sety(paddle.ycor() + 20)
            ball.bounce_y()

screen = turtle.Screen()
screen.bgcolor(background_color)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
breakout = LevelDesign()
breakout.stage_one(level=level)

# TODO: Test Level Design Layouts with Pallete Colors (Complete)


# EVENT LISTENERS
screen.listen()
screen.onkeypress(paddle.move_left, A_KEY)
screen.onkeypress(paddle.move_right, D_KEY)
screen.onkeypress(game_start, SPACEBAR)

while game_on:
    screen.update()

    ball.move()
    ball.cb_detection()
    

    paddle.cb_detection()
    is_ball_and_paddle_collided(ball, paddle)

    for vault_obj in breakout.walls[:]:
        if ball.distance(vault_obj) < 30:
            # change direction
            ball.bounce_y()
            # hide block
            vault_obj.hideturtle()
            # remove the block from the list
            breakout.walls.remove(vault_obj)

            if rate <= 0.0001:
                rate = 0.0001
            else:
                rate -= 0.0001
    
    if len(breakout.walls) == 0 and level <= 3:
        level += 1
        breakout.stage_one(level=level)
    else:
        game_over = True
    
    game_over = ball.ob_collision()
    if game_over:
        game_on = False

    time.sleep(rate)






# CHECK FOR UPDATES IN GAME SEQUENCE
# game_update()

# GAME SCREEN DISPLAY 
screen.exitonclick()