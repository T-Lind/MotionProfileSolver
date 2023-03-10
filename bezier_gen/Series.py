import math
from util import NoneTypeException

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other, self.y + other)

    def distance_to(self, other):
        return math.hypot(abs(other.x - self.x), abs(other.y - self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def mul(self, other):
        return Point(self.x * other, self.y * other)

    def __str__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y) + "\n"


class Series:
    """
    Object
    """
    def __init__(self, values: list[Point] = None):
        if values is None:
            self._values = []
        else:
            self._values = values

    def __call__(self):
        return self._values

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def get(self, index):
        return self._values[index]

    def append(self, item: Point):
        self._values.append(item)

    def get_x(self):
        Series.none_check(self._values)
        return [pt.x for pt in self._values]

    def get_y(self):
        Series.none_check(self._values)
        return [pt.y for pt in self._values]

    @staticmethod
    def none_check(item):
        if item is None:
            raise NoneTypeException("Item retrieved was None!")
