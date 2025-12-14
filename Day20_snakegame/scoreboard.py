from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):  
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
     
        self.clear()
    def update_scoreboard():
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
    def increase_score():
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
         self.goto(0,0)
         self.write(f"GAME OVER", move=False, align='center', font=('Arial', 8, 'normal'))