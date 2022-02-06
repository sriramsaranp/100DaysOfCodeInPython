# import colorgram

# rgb_colors = []
# colors = colorgram.extract('img.jpg',40)

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(200)

timmy.setheading(0)

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190), (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]
for i in range(10):
    timmy.penup()
    timmy.goto(-200,-200 + i*50)
    timmy.pendown()
    for j in range(10):
        timmy.speed(0)
        timmy.dot(20,random.choice(color_list))
        timmy.penup()   
        timmy.forward(50)
        timmy.pendown()
    

my_screen = Screen()
my_screen.exitonclick()