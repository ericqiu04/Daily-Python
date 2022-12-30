import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("Red")
        self.penup()
        self.speed("fastest")

        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 480)

        self.goto(random_x, random_y)
