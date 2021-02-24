from turtle import Turtle
import random

HEIGHT = 600
WIDTH = 600
HALF_WIDTH = int(WIDTH / 2) - 20
HALF_HEIGHT = int(HEIGHT / 2) - 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-HALF_WIDTH, HALF_WIDTH)
        random_y = random.randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.goto(random_x, random_y)
