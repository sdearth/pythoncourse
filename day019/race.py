from turtle import Turtle, Screen, color
import random

is_race_on = False  
screen = Screen()
screen.setup(width=500, height=400)
colors = ("red", "orange", "yellow", "blue", "green")
turtles = []

for index in range(0, 5):
    turtles.append(Turtle(shape="turtle", visible=False))
    turtles[index].color(colors[index])
    turtles[index].pu()
    turtles[index].goto(x=-230, y=100 - (index * 50))
    turtles[index].showturtle()


user_bet = screen.textinput("Place your bet", "Who will win? Enter a color:")

if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0,10)
    turtle_index = random.randint(0, 4)
    turtles[turtle_index].forward(random_distance)
    if turtles[turtle_index].xcor() >= 230:
        winner_color = turtles[turtle_index].pencolor()
        if user_bet == winner_color:
            print("You've won!")
        else:
            print("You've lost!")
        is_race_on = False

screen.exitonclick()