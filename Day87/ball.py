from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.03  # sleep time, smaller = faster

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # Optional: gradually speed up horizontally
        # self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 3  # reset horizontal speed
        self.y_move = 3  # reset vertical speed
        # Optional: flip horizontal direction randomly
        # self.x_move *= -1
