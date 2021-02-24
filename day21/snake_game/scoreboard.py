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
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, HALF_HEIGHT - 15)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Current score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
