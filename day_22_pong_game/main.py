
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Md's Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


gmae_on = True
while gmae_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # detect collition sith wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounch_y()
    
    # detect collition with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounh_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
    
    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()
    


screen.exitonclick()
