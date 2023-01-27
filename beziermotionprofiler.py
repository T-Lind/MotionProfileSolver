from bezier_gen.Bezier import BezierProfiler
from bezier_gen.Series import Point
from util import frange
import matplotlib.pyplot as plt

if __name__ == "__main__":
    profile = BezierProfiler(start=0, end=1, start_v=1, end_v=0)
    plt.plot(profile.curve["points"].get_x(), profile.curve["points"].get_y())
    plt.plot(profile.curve["timewise_deriv"].get_x(), profile.curve["timewise_deriv"].get_y())

    plt.show()