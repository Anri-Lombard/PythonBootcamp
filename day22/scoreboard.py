from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.rally = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, -250)
        self.write(f"Rally: {self.rally}", align="center", font=("Courier", 20, "normal"))

    def rally_point(self):
        self.rally += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        self.rally = 0

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        self.rally = 0
