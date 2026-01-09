from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)  # height 20, width 200
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 30
        if new_x > -300:  # left boundary (-400 + 100 half-width)
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 30
        if new_x < 300:  # right boundary (400 - 100 half-width)
            self.goto(new_x, self.ycor())
