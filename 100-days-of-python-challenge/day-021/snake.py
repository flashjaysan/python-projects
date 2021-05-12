from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        for i in range(3):
            self.add_segment((i * -20, 0))
        self.head = self.turtles[0]

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.color('white')
        new_turtle.shape('square')
        new_turtle.up()
        new_turtle.goto(position[0], position[1])
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def ate_itself(self):
        collide = False
        for segment in self.turtles[1:]:
            if self.head.distance(segment) < 19:
                collide = True
        return collide

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
