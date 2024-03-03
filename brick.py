from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks_list = []
    def bricks_stack(self,color,pos):
        for i in range(-265, 280, 40):
            brick = Brick()
            brick.color(color)
            brick.penup()
            brick.shape("square")
            brick.shapesize(0.6, 1.80)
            brick.goto(i, pos)
            self.bricks_list.append(brick)

    def create_bricks(self):
        for j in range(180,200,16):
            self.bricks_stack("red",j)
        for j in range(148,180,16):
            self.bricks_stack("orange", j)
        for j in range(116,148,16):
            self.bricks_stack("green", j)
        for j in range(83,115,16):
            self.bricks_stack("yellow", j)
