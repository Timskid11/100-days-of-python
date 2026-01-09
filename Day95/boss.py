from turtle import Turtle
import random

COLORS = ["red", "orange", "purple", "blue"]
MOVE_DISTANCE = 2  # slow downward movement

class Enemy(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(position)
        self.setheading(270)

    def move(self):
        self.forward(MOVE_DISTANCE)
