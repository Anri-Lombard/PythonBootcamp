import turtle as t
import random

tim = t.Turtle()
directions = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)


screen = t.Screen()
tim.speed("fastest")
draw_spirograph(1)

screen.exitonclick()