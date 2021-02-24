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


screen = t.Screen()
tim.speed("fastest")
tim.pensize(7)

for _ in range(1000):
    tim.color(random_color())
    tim.forward(15)
    tim.setheading(random.choice(directions))

screen.exitonclick()
