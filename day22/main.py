from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong game")

screen.tracer(0)

r_paddle = Paddle((350, 250))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect when hitting top and bottom wall.
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.y_bounce()

    # detect when hitting paddle.
    if ball.xcor() > 330 and ball.distance(r_paddle) <= 50 or ball.xcor() < -330 and ball.distance(l_paddle) <= 50:
        ball.x_bounce()
        scoreboard.rally_point()

    # detect when missing paddle.
    if ball.xcor() > 350 and ball.distance(r_paddle) > 50:
        scoreboard.l_point()
        ball.x_bounce()
        ball.restart()
    elif ball.xcor() < -350 and ball.distance(l_paddle) > 50:
        scoreboard.r_point()
        ball.x_bounce()
        ball.restart()












screen.exitonclick()