from turtle import Turtle

DOWN = 270
UP = 90


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.up()
        self.down()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        self.seth(UP)
        self.fd(20)

    def down(self):
        self.seth(DOWN)
        self.fd(20)
