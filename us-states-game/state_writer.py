from turtle import Turtle

FONT = ("arial", 8, "normal")

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()

    def write_state(self, name, coord):
        self.goto(coord)
        self.write(name, align="center", font=FONT)