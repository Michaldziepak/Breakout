from turtle import Turtle
import time
DOWN=270
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("cyan")
        self.goto(0,0)
        self.shapesize(0.5,0.5)
        self.setheading(DOWN)
        self.brick_class=[]
        self.points=0
        self.breakout=False

    def bounce_paddle(self, paddle):
        if len(paddle.paddle_list)>3:
            if self.distance(paddle.paddle_list[0]) <= 25:
                self.setheading(135)
            elif self.distance(paddle.paddle_list[1]) <= 25:
                self.setheading(113)
            elif self.distance(paddle.paddle_list[2]) <= 25:
                self.setheading(90)
            elif self.distance(paddle.paddle_list[3]) <= 25:
                self.setheading(68)
            elif self.distance(paddle.paddle_list[4]) <= 25:
                self.setheading(45)
        if len(paddle.paddle_list)==3:
            if self.distance(paddle.paddle_list[0]) <= 25:
                self.setheading(135)
            elif self.distance(paddle.paddle_list[1]) <= 25:
                self.setheading(90)
            elif self.distance(paddle.paddle_list[2]) <= 25:
                self.setheading(45)

    def bounce_brick(self):

        for brick in self.brick_class.bricks_list:
            if self.distance(brick) <=20:
                self.setheading(-self.heading())
                # This line of code should resolve problem of bouncing through a lot of bricks and also ball will not go in between bricks and go to breakout
                if self.xcor()<83:
                    if self.heading() in range(-20,20):
                        self.forward(5)
                    else: self.forward(15)
                
                
                time.sleep(0.18)
                if brick.color()[0]=="yellow":
                    self.points+=1
                elif brick.color()[0] == "green":
                    self.points+=3
                elif brick.color()[0]=="orange":
                    self.points+=5
                elif brick.color()[0] == "red":
                    self.points += 10
                self.brick_class.bricks_list.remove(brick)
                brick.hideturtle()

    def bounce_wall(self):
      if self.xcor()>280 or self.xcor()<-280:
        if self.heading()<=180:
            self.setheading(180-self.heading())
        elif self.heading()>180:
            self.setheading((360-(self.heading()-180)))
        self.forward(10)
    def bounce_topwall(self):
        if self.ycor()>280:
            self.setheading(-self.heading())
            #Breakout
            self.breakout=True

            








