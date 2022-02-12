from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.show_score()
    
    def show_score(self):
        self.write("Level: {}".format(self.level), align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.show_score()

