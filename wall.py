from turtle import Turtle

class Wall(Turtle):
    def __init__(self,length,gotopos):
        super().__init__()
        self.length = length
        self.gotopos = gotopos
        self.create_wall()

    def create_wall(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(self.length,1)
        self.goto(self.gotopos)