from turtle import Turtle
# The scoreboard is now a turtle so I can just treat it as such.


HEIGHT = 600
WIDTH = 600
HALF_WIDTH = int(WIDTH / 2) - 20
HALF_HEIGHT = int(HEIGHT / 2) - 20
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as file_read:
            self.high_score = int(file_read.read())
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, HALF_HEIGHT - 15)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current score: {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file_append:
                file_append.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
