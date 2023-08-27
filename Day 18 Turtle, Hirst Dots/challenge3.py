from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("palegreen4")

colors = ["", "", "", "royal blue", "red", "dark slate gray",
          "saddle brown", "magenta", "pink", "misty rose", "firebrick"]
for i in range(3, 11):
    angle = 360 / i
    turtle.pencolor(colors[i])
    j = 0
    while j < i:
        turtle.forward(100)
        turtle.right(angle)
        j += 1

screen = Screen()
screen.exitonclick()
