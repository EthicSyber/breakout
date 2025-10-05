import turtle
from assets.player.paddle import Paddle
from assets.player.ball import Ball
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


# GAME FUNCTIONS
def game_start():
    global game_on, follow
    game_on = True
    follow = False

def bp_collision(ball, paddle):
    # if the ball is reversed (i.e., coming downward) | ball is in vertical collision
    if ball.ycor() < paddle.ycor() + 20 and ball.dy < 0:
        # ball x coor in horizontal 
        if (ball.xcor() < paddle.xcor() + 30 and ball.xcor() > paddle.xcor() - 30):
            ball.sety(paddle.ycor() + 20)
            ball.bounce_y()

# TODO: Test Level Design Layouts with Pallete Colors (Complete)


def breakout():
    global follow
    # GAME FLAGS
    game_on = True
    follow = True

    # CURRENT LEVEL
    level = 1

    # GAME SPEED
    rate = 0.009

    # SCREEN
    screen = turtle.Screen()
    screen.bgcolor(background_color)
    screen.tracer(0)

    paddle = Paddle()
    ball = Ball()
    stages = LevelDesign()
    stages.stage_one(level=level)

    # EVENTS
    screen.listen()
    screen.onkeypress(paddle.move_left, A_KEY)
    screen.onkeypress(paddle.move_right, D_KEY)
    screen.onkeypress(game_start, SPACEBAR)

    while game_on:
        screen.update()

        if follow:
            x = paddle.xcor()
            y = ball.ycor()
            ball.goto(x, y)
        else:
            ball.move()
    

        ball.cb_detection()
        

        paddle.cb_detection()
        bp_collision(ball, paddle)

        for vault_obj in stages.walls[:]:
            if ball.distance(vault_obj) < 30:
                # change direction
                ball.bounce_y()
                # hide block
                vault_obj.hideturtle()
                # remove the block from the list
                stages.walls.remove(vault_obj)

                if rate <= 0.0001:
                    rate = 0.0001
                else:
                    rate -= 0.0001
        
        if len(stages.walls) == 0 and level <= 3:
            level += 1
            stages.stage_one(level=level)
        else:
            game_over = True
        
        game_over = ball.ob_collision()
        if game_over:
            game_on = False

        time.sleep(rate)

    screen.exitonclick()