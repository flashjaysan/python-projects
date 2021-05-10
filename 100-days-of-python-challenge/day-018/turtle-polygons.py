import turtle

timmy = turtle.Turtle()
timmy.up()
timmy.goto(-50, 350)
timmy.down()
timmy.speed(10)

for i in range(3, 23):
    angle = 360 / i
    for _ in range(i):
        timmy.forward(100)
        timmy.right(angle)

screen = turtle.Screen()
screen.exitonclick()
