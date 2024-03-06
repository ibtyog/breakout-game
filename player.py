from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(1,3)
        self.penup()
        self.goto(0,-330)
    def move_right(self):
        self.goto(self.position()[0] + 25, -330)
    def move_left(self):
        self.goto(self.position()[0] - 25, -330)