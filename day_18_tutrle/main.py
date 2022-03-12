#!/usr/bin/env python3
from turtle import Screen, Turtle

timmy = Turtle()
timmy.color("green")


pix = 5
for i in range(15):
    timmy.forward(pix)
    timmy.penup()
    timmy.forward(pix)
    timmy.pendown()
# for i in range(1000):
#     timmy.forward(pix)
#     timmy.color("white")
#     timmy.left(90)
#     timmy.forward(pix)
#     timmy.color("green")
#     timmy.forward(pix)


screen = Screen()
screen.exitonclick()
