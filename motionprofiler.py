import matplotlib.pyplot as plt
import numpy as np

from fractional_calculus.differint import fractional_integral
from util import frange, within_range


def create_target_equation(x, v, a, offset=0):
    return lambda t: x + v * (t - offset) + 0.5 * a * (t - offset) ** 2


def f(t):
    return create_target_equation(0.4, 1, 0.3)(t)


def g(t, meeting_time=1):
    return create_target_equation(0.9, 0, 0, offset=meeting_time)(t)


def generate_curve(meeting_time, res=0.01):
    result = []
    for t in frange(0, meeting_time, res):
        val = fractional_integral(2, t, f)
        result.append(val)

        for p in frange(0, 4, 0.5):
            if t != 0 and within_range(val, fractional_integral(p, t, g), 0.1):
                print(f"Val:{val}, p:{p}")
    return result


res = 0.01
t = np.arange(0, 4, res)
plt.plot(t, f(t))
plt.plot(t, g(t))
plt.plot(t[:100], generate_curve(1))
plt.show()
