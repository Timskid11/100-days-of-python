import turtle as t
import random  
timmy = t.Turtle()
t.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rc = (r,g,b) 
    return rc
    
timmy.shape("turtle")
direction =[0,90,180,270]

for _ in range(500):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.pensize(15)
    timmy.speed("fastest")
    














screen = t.Screen()
screen.exitonclick()