from turtle import Turtle

LEFT = 180
RIGHT = 0
SPEED=15
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        self.shape("square")
        self.shapesize(0.3,0.6)
        
        self.paddle_list=[]

    def create_paddle(self):
        for j in range(-16,24,8):
            paddle=Paddle()
            paddle.color("white")
            paddle.goto(j,-260)
            self.paddle_list.append(paddle)
            
    def move_right(self):
        if self.paddle_list[-1].xcor()<260:
            for part in self.paddle_list:
                part.setheading(RIGHT)
                part.forward(SPEED)
    def move_left(self):
        if self.paddle_list[-1].xcor()>-250:
            for part in self.paddle_list:
                part.setheading(LEFT)
                part.forward(SPEED)


