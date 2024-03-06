import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(random.randint(260,280))
        self.penup()

    def object_bounce(self):
        self.setheading(90 - self.heading() + 270)

    def ceil_bounce(self):
        self.setheading(-self.heading())
    def wall_bounce(self):
        self.setheading(270 - self.heading() + 270)