from turtle import Turtle, colormode, Screen
import random

turtle = Turtle()
color = colormode(255)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [180, 90, 270, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


turtle.pensize(10)
turtle.speed(0)

for _ in range(200):
    turtle.color(random_color())
    turtle.setheading(random.choice(angle))
    turtle.forward(30)


