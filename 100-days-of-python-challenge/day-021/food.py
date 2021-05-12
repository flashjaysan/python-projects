from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.up()
        self.speed('fastest')
        self.reset_position()

    def reset_position(self):
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
