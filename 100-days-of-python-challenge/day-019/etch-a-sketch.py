import turtle

DISTANCE = 50
ANGLE = 30

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(DISTANCE)


def move_backward():
    tim.backward(DISTANCE)


def turn_left():
    tim.left(ANGLE)


def turn_right():
    tim.right(ANGLE)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen.listen()
screen.onkey(key="z", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="q", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
