import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()
correct_guesses = []

while len(correct_guesses) < 50:
    score = len(correct_guesses)
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="Which states are in America?")
    formatted_answer_state = answer_state.title()

    if formatted_answer_state == "Exit":
        break

    if formatted_answer_state in state_list:
        correct_row = data[data.state == formatted_answer_state]
        writer.goto(int(correct_row.x), int(correct_row.y))
        writer.write(formatted_answer_state)
        correct_guesses.append(formatted_answer_state)

# missing_states.csv
missing_states = {
    "state": []
}
for state in data.state:
    if state not in correct_guesses:
        missing_states["state"].append(state)
        writer.color("red")
        correct_row = data[data.state == state]
        writer.goto(int(correct_row.x), int(correct_row.y))
        writer.write(state)

pandas.DataFrame(missing_states).to_csv("missing_states.csv")
screen.exitonclick()
