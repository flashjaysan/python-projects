import math


class Vector2:

    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2

    def normalized(self):
        length = self.length()
        return Vector2(self.x / length, self.y / length)

    def to_tuple(self):
        return self.x, self.y
