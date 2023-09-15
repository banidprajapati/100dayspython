from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_user_paddle(x, y)

    def create_user_paddle(self, x, y):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.shapesize(5, 1)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
