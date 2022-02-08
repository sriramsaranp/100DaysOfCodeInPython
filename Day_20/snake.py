from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    #segments = []
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self,position):
        timmy = Turtle()
        timmy.color("white")
        timmy.shape("square")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN :
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
        
        

        
