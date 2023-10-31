import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
df = pd.DataFrame(data)

correct_guess = []
screen = turtle.Screen()
screen.title("The U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(correct_guess) < 50:
    answer_state = screen.textinput(
        title=f"Score: {len(correct_guess)}/ 50",
        prompt="Enter a state name: ",
    ).title()

    if answer_state == "Exit":
        missing_state = [state for state in data.state if state not in correct_guess]
        data = pd.DataFrame(missing_state)
        data.to_csv("states_to_learn.csv")
        break

    for index, rows in df.iterrows():
        if answer_state == rows.state:
            correct_guess.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(rows["x"], rows["y"])
            t.write(answer_state, align="center")
