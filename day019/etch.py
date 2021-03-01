from turtle import Turtle, Screen

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def right():
    tim.right(10)

def left():
    tim.left(10)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
