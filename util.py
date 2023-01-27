import numpy as np


def frange(a, b, step):
    return np.arange(a, b, step)

def within_range(x, y, range):
    return x-range < y < x+range

class NoneTypeException(Exception):
    pass
