import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.re_location()


    def re_location(self):
        random_x = random.randint(-278, 278)
        random_y = random.randint(-278, 278)
        self.goto(random_x,random_y)
        
