from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height = 400)
user_input = screen.textinput(title = "Make your bet",prompt = "Which color turtle do you bet on?")
#print(user_input)
colors = ["red","blue","green","yellow","orange","purple"]
turtles = []

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x = -240, y = -100 + i * 50)
    turtles.append(timmy)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if(winning_color == user_input):
                print("You have won the bet")
            else:
                print("You have lost the bet")
                print(f"The winning color was {winning_color}")
            is_race_on = False

        random_distane = random.randint(0,10)
        turtle.forward(random_distane)

        
screen.exitonclick()

