from board import Board
from wall import Wall
from topwall import Topwall
from brick import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

NORMAL_SPEED=15
new_board= Board()

screen = new_board.screen
screen.setup(width=600, height=600)
screen.listen()
left_wall = Wall(length=55,gotopos=(-300,-255))
right_wall = Wall(length=55,gotopos=(288,-255))
top_wall = Topwall(length=90,gotopos=(-300,300))
bricks = Brick()
bricks.create_bricks()
paddle=Paddle()
scoreboard= Scoreboard()

paddle.create_paddle()
ball = Ball()
ball.brick_class=bricks
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
new_board.update_screen()
game_is_on=True
while game_is_on:
    ball.bounce_wall()
    time.sleep(0.05)
    ball.bounce_paddle(paddle)

    ball.forward(NORMAL_SPEED)
    ball.bounce_brick()
    scoreboard.update_score(ball.points)
    scoreboard.write_score()
    new_board.update_screen()




screen.exitonclick()


