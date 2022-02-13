from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

with open("data.txt", mode="r") as file:
    contents = file.read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = int(contents)
        self.scoreboard()
        self.high_scoreboard()
    
    def scoreboard(self):
        self.goto(-150,250)
        
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def high_scoreboard(self):
        self.goto(150,250)
        
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.scoreboard()
        self.high_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()
        self.high_scoreboard()
        
