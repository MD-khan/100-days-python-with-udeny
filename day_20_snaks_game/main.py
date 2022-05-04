
from snake import Snake
from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("MD's Snack Game")
screen.tracer(0)

snake = Snake()

# starting_position = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
