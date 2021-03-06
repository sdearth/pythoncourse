from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment(self):
        self.level += 1
        self.write_score()

    def get_level(self):
        return self.level

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)