import turtle as turtle_module

tim = turtle_module.Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def anti_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.reset()


screen = turtle_module.Screen()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=anti_clockwise, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
