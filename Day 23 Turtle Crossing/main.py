import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkeypress(key="Up", fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        cars.car_movement()
        scoreboard.update_score()
        player.reset()

screen.exitonclick()
