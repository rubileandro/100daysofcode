from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + 10 + self.xmove
        new_y = self.ycor() + 10 + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1
