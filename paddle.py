from turtle import Turtle

LEFT = 180
RIGHT = 0
SPEED=15
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_list=[]

    def create_paddle(self):
        for j in range(-16,24,8):
            paddle=Paddle()
            paddle.color("white")
            paddle.penup()
            paddle.shape("square")
            paddle.shapesize(0.3,0.6)
            paddle.goto(j,-260)
            self.paddle_list.append(paddle)
    def move_right(self):
        for part in self.paddle_list:
            part.setheading(RIGHT)
            part.forward(SPEED)
    def move_left(self):
        for part in self.paddle_list:
            part.setheading(LEFT)
            part.forward(SPEED)


