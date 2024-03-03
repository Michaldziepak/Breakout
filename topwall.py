from turtle import Turtle

class Topwall(Turtle):
    def __init__(self,length,gotopos):
        super().__init__()
        self.length = length
        self.gotopos = gotopos
        self.create_wall()
    def create_wall(self):
        self.setheading(90)
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(self.length,1)
        self.goto(self.gotopos)
