from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 # starting lives/score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.game_over_flag = False
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase(self):
        if self.game_over_flag:
            return
        self.score += 1
        self.update_score()

    def decrease(self):
        if self.game_over_flag:
            return False

        # Only decrease if score > 0
        if self.score > 0:
            self.score -= 1
            self.update_score()

        # Trigger game over when score reaches 0
        if self.score == 0:
            self.game_over()
            self.game_over_flag = True
            return True

        return False

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
