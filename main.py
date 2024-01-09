import turtle
import pandas
from turtle import Screen

EXIT_COMMAND = "Exit"
FONT = ("Courier", 12, "bold")

screen = Screen()
screen.title("US States Game")
image = "blank_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    user_guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another states "
                                                                                            "name?").title()

    if user_guess == EXIT_COMMAND:
        break
    if user_guess in states:
        correct_guesses.append(user_guess)

        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_info = data[data.state == user_guess]
        state_name.goto(int(state_info.x.iloc[0]), int(state_info.y.iloc[0]))
        state_name.color("red")
        state_name.write(state_info.state.item(), font=FONT)

missed_states = [state for state in states if state not in correct_guesses ]
df = pandas.DataFrame(missed_states, columns=['missed_states'])
df.to_csv("results.csv")

