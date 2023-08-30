from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)


snake_list = [1, 2, 3]
segment = []
initial_x_pos = 0
initial_y_pos = 0


for i in snake_list:
    i = Turtle(shape="square")
    i.color("white")
    i.penup()
    initial_x_pos -= 20
    i.goto(initial_x_pos, initial_y_pos)
    segment.append(i)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segment:
        seg.forward(20)


screen.exitonclick()
