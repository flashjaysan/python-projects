import turtle

t = turtle.Turtle()


def move_forwards():
    t.forward(10)


screen = turtle.Screen()
screen.listen()
screen.onkey(move_forwards, 'space')
screen.exitonclick()
