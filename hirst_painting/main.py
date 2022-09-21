import turtle as turtle_module
import random


turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
color_list = [(147, 86, 56), (204, 143, 117), (216, 203, 188), (70, 31, 15), (188, 106, 79), (108, 47, 28),
              (47, 8, 11), (193, 194, 200), (182, 186, 194), (97, 66, 19), (229, 194, 138), (202, 197, 199),
              (187, 190, 198), (214, 184, 172), (187, 178, 182), (154, 128, 91), (197, 188, 190), (193, 196, 194),
              (169, 174, 171), (123, 94, 98), (127, 20, 26), (187, 193, 195), (189, 193, 191), (148, 114, 117),
              (26, 36, 21), (80, 96, 83), (112, 107, 120), (20, 18, 29), (53, 72, 49), (114, 134, 123)]


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
