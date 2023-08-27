from turtle import Turtle, colormode, Screen
import random

colormode(255)
rgb_color = [(202, 164, 110), (149, 75, 50), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (14, 98, 70), (232, 176, 165),
             (160, 142, 158), (101, 75, 77), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (168, 99, 102)]
turtle = Turtle()

x_cord = -250
y_cord = -250
turtle.hideturtle()
turtle.penup()
turtle.goto(x_cord, y_cord)
turtle.speed(0)


def art_generator(square, y_cord=-250):
    for _ in range(square):
        y_cord += 50
        turtle.goto(x_cord, y_cord)
        for _ in range(square):
            turtle.dot(30, random.choice(rgb_color))
            turtle.forward(50)


art_generator(10)
screen = Screen()
print(screen.screensize())
screen.exitonclick()
