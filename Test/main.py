import turtle 


#################################
###### -----------------  #######
####### VAULT DIMENSIONS ########
###### ------------------ #######
#################################

# SHAPES
TRIANGLE = "triangle"
SQUARE = "square"
CIRCLE = 'circle'

# * VAULT OUTER SHAPE - CORNERS
VOS = (0, 5, 5, 2.9) # handles shape sizing for left bottom and right top; negate last value for flipping the object left to right
# * VAULT OUTER SHAPE CORNER COORDINATES
vos_coordinates = [(150.0, 320.0), (-150.0, 120.0), (-150.0, 320.0), (150.0, 120.0)]

# * VAULT OUTER SHAPE - PANELS
# ** VAULT OUTER SHAPE - PANEL - Vertical
vopv = (11.5, 3.5)
# ** VAULT OUTER SHAPE - Panel - Horizontal
voph = (17.3, 3.5)
vos_panel_coordinates = [(-138.0, 229), (138.0, 229), (0, 130), (0, 310)]

# * VAULT DOOR SHAPE 
VDOOR_BFRAME_COLOR = "#dedede"
VDOOR_FRAME_COLOR = "#908989"
# ** VDOOR COORDINATES
# > 1st-tuple = base-frame, 2nd-tuple =
vdoor_coordinates = [(0, 215), (0, 216), (0, 214)]
# ** VDOOR BASE-FRAME
vdoor_bfs = (13.3, 13.3)
vdoor_fs = (12, 12)
vdoor_fps = (10.5, 10.5)

# KEY HOLE 
keyhole_coordinates = [(0, 190), (0, 215)]


# screen = turtle.Screen()
# screen.bgcolor('black')
# screen.tracer(0)


# def click_xy(x, y):
#     print(x, y)

# vault_frame = []

# NEW STYLE BREAKOUT GAME
# TODO: LEVEL BACKGROUND DRAWING - LEVEL TITLE: THE JOB

def vault_wall():
    """Creates a wall of panels behind the vault"""
    parts = []
    for x in range(-300, 320, 200):
        for y in range(100, 380, 40):
            panel = turtle.Turtle()
            panel.penup()
            panel.color("#B8B4B4", "#817f7f")
            panel.begin_fill
            panel.shape(SQUARE)
            panel.shapesize(2, 10)
            panel.end_fill()
            panel.goto(x, y)
            parts.append(panel)
    return parts

def outer_corners():
    """Creates the outer corners behind the outer panels of the vault"""

    parts = []
    for idx in range(len(vos_coordinates)):
        x, y = vos_coordinates[idx]
        corner = turtle.Turtle()
        corner.shape(TRIANGLE)
        corner.color("#c2c2c2")
        corner.penup()
        if idx < 2:
            corner.shapetransform(VOS[0], VOS[1], VOS[2], VOS[3])
            corner.goto(x, y)
        else:
            corner.shapetransform(VOS[0], VOS[1], VOS[2], -VOS[3])
            corner.goto(x, y)
        
        if idx == 1 or idx == 3:
            corner.left(180)
        parts.append(corner)
    
    return parts

def outer_panels():
    """Creates the outer panels for the vault"""

    parts = []
    for idx in range(len(vos_panel_coordinates)):
        x, y = vos_panel_coordinates[idx]
        panel = turtle.Turtle()
        panel.shape(SQUARE)
        panel.penup()
        panel.color("#A9A0A0")

        if idx < 2: 
            panel.shapesize(stretch_wid=vopv[0], stretch_len=vopv[1])
            panel.goto(x, y)
        else:
            panel.shapesize(stretch_wid=voph[0], stretch_len=voph[1])
            panel.goto(x, y)
            panel.left(90)
        
        parts.append(panel)
    
    return parts

def vault_door():
    """Creates The Vault Door"""
    parts = []
    # VDOOR Base-Frame 
    base_frame = turtle.Turtle()
    base_frame.shape(CIRCLE)
    base_frame.color(VDOOR_BFRAME_COLOR)
    base_frame.penup()
    base_frame.shapesize(vdoor_bfs[0],vdoor_bfs[1])
    base_frame.goto(vdoor_coordinates[0][0], vdoor_coordinates[0][1])
    parts.append(base_frame)
    
    center_frame = turtle.Turtle()
    center_frame.shape(CIRCLE)
    center_frame.color(VDOOR_FRAME_COLOR)
    center_frame.penup()
    center_frame.shapesize(vdoor_fs[0], vdoor_fs[1])
    center_frame.goto(vdoor_coordinates[1][0], vdoor_coordinates[1][1])
    parts.append(center_frame)

    top_frame = turtle.Turtle()
    top_frame.shape(CIRCLE)
    top_frame.color(VDOOR_BFRAME_COLOR)
    top_frame .penup()
    top_frame.shapesize(vdoor_fps[0], vdoor_fps[1])
    top_frame.goto(vdoor_coordinates[2][0], vdoor_coordinates[2][1])
    parts.append(top_frame)

    keyhole_bottom = turtle.Turtle()
    keyhole_bottom.color("#6e5f5f")
    keyhole_bottom.penup()
    keyhole_bottom.shape('arrow')
    keyhole_bottom.shapesize(1, 3)
    keyhole_bottom.left(90)
    keyhole_bottom.goto(keyhole_coordinates[0][0], keyhole_coordinates[0][1])
    parts.append(keyhole_bottom)

    keyring_top = turtle.Turtle()
    keyring_top.color("#6e5f5f")
    keyring_top.shape(CIRCLE)
    keyring_top.penup()
    keyring_top.goto(keyhole_coordinates[1][0], keyhole_coordinates[1][1])
    parts.append(keyring_top)

    return parts

def vault():
    frame = []
    frame += vault_wall()
    frame += outer_corners()
    frame += outer_panels()
    frame += vault_door()
    return frame

# TODO: DISPLAY VAULT
# vault()

## TODO: BACKGROUND IMAGE BANK

# screen.listen()
# screen.onclick(click_xy)





## TODO: BREAKOUT OBJECTS: A VAULT
## creates a 90 deg triangle
# test = Turtle()
# test.hideturtle()
# test.color('darkgray')
# test.begin_fill()
# test.forward(163)
# test.left(145)
# test.forward(200)
# test.left(125)
# test.forward(115)
# test.end_fill()
# # test.shape('triangle')


### * TODO: Turtle vault objects 
## TODO: BEHIND THE VAULT IS A GATE PROTECTING GOLD AND MONEY

# TODO: Create graphic character sheets for background design and character elements
# TODO: Test image
# TODO: Test graphics and pictures
# screen.update()

# screen.mainloop()