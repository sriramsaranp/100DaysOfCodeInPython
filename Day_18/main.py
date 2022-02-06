from turtle import Turtle, Screen 
import random
import turtle

timmy = Turtle()
#timmy.shape("turtle")
timmy.color("blue")

turtle.colormode(255)

def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) 


dirs = [0,90,180,270]

def movement(dir):
    timmy.speed("fastest")
    timmy.pensize(5)
    timmy.color(get_color())
    timmy.forward(30)
    timmy.setheading(dir)

screen = Screen()
for _ in range(100):
    direction = random.choice(dirs)
    movement(direction)

screen.exitonclick()



