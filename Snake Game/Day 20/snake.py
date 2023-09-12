from turtle import Turtle

snake_starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
left = 180
right = 0
up = 90
down = 270


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.headposition = self.segment[0]

    def create_snake(self):
        for i in snake_starting_pos:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.segment.append(new_segment)

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.headposition.forward(move_distance)

    def up(self):
        if self.headposition.heading() != down:
            self.headposition.setheading(up)

    def down(self):
        if self.headposition.heading() != up:
            self.headposition.setheading(down)

    def left(self):
        if self.headposition.heading() != right:
            self.headposition.setheading(left)

    def right(self):
        if self.headposition.heading() != left:
            self.headposition.setheading(right)
