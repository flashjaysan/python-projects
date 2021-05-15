import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 20


class CarManager:

    def __init__(self):
        self.speed_multiplier = 1
        self.cars = []
        for _ in range(NUMBER_OF_CARS):
            self.create_car()

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.turtlesize(stretch_len=2)
        car.color(random.choice(COLORS))
        car.up()
        car.goto(random.randint(-300, 300), random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.hideturtle()
                car.goto(320, car.ycor())
            else:
                car.showturtle()
                car.backward(MOVE_INCREMENT * self.speed_multiplier)

    def increase_speed(self):
        self.speed_multiplier += 0.5

    def check_collision(self, player):
        collision = False
        for car in self.cars:
            if car.distance(player) < 20:
                collision = True
        return collision
