import time
from turtle import Screen
from player import Player
from blocks import BlockManager
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=500,height=700)
screen.tracer(0)
screen.title('Python Breakout Game')


player = Player()
blocks = BlockManager()
blocks.set_blocks()
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_right, 'Right')
screen.onkeypress(player.move_left, 'Left')
game = True
screen.update()
time.sleep(2)

def game_won():
    screen.clear()
    screen.bgcolor("black")
    scoreboard.win()
    return False
def game_lost():
    screen.clear()
    screen.bgcolor("black")
    scoreboard.lose()
    return False

while game:
    time.sleep(0.01)
    ball.forward(4)
    #collision with player
    if ball.distance(player) < 50 and abs(ball.ycor() - player.ycor()) < 10:
        ball.object_bounce()
        bounce_factor = ball.xcor() - player.xcor()
        ball.setheading(ball.heading() - bounce_factor)
    #collision with blocks
    for current_block in blocks.block_list:
        if current_block.distance(ball) < 25:
            ball.object_bounce()
            current_block.goto(1000,1000)
            scoreboard.update_scoreboard()
    #collision with walls
    if ball.xcor() > 245 or ball.xcor() < -245:
        ball.wall_bounce()
    # collision with ceil
    if ball.ycor() > 320:
        ball.ceil_bounce()
    if ball.ycor() < -370:
        game = game_lost()
    if scoreboard.blocks_destroyed == 80:
        game = game_won()
    screen.update()
screen.exitonclick()