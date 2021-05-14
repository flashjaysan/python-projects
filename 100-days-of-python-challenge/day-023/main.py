import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Frogger')
screen.bgcolor('white')
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()
scoreboard.draw(level)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    if player.crossed_finish_line():
        player.reset_position()
        level += 1
        car_manager.increase_speed()
    car_manager.move_cars()
    if car_manager.check_collision(player):
        game_is_on = False
    scoreboard.draw(level)
    time.sleep(0.1)
    screen.update()

scoreboard.end()
screen.update()

screen.exitonclick()
