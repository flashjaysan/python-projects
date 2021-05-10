import colorgram
import random
import turtle

colorgram_colors = colorgram.extract('image.jpg', 30)
colors = []
for color in colorgram_colors:
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.up()
timmy.hideturtle()
timmy.speed(10)
timmy.goto(-315, -315)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(70)
    timmy.goto(-315, timmy.ycor() + 70)

screen = turtle.Screen()
screen.exitonclick()
