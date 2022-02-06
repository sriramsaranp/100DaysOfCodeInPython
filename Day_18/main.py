from turtle import Turtle, Screen 
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

colors = [ "red", "green", "blue", "orange", "purple", "yellow", "pink", "cyan", "magenta" ]

for i in range(3,11):
    for j in range (i):
        timmy.color(colors[random.randint(0,8)])
        timmy.forward(75)
        timmy.right(360/i)



screen = Screen()
screen.exitonclick()

