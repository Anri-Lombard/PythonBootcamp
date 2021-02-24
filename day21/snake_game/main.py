from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SPEED = 0.1
WIDTH = 600
HEIGHT = 600
HALF_WIDTH = int(WIDTH / 2) - 20
HALF_HEIGHT = int(HEIGHT / 2) - 20

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# These onkey methods require a function.
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)

    snake.move()

    # detect collison with food
    if snake.head.distance(food) < 16:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() < -HALF_WIDTH or snake.head.xcor() > HALF_WIDTH or snake.head.ycor() < -HALF_HEIGHT or snake.head.ycor() > HALF_HEIGHT:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
