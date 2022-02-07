from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()
#w to move forwards
#s to move backwards
#a to rotate anti-clockwise
#d to rotate clockwise

def move_forwards():
    timmy.forward(50)
def move_backwards():
    timmy.backward(50)
def rotate_left():
    timmy.left(10) 
def rotate_right():
    timmy.right(10)
def clear():
    timmy.reset()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(clear, "q")
screen.exitonclick()

