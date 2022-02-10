from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Score
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()


my_screen.listen()
my_screen.onkey(r_paddle.move_up, "Up")
my_screen.onkey(r_paddle.move_down, "Down")
my_screen.onkey(l_paddle.move_up, "w")
my_screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move_ball()

    #Detect collision between paddle 
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        # ball.setx(320)

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        # ball.setx(-320)

    #Detect collision with wall on left and right
    if ball.xcor() > 380:
        ball.reset_position()
        score.increment_l_score()
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.increment_r_score()
        #
    

        




my_screen.exitonclick()



