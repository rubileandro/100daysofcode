from turtle import Screen
from snake import Snake
import time
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snak%e Game")
screen.tracer(0)


snake = Snake()
food = Food()

screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # print("nom nom nom")
        food.refresh()


screen.exitonclick()
