import turtle

class Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        self.screen.title("Breakout")

        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def update_screen(self):
        self.screen.update()
