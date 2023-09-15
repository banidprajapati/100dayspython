from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.pensize(5)
        self.goto(0, 300)
        self.setheading(270)

        for _ in range(1, 18):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
