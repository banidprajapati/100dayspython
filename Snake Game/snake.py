from turtle import Turtle

snake_starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

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
        self.segment[0].forward(move_distance)
        
    def up(self):
        self.head


    def down():
        snake.back(90)


    def left():
        snake.left(90)


    def right():
        snake.right(90)
