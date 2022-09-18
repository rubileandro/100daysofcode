import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed(0)


for _ in range(5000):
    timmy.color(random_color())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
