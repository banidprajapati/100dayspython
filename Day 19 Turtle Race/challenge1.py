from turtle import Turtle, Screen

turtle = Turtle()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.back(10)


def rotate_left():
    turtle.left(10)


def rotate_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
