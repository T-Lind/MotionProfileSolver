import math

from custom_curve.Point import Point, PointSeries


class Curve:
    @staticmethod
    def gen_pts(start_t, end_t, num):
        points = PointSeries(shape=num)
        for i in range(num):
            points[i].t = (i / num) * (end_t - start_t) + start_t
            points[i].idx = i
        return points

    def __init__(self, start: Point, end: Point, num=1000, max_v=4, max_a=0.25):
        self.points = Curve.gen_pts(start.t, end.t, num)

        self.points[0] = start
        self.points[-1] = end

        self.da = end.a - start.a
        self.dv = end.v - start.v
        self.dt = end.t - start.t

        x_pos = start.x
        idx = 0
        while x_pos < (start.x + end.x) / 2:
            point = self.points[idx]
            point.a = max_a
            point.v = point.a * point.t + point.t / 10 * max_v
            point.x = point.v * point.t + start.x
            x_pos = point.x
            idx += 1
        idx -= 1
        half_time = self.points[idx].t-start.t
        accel = lambda t: abs((end.a-start.a)/2)*math.cos(math.pi/half_time*(t-half_time))+abs((end.a-start.a)/2)+end.a
        while x_pos < end.x:
            point = self.points[idx]
            point.a = accel(point.t)*()
            point.v = point.a * point.t + self.points[idx - 1].v
            point.x = point.v * point.t + start.x
            x_pos = point.x
            idx += 1
