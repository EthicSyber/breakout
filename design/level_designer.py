from design.pattern_designer import *
from design.pallete import *
from Test.main import vault

class LevelDesign(PatternDesign):
    def __init__(self):
        super().__init__()
        self.walls = []

    def stage_one(self, level=1):
        if level == 1:
            self.walls += vault()
        elif level == 2:
            self.walls += self.double_block_pattern(pallete1=YELLOW_GOLD_PALLETE, pallete2=GREEN_PALLETE)
            self.walls += self.gate_pattern()
        elif level == 3:
            self.walls += self.double_block_pattern(pallete1=BLUE_PALLETE, pallete2=RED_PALLETE)
    
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