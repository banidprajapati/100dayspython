from turtle import Turtle, colormode, Screen
import random


colormode(255)
turtle = Turtle()
turtle.speed(0)
angle = 0
turtle.pensize(1.5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(73):

    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(angle)
    angle += 5


screen = Screen()
screen.exitonclick()
