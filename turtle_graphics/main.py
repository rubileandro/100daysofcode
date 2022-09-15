from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen4")

# # first attempt
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# Solution
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = Screen()
screen.exitonclick()
