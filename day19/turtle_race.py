from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color ("
                                                          "red/orange/yellow/green/blue/purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

ref = Turtle(shape="turtle")
ref.color("black")
ref.speed("slowest")
ref.penup()
ref.goto(x=230, y=190)
ref.setheading(270)
ref.pensize(10)
ref.color("gray")
ref.pendown()
ref.fd(370)
ref.hideturtle()

x = -230
y = -130
all_turtles = []
for turtle_color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color)
    new_turtle.goto(x=x, y=y)
    all_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.fd(random.randint(0, 10))
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You're right! The {winning_color} turtle won!")
            else:
                print(f"You're wrong! The {winning_color} turtle won!")


screen.exitonclick()
