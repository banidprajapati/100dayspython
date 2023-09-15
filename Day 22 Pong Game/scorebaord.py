from turtle import Turtle

Alignment = "Center"
Font = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.L_score = 0
        self.R_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-50, 190)
        self.write(f"{self.L_score}", align=Alignment, font=Font)
        self.goto(50, 190)
        self.write(f"{self.R_score}", align=Alignment, font=Font)

    def l_points(self):
        self.L_score += 1
        self.clear()
        self.update_scoreboard()

    def r_points(self):
        self.R_score += 1
        self.clear()
        self.update_scoreboard()
