import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.up()
        self.move = [10, self.random_y_direction()]

    def update(self):
        self.showturtle()
        self.goto(self.xcor() + self.move[0], self.ycor() + self.move[1])
        if self.ycor() > 280:
            self.goto(self.xcor(), 280)
            self.move[1] *= -1
        if self.ycor() < -280:
            self.goto(self.xcor(), -280)
            self.move[1] *= -1

    def check_for_point(self, score):
        if self.xcor() > 380:
            self.hideturtle()
            self.home()
            self.move = [-10, self.random_y_direction()]
            score.point_to_l_player()
        if self.xcor() < -380:
            self.hideturtle()
            self.home()
            self.move = [10, self.random_y_direction()]
            score.point_to_r_player()

    def random_y_direction(self):
        return random.randint(-20, 20)

    def check_collision_with_left_paddle(self, l_paddle):
        if self.xcor() - 20 < l_paddle.xcor() + 20 and self.xcor() + 20 > l_paddle.xcor() and self.ycor() - 20 < l_paddle.ycor() + 50 and self.ycor() + 20 > l_paddle.ycor() - 50:
            self.goto(l_paddle.xcor() + 40, self.ycor())
            self.move = [10, (self.ycor() - l_paddle.ycor()) / 4]

    def check_collision_with_right_paddle(self, r_paddle):
        if self.xcor() - 20 < r_paddle.xcor() + 20 and self.xcor() + 20 > r_paddle.xcor() and self.ycor() - 20 < r_paddle.ycor() + 50 and self.ycor() + 20 > r_paddle.ycor() - 50:
            self.goto(r_paddle.xcor() - 40, self.ycor())
            self.move = [-10, (self.ycor() - r_paddle.ycor()) / 4]

