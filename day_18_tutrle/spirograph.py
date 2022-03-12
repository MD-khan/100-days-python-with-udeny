#!/usr/bin/env python3
from turtle import Screen
import turtle as t
import random


munisa = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


munisa.speed("fastest")
munisa.pensize(1)


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        munisa.color(random_color())
        munisa.circle(100)
        munisa.setheading(munisa.heading() + gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
