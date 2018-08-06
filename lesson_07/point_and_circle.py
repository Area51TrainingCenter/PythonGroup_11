class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


point = Point(3, 4)
print(point)


class Circle(Point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return '({}, {}) with radius: {}'.format(self.x, self.y, self.radius)


circle = Circle(3, 4, 4)
print(circle)

