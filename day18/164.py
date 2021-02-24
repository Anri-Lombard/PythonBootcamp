import turtle as t
import random

tul = t.Turtle()
tul.shape("turtle")
tul.color("sea green")
color = ["blue", "purple", "yellow", "orange", "cyan", "pink", "sea green", "gray", "black"]


def draw_shape(num_of_sides, length):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tul.fd(length)
        tul.lt(angle)


sides = 3
for _ in range(10):
    tul.color(random.choice(color))
    draw_shape(sides, 100)
    sides += 1

screen = t.Screen()
screen.exitonclick()
