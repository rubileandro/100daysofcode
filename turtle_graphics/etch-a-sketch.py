from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
