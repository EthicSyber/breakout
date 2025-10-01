from turtle import Turtle


############################
##### BLOCK - DESIGNER #####
############################

# TODO: Create Shape Style for Block Design Pattern (COMPLETE)
# # TODO: Create value constants for Block Designer (COMPLETE)
# # TODO: Create Wall | Block Size (COMPLETE)
SQUARE = "square"
WALL_BLOCK_SIZE = (1, 4)
MIN_X = -320
MAX_X = 340
PADX = 90
MIN_Y = 200
MAX_Y = 360
PADY = 25

############################
##### DIAMOND - DESIGN #####
############################
# TODO: Create Diamond Block Size (COMPLETE)
# # TODO: Create a mapping for diamond design (COMPLETE)
DIAMOND_BLOCK_SIZE = (0.8, 2.0)
DIAMOND_MAP = {
    'outer':[(0, 332.0), (-43.0, 315.0), (43.0, 315.0), (-86, 300.0), (86, 300.0), (-43.0, 283.0), (43.0, 283.0), (0, 266.0)],
    'inner':[(-43, 300),(0, 315), (43, 300), (0, 283)],
    'center':[(0, 300)]
}


# TODO: Once Level Design Class is created Ch
class PatternDesign:
    """Pattern Designer for the various levels in the breakout style game"""
    def __init__(self):
        pass

    def block_pattern(self, min_x:int=MIN_X, max_x:int=MAX_X, padx:int=PADX, min_y:int=MIN_Y, max_y:int=MAX_Y, pady:int=PADY, shape_size:tuple=WALL_BLOCK_SIZE, color:str|list[str]='#0069ff') -> list:
        """Block design layout for a pattern of blocks
        
        :params min_x: min value to set walls to the left of the screen
        :params max_x: max value to set walls to the right of the screen
        :params min_y: min value to set walls to the middle of the screen
        :params max_y: max value to set walls to the top of the screen
        :params pad_x: spacing on the horizontal plane between walls
        :params pad_y: spacing on the vertical plane between walls
        :params color: color(s) of blocks
        """
        blocks = []
        for x in range(min_x, max_x, padx):
            for y in range(min_y, max_y, pady):
                wall = Turtle()
                wall.speed(0)
                wall.shape(SQUARE)
                wall.penup()
                wall.goto(x, y)
                wall.shapesize(shape_size[0], shape_size[1])
                blocks.append(wall)
        
        if type(color) == list:
            self.set_pallete(block_list=blocks, pallete=color)
        else:
            self.set_block_color(block_list=blocks, color=color)     
        return blocks

    def diamond_pattern(self, diamond_map:dict, color:list[str], x_offset:int=0, y_offset:int=0) -> list:
        """Creates a diamond design pattern and places it top center of the screen
        
        :params dict diamond_map: tuple values that place each block on an xy coordinate 
        :params list color: value(s) for single or variation of colors (i.e., color pallete)
        :params int x_offset: the value to place the diamond toward the left or right
        :params int y_offset: the value to place the diamond toward the top or bottom

        Example:
        >>> diamond_map = {
            'outer':[(0, 332.0), (-43.0, 315.0), (43.0, 315.0), (-86, 300.0), (86, 300.0), (-43.0, 283.0), 
            (43.0, 283.0), (0, 266.0)],
            'inner':[(-43, 300),(0, 315), (43, 300), (0, 283)],
            'center':[(0, 300)]
            }
        >>> diamond_colors = ["#ececfb","#dfe0fb", "#e4e0ff"]
        >>> diamond_design(diamond_map=diamond_map, color=diamond_colors)
        """

        blocks = []
        for i in range(3):
            key = list(diamond_map.keys())[i]
            for pos in diamond_map[key]:
                wall = Turtle(SQUARE)
                wall.shapesize(DIAMOND_BLOCK_SIZE[0], DIAMOND_BLOCK_SIZE[1])
                # wall.color(color)
                wall.speed(0)
                wall.penup()
                wall.goto(pos[0] + x_offset, pos[1] + y_offset)
                blocks.append(wall)

        self.set_pallete(block_list=blocks, pallete=color)
        return blocks

    def gate_pattern(self):
        gate = []
        # vertical bars
        gate += self.block_pattern(color='gray',shape_size=(3, 0.8), padx=56)
        # horizontal top bars
        gate += self.block_pattern(color='gray', shape_size=(0.8, 5), max_y=370, min_y=360)
        # horizontal bottom bars
        gate += self.block_pattern(color='gray', shape_size=(0.8, 5), max_y=180, min_y=160)
        return gate

    def double_block_pattern(self, pallete1, pallete2):
        walls = []
        walls += self.block_pattern(max_x=0, color=pallete1)
        walls += self.block_pattern(min_x=40, color=pallete2)
        return walls

    def set_block_color(self, block_list:list, color:str):
        """Method sets the block color for multiple blocks."""
        for wall in block_list[:]:
            wall.color(color)

    def set_pallete(self, block_list:list, pallete:list):
            """Method sets the color pallete for the blocks."""
            position = 0
            for wall in block_list[:]:
                wall.color(pallete[position % len(pallete)])
                position+=1
            
    def brick_wall(self, xcor=(-350, 0, 50), ycor=(100, 350, 15), color=("#c0c0c0", "#AD3E3E"), shape_size=(0.8, 2.5)):
        """Creates a brick wall look with the turtle blocks on the screen
        
        :params tuple xcor: the xcor value is set for start, end, spacing on the horziontal plane
        :params tuple ycor: the ycor value is set for start, end, spacing on the vertical plane
        :params tuple color: the border color is the first value, the fill color is the second value
        :params tuple shape_size: two values set for width and length of the brick

        """
        bricks = []
        for x in range(xcor[0], xcor[1], xcor[2]):
            for y in range(ycor[0], ycor[1], ycor[2]):
                t = Turtle()
                t.speed(0)
                t.color(color[0], color[1])
                t.shape("square")
                t.shapesize(shape_size[0], shape_size[1])
                t.penup()
                t.goto(x, y)
                bricks.append(t)
                
        return bricks        
    
    def test_method(self):
        """A test method used to create a new design prior to implementing it"""
        pass

    # Design Patterns Below - TODO: Think about level creation next

    # def create_diamonds(self,  x_start_pos:int=0, x_offset:int=0, total_diamonds:int=3, colors:list=DIAMOND_COLORS, diamond_mapping:dict=DIAMOND_MAP) -> None:
    #     """Creates multiple diamonds using the create diamond design pattern"""
    #     offset = x_start_pos
    #     for total in range(total_diamonds):
    #         for i in range(3):
    #             color = colors[i]
    #             key = list(diamond_mapping.keys())[i]
    #             self.diamond_design(
    #                 diamond_map=diamond_mapping[key], 
    #                 color=color, 
    #                 x_offset=offset
    #             )
    #         offset += x_offset  

