import turtle
import random

directions = [0, 90, 180, 270]
colors = ['floral white',
          'antique white',
          'bisque',
          'mint cream',
          'lavender',
          'dark slate gray',
          'light slate gray',
          'cornflower blue',
          'slate blue',
          'royal blue',
          'light sea green',
          'yellow',
          'purple',
          'maroon',
          'coral',
          'orange',
          'salmon',
          'tomato',
          'red',
          'turquoise',
          'cyan',
          ]

timmy = turtle.Turtle()
timmy.down()
timmy.speed(10)
timmy.width(10)

while True:
    timmy.setheading(random.choice(directions))
    timmy.color(random.choice(colors))
    timmy.forward(50)

screen = turtle.Screen()
screen.exitonclick()
