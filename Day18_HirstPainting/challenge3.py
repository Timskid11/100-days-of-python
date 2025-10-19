from turtle import Turtle,Screen
import random

tim = Turtle()
colors = ["red","yellow","blue","orange","purple","green","black","brown"]

def draw(number):
#triangle
  
        
    for eachshape in range(number):
         angle = int(360/number)
         tim.forward(100)
         tim.right(angle)
         

for shape_side_n in range(3,101):
   
   choice = random.choice(colors)
   tim.color(choice)
   draw(shape_side_n)
   
   
   
   







screen = Screen()
screen.exitonclick()