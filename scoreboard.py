from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives =3
        self.color("white")
        self.goto(-100, 250)
        self.write_score()
        self.penup()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Player score: {self.score}     {'❤'*self.lives}", move=False, font=('Arial', 12, 'normal'))
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=('Arial', 12, 'normal'))
    def win(self):
        self.clear()
        self.goto(0,0)
        self.write(f"YOU WIN", align="center", font=('Arial', 12, 'normal'))

    def update_score(self,score):
        self.score=score
    def lose_life(self):
        self.lives -= 1