from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time
from scoreboard import Scoreboard
import winsound
import random


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BreakOut")
screen.tracer(0)
round_number = 1

paddle = Paddle((0, -250))  # paddle near bottom
ball = Ball()
scoreboard = Scoreboard()

bricks = []

rows = 5
columns = 8
brick_width = 100
brick_height = 40
x_gap = 5
y_gap = 5
start_x = -350
start_y = 250

for row in range(rows):
    for col in range(columns):
        x = start_x + col * (brick_width + x_gap)
        y = start_y - row * (brick_height + y_gap)
        brick = Brick((x, y))
        bricks.append(brick)

def new_level():
    global round_number
    rows =  random.randint(5,9)
    columns = random.randint(4,8)
    brick_width =  random.randint(100,200)
    brick_height =  random.randint(40,50)
    x_gap = 5
    y_gap = 5
    start_x = -350
    start_y = 250
    for row in range(rows):
        for col in range(columns):
            x = start_x + col * (brick_width + x_gap)
            y = start_y - row * (brick_height + y_gap)
            brick = Brick((x, y))
            bricks.append(brick)


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.ycor() < -290:  # bottom
        ball.reset_position()

        game_is_on = False

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()


    paddle_top = paddle.ycor() + 10
    paddle_bottom = paddle.ycor() - 10
    paddle_left = paddle.xcor() - 100
    paddle_right = paddle.xcor() + 100

    if ball.y_move < 0 and (paddle_bottom <= ball.ycor() <= paddle_top) and (paddle_left <= ball.xcor() <= paddle_right):
        ball.bounce_y()



    for brick in bricks:
        if (ball.xcor() > brick.xcor() - 40 and
            ball.xcor() < brick.xcor() + 40 and
            ball.ycor() > brick.ycor() - 15 and
            ball.ycor() < brick.ycor() + 15):
            ball.bounce_y()
            brick.hideturtle()
            scoreboard.increase_score()
            bricks.remove(brick)

    if len(bricks) == 0:
        round_number += 1
        ball.reset_position()  # put ball back in center
        ball.move_speed *= 0.9  # speed up ball for next round
        breakout = new_level()


screen.exitonclick()
