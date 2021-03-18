import turtle
import pandas
from state_writer import StateWriter

states = pandas.read_csv("50_states.csv")
title = "Guess the State"
screen = turtle.Screen()
score = 0
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = StateWriter()
state_list = states.state.to_list()

while score < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state?" )
    if answer_state == None:
        turtle.bye()
        break
    answer_state = answer_state.title()
    state = states[states.state == answer_state]
    if not state.empty:
        score += 1
        if answer_state in state_list: state_list.remove(answer_state)
        name = state.state.iloc[0]
        x = state.x.iloc[0]
        y = state.y.iloc[0]
        writer.write_state(name, (x, y))
    title = f"Score: {score}/50"

frame = pandas.DataFrame({"missing": state_list})
frame.to_csv("missing.csv")
