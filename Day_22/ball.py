from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.score = 0
        self.dx = 2
        self.dy = 2
        self.screen.tracer(0)
        self.speed(0)
        self.move_speed = 0.01

    
    def move_ball(self):
        self.bounce_y()
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        self.screen.update()

    def bounce_y(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1
    
    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.dx *= -1
        
    
        