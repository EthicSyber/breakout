# TODO: Once completed in main, create game functionality here



class Collisions:

    def walls(cls, obj, top:int, left:int, right:int):
        if obj.xcor() > right or obj.xcor() < left:
            obj.bounce_x()
        if obj.ycor() > top:
            obj.bounce_y()