from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.update()
    ball.check_collision_with_left_paddle(l_paddle)
    ball.check_collision_with_right_paddle(r_paddle)
    ball.check_for_point(score)
    score.print_score()
    if score.game_over():
        game_is_on = False
    time.sleep(0.01)
    screen.update()

score.end()
screen.update()

screen.exitonclick()