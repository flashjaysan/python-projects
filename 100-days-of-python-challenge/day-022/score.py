from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.up()
        self.goto(0, 260)
        self.l_point = 0
        self.r_point = 0
        self.print_score()

    def point_to_l_player(self):
        self.l_point += 1

    def point_to_r_player(self):
        self.r_point += 1

    def print_score(self):
        self.clear()
        self.write(f'{self.l_point} : {self.r_point}', align='center')

    def game_over(self):
        return self.l_point >= 11 or self.r_point >= 11

    def end(self):
        self.home()
        self.write('GAME OVER', align='center')
        self.goto(0, 20)
        if self.l_point >= 11:
            winner = 'Left player'
        else:
            winner = 'Right player'
        self.write(winner + ' won.', align='center')

