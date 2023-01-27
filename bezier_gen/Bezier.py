import enum
import math

from util import frange
from bezier_gen.Series import Point, Series


class Bezier:
    def __init__(self, control_values, resolution=0.001):
        self.data = {"points": Series(), }

        # Provided control values
        self.__control_values = control_values

        # The resolution of the bezier curve
        self.__resolution = resolution

        # A list of times one less than 1/resolution long
        self.time_list = frange(0, 1, 1 / self.__resolution)

        # Create the bezier curve
        for current_time in range(0, int(1 / self.__resolution), 1):
            current_point = Bezier.recursive_lerp(self.__control_values, current_time * self.__resolution)
            self.data["points"].append(current_point)

        # Calculate timewise derivative

        # Temp variable to ease naming
        points = self.data["points"]
        self.data["timewise_deriv"] = Series()
        for i in range(0, len(points) - 1):
            pt0 = points[i]
            pt1 = points[i+1]
            self.data["timewise_deriv"].append(Point(pt0.x, (pt1.y - pt0.y) / (pt1.x - pt0.x)))

    def __call__(self):
        return self.data

    def __getitem__(self, item):
        return self.data[item]

    @staticmethod
    def lerp(point0, point1, t):
        """
        Perform linear interpolation between two points. ex. t=0.5 is halfway between them
        :param point0:
        :param point1:
        :param t: the time to interpolate at
        :return: the linear interpolated point
        """
        return point0.mul(1 - t) + point1.mul(t)

    @staticmethod
    def recursive_lerp(points, time):
        """
        Recursively perform linear interpolation between a list of control points given a time along the bezier curve (t is 0-1)
        :param points: The list of control points to perform recursive linear interpolation on
        :param time: the moment in time to grab the current point
        :return: The point into the curve based on the time and set of control points
        """
        if len(points) == 2:
            return Bezier.lerp(points[0], points[1], time)

        index = 0
        list_of_lerps = []
        while index < len(points) - 1:
            point1 = Bezier.lerp(points[index], points[index + 1], time)
            list_of_lerps.append(point1)
            index += 1

        return Bezier.recursive_lerp(list_of_lerps, time)
