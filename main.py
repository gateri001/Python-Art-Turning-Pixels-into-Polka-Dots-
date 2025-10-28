# import colorgram
#
#
# colors = colorgram.extract("image.jpg", 20)
#
# print(colors)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g , b)
#     color_list.append(new_colors)
# print(color_list)
import turtle
from turtle import Turtle, Screen
import random
art = Turtle()
color = turtle.colormode(255)
art.hideturtle()
x = -250
y = -250
art.teleport(x, y)
color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172)]

for column in range(10):
    for row in range(10):
        art.dot(20, random.choice(color_list))
        art.up()
        if row < 9:
            art.forward(50)
        art.pendown()
    y += 50
    art.teleport(x, y)



screen = Screen()
screen.exitonclick()