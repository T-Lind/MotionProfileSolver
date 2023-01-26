import matplotlib.pyplot as plt
import numpy as np

from fractional_calculus.differint import fractional_integral


def f(x):
    return x ** 2


print(fractional_integral(2.9, 1.2, f, res=0.001))

x = np.arange(0, 4, 0.01)
y = [f(v) for v in x]
y_p1 = [fractional_integral(1.5, t, f) for t in x]
y_p2 = [fractional_integral(2.3 + 1, t, f) for t in x]
plt.plot(x, y, label="f(x)")
plt.plot(x, y_p1, label="F1.5(x)")
plt.plot(x, y_p2, label="F2.3(X)")
plt.legend()
plt.title("Fractional integration in Python")
plt.show()
