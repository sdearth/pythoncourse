from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.pu()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.turtlesize(stretch_len=2)
            car.seth(180)
            start_y = random.randrange(-250, 250, 20)
            car.goto(640, start_y)
            self.cars.append(car)

    def move_cars(self, round):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE * round)