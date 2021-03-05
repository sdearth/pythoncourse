from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.x_incr = 10
        self.y_incr = 10
        super(Ball, self).__init__()
        self.pu()
        self.color("white")
        self.shape("circle")
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_incr
        new_y = self.ycor() + self.y_incr
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_incr *= -1

    def bounce_x(self):
        self.x_incr *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.bounce_x()
        self.goto(0, 0)