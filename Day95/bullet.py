from turtle import Turtle

MOVE_DISTANCE = 20

class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
