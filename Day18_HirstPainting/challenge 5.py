import turtle as t
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
timmy.speed("fastest")
def all(angle):
    
    for eachcircle in range(int(360/angle)):
        timmy.color(random_colour())   
        timmy.circle(100)
        timmy.left(angle)
    
angle = 5
all(angle)