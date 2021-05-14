from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.up()
        self.goto(0, 260)

    def draw(self, level):
        self.clear()
        self.write(f'Level: {level}', align='center', font=FONT)

    def end(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)
