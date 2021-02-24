from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1400, height=800)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
# These onkey methods require a function.
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
