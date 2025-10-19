from turtle import Turtle, Screen   

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue","green")
timmy.speed(2)
for each in range(20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
        