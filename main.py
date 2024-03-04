from board import Board
from wall import Wall
from topwall import Topwall
from brick import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

NORMAL_SPEED=15

def check_death():
    global game_is_on
    if ball.ycor()<-280:
        if scoreboard.lives==1:
            scoreboard.lives-=1
            ball.breakout=False
            game_is_on = False
            gameover=Scoreboard()
            gameover.gameover()
            new_board.update_screen()
        else:
            scoreboard.lives-=1
            ball.breakout=False
            scoreboard.write_score()
            ball.goto(0,0)
            ball.setheading(270)
            for item in paddle.paddle_list:
                item.hideturtle()
                paddle.paddle_list=[]
            paddle.create_paddle()
            
def check_win():
    if bricks.bricks_list ==[]:
            win=Scoreboard()
            win.win()
            ball.hideturtle()
        
def breakout_paddle():
    #Shortens paddle when ball hits topwall
    if len(paddle.paddle_list)==5:
        paddle.paddle_list[0].hideturtle()
        paddle.paddle_list.pop(0)
        paddle.paddle_list[-1].hideturtle()
        paddle.paddle_list.pop(-1)
def bounce_everything(speed):
        check_death()
        check_win()
        ball.bounce_wall()
        ball.bounce_topwall()
        time.sleep(0.05)
        ball.forward(speed)
        scoreboard.update_score(ball.points)
        scoreboard.write_score()
        ball.bounce_paddle(paddle)
        ball.bounce_brick()
        
        new_board.update_screen()        
        
#Screen
new_board= Board()
screen = new_board.screen
screen.setup(width=600, height=600)
screen.listen()
#Walls
left_wall = Wall(length=55,gotopos=(-300,-255))
right_wall = Wall(length=55,gotopos=(293,-255))
top_wall = Topwall(length=90,gotopos=(-300,300))
#Create bricks
bricks = Brick()
bricks.create_bricks()
#Create Paddle,Scoreboard and ball
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
    # return paddle to normal state when shortened after brekout (in next life)
    if len(paddle.paddle_list) == 3:
        for item in paddle.paddle_list:
            item.hideturtle()
        paddle.paddle_list=[]
        paddle.create_paddle()
        
    bounce_everything(NORMAL_SPEED)
    while ball.breakout:
        bounce_everything(NORMAL_SPEED*1.5)
        breakout_paddle()    



screen.exitonclick()


