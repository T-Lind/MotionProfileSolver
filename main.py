import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

from fractional_calculus.differint import fractional_integral


def f(x):
    return np.sin(x) + 2 * np.sin(3 * x) + np.sin(0.3 * x) + x**1.1 - 2*x

plt.title("Fractional derivative in Python")

fig = plt.figure()
plt.subplots_adjust(bottom=0.4)
ax = fig.subplots()

x = np.arange(0, 4, 0.01)
y = [f(v) for v in x]
plt.title("Fractional integration in python")

ax_slide1 = plt.axes([0.25, 0.25, 0.65, 0.03])
s_factor1 = Slider(ax_slide1, 'p',
                   0, 6, valinit=1, valstep=0.2)


def update(_):
    order_deriv = s_factor1.val
    y_p = [fractional_integral(order_deriv, t, f) for t in x]
    ax.clear()
    ax.plot(x, y_p, label="Fn(x)", color="red")
    ax.plot(x, y, label="f(x)", color="blue")
    ax.legend()


ax.plot(x, y, label="f(x)", color="blue")
ax.legend()
s_factor1.on_changed(update)
plt.show()
