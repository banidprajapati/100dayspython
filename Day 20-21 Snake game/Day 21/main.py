from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(620, 620)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.headposition.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.headposition.xcor() > 300 or snake.headposition.xcor() < -300 or snake.headposition.ycor() > 300 or snake.headposition.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.headposition.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
