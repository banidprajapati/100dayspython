"""
- screen 🟩
- net 🟩
- paddle and make it move with arrows 🟩
- cpu paddle, make it move up and down continuously 🟩
- ball and moving it 🟩
- ball detects collision with the paddles 🟩
- ball detects collision with walls 🟩
- scoreboard 🟩
- detect loses and update scoreboard accordingly 🟩
"""


from turtle import Screen
from paddle import Paddle
from net import Net
from scorebaord import Score
from ball import Ball
import time

screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Score()
net = Net()
ball = Ball()


screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collision()

    if ball.xcor() > 380:
        scoreboard.l_points()
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard.r_points()
        ball.reset()


screen.exitonclick()
