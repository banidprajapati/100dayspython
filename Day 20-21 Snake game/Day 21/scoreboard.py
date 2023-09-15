from turtle import Turtle
Text = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.counter}", align="center", font=Text)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=Text)

    def increase_score(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()
