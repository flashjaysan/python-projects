from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=('Arial', 18, 'normal'))
