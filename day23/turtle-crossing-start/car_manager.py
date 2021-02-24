from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
INCREMENT_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.total_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        choice = random.randint(1, 6)
        if choice == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_position = random.randint(-250, 250)
            new_car.goto(320, y_position)
            self.total_cars.append(new_car)

    def move_cars(self):
        for car in self.total_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT_DISTANCE


