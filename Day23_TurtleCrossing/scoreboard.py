from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 1
        self.penup()
        self.hideturtle()    
        self.goto(-280,200)  
        self.update_scoreboard()                
    def game_over(self):
         self.write("GAME OVER","center",FONT)         
    def update_scoreboard(self):
        self.write(f"Level: {self.score}",align = "left",font= FONT) 
    def increase_level(self):   
             self.score += 1  
             self.update_scoreboard()
        
        