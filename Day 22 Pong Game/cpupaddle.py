from turtle import Turtle


class Cpupaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cpu_paddle()

    def create_cpu_paddle(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(350, 0)
        self.shapesize(5, 1)
