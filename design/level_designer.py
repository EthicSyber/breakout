from pattern_designer import *
from pallete import *

class LevelDesign(PatternDesign):
    def __init__(self):
        super().__init__()
        self.walls = []

    def stage_one(self, level=1):
        if level == 1:
            self.walls += self.block_pattern(color=RED_PALLETE)
        elif level == 2:
            self.walls += self.block_pattern(color=BLUE_PALLETE)
        elif level == 3:
            self.walls += self.block_pattern(color=GREEN_PALLETE)
    
    def stage_one_bonus(self):
        self.walls += self.double_block_pattern(pallete1=YELLOW_GOLD_PALLETE, pallete2=GREEN_PALLETE)
        self.walls += self.gate_pattern()

    def stage_two(self, level=5):
        if level == 5:
            self.walls += self.double_block_pattern(pallete1=BLUE_PALLETE, pallete2=RED_PALLETE)
            self.walls += self.gate_pattern()
        elif level == 6:
            self.walls += self.double_block_pattern(pallete1=GRAY_PALLETE, pallete2=GREEN_PALLETE)
            self.walls += self.gate_pattern()
    
    def test_level_design(self):
        self.walls += self.brick_wall()
        
    def stage_two_bonus(self):
        pass

    def stage_three(self):
        pass

    def stage_three_bonus(self):
        pass

 
# TODO: After doing a couple diamond level designs. Create a Class for Level Design to handle levels

    # def level_one(self) -> None:
    #     """Level One Design layout uses single color block pattern across screen"""
    #     self.block_design(
    #         min_x=MIN_X,
    #         max_x=MAX_X,
    #         min_y=MIN_Y,
    #         max_y=MAX_Y,
    #         color=COLORS["blue"],
    #         shape=SQUARE,
    #     )

    # def level_two(self) -> None:
    #     """Level Two Design layout uses block pattern with two colors on left and right side of screen"""
    #     for idx in range(2):
    #         self.block_design(
    #             min_x=MIN_X+self.xmin_offset,
    #             max_x=self.xmax_offset,
    #             min_y=MIN_Y,
    #             max_y=MAX_Y,
    #             color=self.color_keys[idx],
    #             shape=SQUARE
    #         )
    #         self.xmin_offset+=360
    #         self.xmax_offset+=340