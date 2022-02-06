from turtle import Turtle, Screen, tiltangle 
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

tilt_angle = 5
for i in range(round(360/tilt_angle)):
    timmy.speed(0)
    timmy.pen(pencolor=get_color())
    timmy.circle(100)
    timmy.left(tilt_angle)
    


screen = Screen()

screen.exitonclick()



