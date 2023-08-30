from turtle import Turtle, Screen, distance
from random import randint

list_turtle = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5"]
list_color = ["red", "blue", "orange", "green", "purple"]
x_pos = -400
y_pos = -150
screen = Screen()
screen.setup(900, 480)


def win_condition(position):
    if position < 400:
        return True


for i in range(0, 5):
    list_turtle[i] = Turtle()
    list_turtle[i].color(list_color[i])
    list_turtle[i].shape("turtle")
    list_turtle[i].penup()
    list_turtle[i].setpos(x_pos, y_pos)
    y_pos += 80

position = 0
while win_condition(position):
    for i in range(0, 5):
        random = randint(1, 5)
        if random < 3:
            list_turtle[i].forward(10)
        position = list_turtle[i].xcor()
        win_condition(position)


screen.exitonclick()
