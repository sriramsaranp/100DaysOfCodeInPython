from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    #segments = []
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for i in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.shape("square")
            timmy.penup()
            timmy.goto(-20*i, 0)
            self.segments.append(timmy)
    
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN :
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != RIGHT :
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT :
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() != UP :
            self.segments[0].setheading(270)
        
        

        
