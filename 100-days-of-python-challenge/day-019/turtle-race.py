import random
import turtle

screen = turtle.Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []
for i in range(len(colors)):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(-230, -150 + i * 60)
    turtles.append(new_turtle)

is_race_on = False
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
if user_bet:
    is_race_on = True

while is_race_on:
    for current_turtle in turtles:
        current_turtle.forward(random.randint(1, 10))
        if current_turtle.xcor() >= 230:
            winning_color = current_turtle.pencolor()
            is_race_on = False

if winning_color == user_bet:
    print(f'You\'ve won. The {winning_color} turtle crossed the finishing line first.')
else:
    print(f'You\'ve lost. The {winning_color} turtle crossed the finishing line first.')

screen.exitonclick()
