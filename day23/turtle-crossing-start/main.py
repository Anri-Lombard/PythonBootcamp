import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with car.
    for car in car_manager.total_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.reset()

    # detect successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    # if player.game_over():
    #     scoreboard.reset_scoreboard()
screen.exitonclick()