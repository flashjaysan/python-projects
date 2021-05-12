from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.update()

game_is_on = True
while game_is_on:
    snake.move()
    if snake.head.distance(food) < 19:
        food.reset_position()
        snake.extend()
        scoreboard.update_score()
    scoreboard.display_score()
    screen.update()
    time.sleep(0.1)
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280 or snake.ate_itself():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
