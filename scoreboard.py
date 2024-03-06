from turtle import Turtle
FONT = ("Courier", 16, 'normal')
END_FONT = ("Courier", 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks_destroyed = -1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,320)
        self.update_scoreboard()
    def score_up(self):
        self.blocks_destroyed +=1
    def update_scoreboard(self):
        self.clear()
        self.score_up()
        self.write(f'Score: {self.blocks_destroyed}', align='center', font=FONT)
    def win(self):
        self.goto(0,0)
        self.write(f'U won!', align='center', font=END_FONT)
    def lose(self):
        self.goto(0,0)
        self.write(f'You lost, {self.blocks_destroyed} blocks destroyed!', align='center', font=END_FONT)