import turtle as t
tim = t.Turtle
t.color("blue","red")
t.shape("turtle")
def forward():
     tim.forward(10)
def backward():
     tim.backward(10)
def left():
     tim.left(10)
     tim.forward(10)
def right():
     tim.right(10)
     tim.forward(10)
def reset():
    tim.reset()
screen = t.Screen()
screen.listen()
screen.onkey(forward,"w")
screen.onkey( backward,"s")
screen.onkey( left,"a" )
screen.onkey(right,"d")
screen.onkey(reset,"c")
screen.exitonclick()