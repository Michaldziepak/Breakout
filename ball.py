from turtle import Turtle
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

    def bounce_paddle(self, paddle):
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

    def bounce_brick(self,brick_class):
        for brick in brick_class.bricks_list:
            if self.distance(brick) <=25:
                self.setheading(-self.heading())
                # if self.heading() in range(-20,20):
                #     self.forward(5)
                # else: self.forward(15)
                brick_class.bricks_list.remove(brick)
                brick.hideturtle()

    def bounce_wall(self):
        #This version calculates exact angle but lags and I created simpler version
      if self.xcor()>280 or self.xcor()<-280:
        if self.heading()<=180:
            self.setheading(180-self.heading())
        if self.heading()>180:
            self.setheading((360-(self.heading()-180)))







