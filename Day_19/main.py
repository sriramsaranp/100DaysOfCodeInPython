from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(50)

screen.listen()
screen.onkey(move_forwards, "m")
screen.exitonclick()

