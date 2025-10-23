import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.add_cars = []
        self.move_speed = MOVE_INCREMENT
    def create_new_car(self):
        chance = random.randint(1,6)
        if chance == 1:            
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))    
            new_car.speed(self.move_speed)  
            new_car.goto(300,random.randint(-250,250))
            self.add_cars.append(new_car)
    def move(self):
        for eachcar in self.add_cars:
            eachcar.backward(self.move_speed)
    def speed_increase(self):
        self.move_speed += 10
