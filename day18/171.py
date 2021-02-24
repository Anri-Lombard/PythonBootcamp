# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Hirstspotpainting-1.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

import turtle as t
import random

tess = t.Turtle()
tess.penup()
t.colormode(255)

color_list = [(144, 76, 49), (188, 164, 120), (166, 153, 35), (14, 45, 83), (45, 110, 137), (142, 185, 175), (146, 55, 82), (59, 120, 100), (141, 169, 177), (86, 35, 29), (63, 152, 169), (219, 210, 94), (112, 37, 30), (101, 145, 111), (166, 98, 129), (94, 121, 170), (169, 144, 162), (178, 103, 83), (206, 183, 195), (50, 52, 90), (71, 38, 55), (93, 44, 63), (172, 201, 193), (172, 201, 204), (14, 101, 81), (4, 98, 119)]


def draw_10_dots():
    for _ in range(10):
        tess.dot(20, random.choice(color_list))
        tess.fd(50)


def turn_left():
    tess.lt(90)
    tess.fd(50)
    tess.lt(90)
    tess.fd(50)


def turn_right():
    tess.rt(90)
    tess.fd(50)
    tess.rt(90)
    tess.fd(50)


tess.hideturtle()
tess.speed("fastest")
tess.setheading(225)
tess.fd(300)
tess.setheading(0)
line = 1
for _ in range(10):
    draw_10_dots()
    if line % 2 == 0:
        turn_right()
    else:
        turn_left()
    line += 1

screen = t.Screen()
screen.exitonclick()
