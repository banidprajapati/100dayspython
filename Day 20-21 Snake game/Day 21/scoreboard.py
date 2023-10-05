from turtle import Turtle
Text = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Score: {self.counter}   |   Highscore: {self.highscore}", align="center", font=Text)

    def reset(self):
        if self.counter > self.highscore:
            self.highscore = self.counter
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.counter = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", align="center", font=Text)

    def increase_score(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()
