
from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("MD's Snack Game")
screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

new_snacks = []

for position in starting_positions:
    snack = Turtle('square')
    snack.color('white')
    snack.penup()
    snack.goto(position)
    new_snacks.append(snack)

# move snaks
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for snack_parts_num in new_snacks:
        


def move_forward():
    snack.forward(10)


def move_backward():
    snack.backward(10)


def turn_up():
    new_heading = snack.heading() + 90
    snack.setheading(new_heading)


def turn_down():
    new_heading = snack.heading() - 90
    snack.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_up)
screen.onkey(key="d", fun=turn_down)


screen.exitonclick()
