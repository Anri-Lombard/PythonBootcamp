import turtle
import random
# I added randint.
from random import randint


# Let's define a class so we can create turtles
class MyTurtle():

    # Here's the constructor. Where we give some initial values.
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(self.color)
        self.turtle.speed(1)
        self.turtle.pd()

    # We need to know if this turtle is off the board.
    def off_board(self):
        x = self.turtle.xcor()
        y = self.turtle.ycor()
        return x < -160 or 160 < x or y < -160 or 160 < y

    # calling this will move the turtle in a random direction.
    def move(self):
        turn = randint(0, 2)
        if turn == 1:
            self.turtle.lt(45)
        elif turn == 2:
            self.turtle.rt(45)
        self.turtle.forward(5)


# Put your code for drawing the grid

# Let's create some turtles and start moving them.
turtles = [MyTurtle('billy', 'red'), MyTurtle('chris', 'blue'), MyTurtle('lilly', 'pink'), MyTurtle('kevin', 'green')]

ok = True
while ok:
    for t in turtles:
        t.move()
        if t.off_board():
            print("Turtle %s wins!!!" % (t.name))
            ok = False

turtle.done()
