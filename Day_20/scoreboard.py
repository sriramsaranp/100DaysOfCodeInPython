from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.scoreboard()
    
    def scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()
