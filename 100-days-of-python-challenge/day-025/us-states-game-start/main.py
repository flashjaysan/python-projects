import pandas
import turtle
from turtle import Screen, Turtle

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()

screen = Screen()
screen.title('U.S.A. States Game')
usa_image = 'blank_states_img.gif'
screen.addshape(usa_image)
turtle.shape(usa_image)

turtle = Turtle()
turtle.hideturtle()
turtle.up()

states_remaining = len(states)
states_total = states_remaining
exit_loop = False
while states_remaining > 0 and not exit_loop:
    answer = screen.textinput(title=f'{states_total - states_remaining}/{states_total} states', prompt='What\'s another state name?').title()
    if answer in states:
        row = data[data['state'] == answer]
        turtle.goto(int(row['x']), int(row['y']))
        turtle.write(answer, align='center')
        states.remove(answer)
        states_remaining = len(states)
        # print(states) # show states remaining
    elif answer == 'Exit':
        exit_loop = True

if len(states) > 0:
    states_data_frame = pandas.DataFrame(states)
    states_data_frame.to_csv('states_to_review.csv')
