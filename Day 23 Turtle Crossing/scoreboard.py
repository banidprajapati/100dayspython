from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def increase_level(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.increase_level()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="Left", font=FONT)
