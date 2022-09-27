from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)







screen.exitonclick()
