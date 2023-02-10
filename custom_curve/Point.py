import numpy as np

class Point:
    def __init__(self, x=0, v=0, a=0, t=0, idx=0):
        self.x = x
        self.v = v
        self.a = a
        self.t = t
        self.idx = idx

        self.corr_dict = {
            "x": self.x,
            "v": self.v,
            "a": self.a,
            "t": self.t,
            "idx": self.idx,
        }
    def update(self):
        self.corr_dict = {
            "x": self.x,
            "v": self.v,
            "a": self.a,
            "t": self.t,
            "idx": self.idx,
        }

class PointSeries:
    def __init__(self, shape=None):
        self._data = [Point() for _ in range(shape)]

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self):
        return len(self._data)

    def get_linspace(self, key):
        for point in self._data:
            point.update()
        return [self._data[i].corr_dict[key.lower()] for i in range(self.__len__())]

