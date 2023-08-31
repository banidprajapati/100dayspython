from turtle import Screen
import random
from snake import Snake
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)

snake = Snake()


def move_forward():
    snake.forward(90)


def move_backward():
    snake.back(90)


def rotate_left():
    snake.left(90)


def rotate_right():
    snake.right(90)


game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


screen.exitonclick()
