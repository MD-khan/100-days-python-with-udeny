#!/usr/bin/env python3
import random
from turtle import Screen
import turtle as t
import random


colors = ["DarkSlateBlue", "Crimson", "DarkRed",
          "DarkOrange", "MediumPurple", "DarkGreen", "DarkSeaGreen", "Black", "Navy"]
direction = [0, 90, 180, 270]

munisa = t.Turtle()
t.colormode(255)
munisa.pensize(15)
munisa.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for i in range(5000):
    munisa.color(random_color())
    munisa.forward(30)
    munisa.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
