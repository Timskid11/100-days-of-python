from turtle import Screen,Turtle
import random
screen = Screen()
screen.setup(width = 1000, height = 400)
not_playing = False
userbet = screen.textinput(title = "Make your bet",prompt = "Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]
y_coordinate = [-70,-20,30,80,130,180,240]
all_turtles = []
for x in range(0,6):
    tim = Turtle(shape ="turtle")
    tim.penup()
    tim.pencolor(colors[x])
    tim.goto(x = -500,y = y_coordinate[x])
    all_turtles.append(tim)

if userbet:
    not_playing = True
while not_playing:
   for eachturtle in all_turtles:
        
        if eachturtle.xcor() > 500:
            not_playing = False
            winner_color = eachturtle.pencolor()
            if winner_color == userbet:
                print(f"You won!!,  The {winner_color} turtle is the winner")
            else:
                print(f"You lose!!,  The {winner_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        eachturtle.forward(rand_distance)
                
screen.exitonclick()