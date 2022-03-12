#!/usr/bin/env python3
from turtle import Screen, Turtle, screensize
import random
tim = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


colors = ["CornflowerBlue", "DarkGreen", "PaleGoldenrod",
          "Crimson", "Yellow", "BlueViolet", "Indigo", "Black"]

for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)


screen = Screen()
screen.exitonclick()
