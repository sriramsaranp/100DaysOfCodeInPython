from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self,pos):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.screen.tracer(0)
        self.goto(pos)
        self.screen.update()
        self.speed(0)
        

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        self.screen.update()
    
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        self.screen.update()   