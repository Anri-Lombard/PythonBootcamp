import turtle

# To work with imports go see the docs.

timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("dark orchid")
timmy.fd(100)
timmy.rt(90)
timmy.fd(100)
timmy.lt(90)
timmy.fd(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()