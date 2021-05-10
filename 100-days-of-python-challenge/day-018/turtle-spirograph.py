import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)
timmy.width(2)
for i in range(90):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(360 / 90)


screen = turtle.Screen()
screen.exitonclick()
