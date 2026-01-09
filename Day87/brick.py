from turtle import Turtle
import random

class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=5)  # height=40, width=100
        self.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        self.penup()
        self.goto(position)
