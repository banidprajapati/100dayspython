from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.all_cars = []

    def generate_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_axis = random.randint(-230, 230)
            new_car.goto(320, y_axis)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.STARTING_MOVE_DISTANCE)

    def car_movement(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
