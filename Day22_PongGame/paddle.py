from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.goto(x,y)
        
    def go_up(self):
        
        new_y = self.ycor()
        new_y += 20
        self.goto(350,new_y)
    
    def go_down(self):
        new_y = self.ycor()
        new_y -= 20
        self.goto(350,new_y)
        
