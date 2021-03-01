from turtle import Turtle, Screen
import random

def get_angle(sides):
    return 360/sides

def get_random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# tim.pu()
# tim.goto(0.0 - screen.window_width()/2, 0.0)
# for _ in range(15):
#     tim.pd()
#     tim.forward(10)
#     tim.pu()
#     tim.fd(10)

# screen.colormode(255)
# for sides in range(3, 21):
#     angle = get_angle(sides)
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     tim.pencolor((r, g, b))
#     for _ in range(sides):
#         tim.fd(50)
#         tim.rt(angle)

screen.colormode(255)

# tim.pensize(5)
# tim.hideturtle()
# directions = [0, 90, 180, 270]
# while True:
#     tim.pencolor(get_random_color())
#     tim.seth(random.choice(directions))
#     tim.fd(10)

tim.speed("fastest")
tim.hideturtle()
for _ in range(120):
    tim.pencolor(get_random_color())
    tim.circle(100)
    tim.seth(tim.heading() + 3)

screen.exitonclick()