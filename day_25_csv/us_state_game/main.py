#!/usr/bin/env python3

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/mdkhan/Code/python/100-days-python-with-udeny/day_25_csv/us_state_game/map.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

df = pandas.read_csv("50_states.csv")
states = df.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state").title()
    if answer == "Exit":
        break
    
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = df[df.state == answer]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(states_data.state.item())

# turtle.mainloop()
screen.exitonclick()
