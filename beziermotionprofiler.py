from bezier_gen.Bezier import Bezier
from bezier_gen.Series import Point
from util import frange
import matplotlib.pyplot as plt

curve = Bezier([Point(0, 0), Point(0.1, 0), Point(0.9, 2), Point(1, 2)])
plt.plot(curve["points"].get_x(), curve["points"].get_y())
plt.show()
