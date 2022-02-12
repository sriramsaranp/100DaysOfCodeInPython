import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
   
    car_manager.create_car()
    car_manager.move_car()


    # Check if the player has collided with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            player.game_over()

    # Check if the player has reached the finish line
    if player.ycor() == 280:
        scoreboard.update_level()
        player.next_level()
        car_manager.increase_speed()
        





    
    

screen.exitonclick()