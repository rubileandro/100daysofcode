from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")


# Triangle 360 / 3 = 120
for _ in range(3):
    timmy.right(120)
    timmy.forward(100)

# Square 360 / 4 = 90
for _ in range(4):
    timmy.right(90)
    timmy.forward(100)

# Pentagon 360 / 5 = 72
for _ in range(5):
    timmy.right(72)
    timmy.forward(100)

# Hexagon 360 / 6 = 60
for _ in range(6):
    timmy.right(60)
    timmy.forward(100)

# Heptagon 360 / 7 = 51.4
for _ in range(7):
    timmy.right(51.4)
    timmy.forward(100)

# Octagon 360 / 8 = 45
for _ in range(8):
    timmy.right(45)
    timmy.forward(100)

# Nonagon 360 / 9 = 40
for _ in range(9):
    timmy.right(40)
    timmy.forward(100)

# Decagon 360 / 10 = 36
for _ in range(10):
    timmy.right(36)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
