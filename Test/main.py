from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)

# NEW STYLE BREAKOUT GAME
# TODO: LEVEL BACKGROUND DRAWING - LEVEL TITLE: THE JOB

## TODO: BACKGROUND IMAGE BANK

## TODO: BREAKOUT OBJECTS: A VAULT
test = Turtle()
test.hideturtle()
test.color('darkgray')
test.begin_fill()
test.forward(163)
test.left(145)
test.forward(200)
test.left(125)
test.forward(115)
test.end_fill()
# test.shape('triangle')


### * TODO: Turtle vault objects 
## TODO: BEHIND THE VAULT IS A GATE PROTECTING GOLD AND MONEY

# TODO: Create graphic character sheets for background design and character elements
# TODO: Test image
# TODO: Test graphics and pictures
screen.update()

screen.exitonclick()