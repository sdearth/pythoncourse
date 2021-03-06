import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    manager.add_car()
    manager.move_cars(scoreboard.get_level())
    screen.update()

    # detect collision with car
    for car in manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.at_finish_line():
        scoreboard.increment()
        player.go_home()

screen.exitonclick()
