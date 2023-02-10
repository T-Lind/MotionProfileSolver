from custom_curve import Curve, Point
import matplotlib.pyplot as plt

if __name__ == "__main__":
    curve = Curve(Point(), Point(t=5, x=3, v=0, a=0))
    print(curve.points[500].t)
    print(curve.points[500].x)
    plt.plot(curve.points.get_linspace("t"), curve.points.get_linspace("x"), label="Position")
    plt.plot(curve.points.get_linspace("t"), curve.points.get_linspace("v"), label="Velocity")
    plt.plot(curve.points.get_linspace("t"), curve.points.get_linspace("a"), label="Acceleration")
    plt.legend()
    plt.show()
