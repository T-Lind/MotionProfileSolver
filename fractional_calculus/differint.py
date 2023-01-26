from scipy.special import gamma
from util import frange


def integral(a, b, func, res=0.01):
    """
    Returns the integral from a to b that is used in the differintegral calculation
    :param a: left bound
    :param b: right bound
    :param func: function to apply to
    :param res: resolution (data step increment)
    :return: numerical result
    """
    summation = 0

    # Perform left riemann sum
    for current_x in frange(a, b, res):
        summation += res * func(current_x)

    return summation


def derivative(a, func, res=0.01):
    """
    Calculate derivative at a point
    :param a: point to calculate derivative at
    :param func: function to calculate derivative of
    :param res: resolution (delta x)
    :return: the approximated derivative at point a
    """
    return (func(a + res) - func(a)) / res


def fractional_integral(p, t, func, res=0.01):
    """
    Returns the integral from a to b that is used in the differintegral calculation
    :param p: order of fractional integral to compute
    :param t: right bound, current time
    :param func: function to apply to
    :param res: resolution (data step increment)
    :return: numerical result
    """
    summation = 0

    # Uses a left riemann sum
    for current_x in frange(0, t, res):
        summation += (t - current_x) ** (p - 1) * func(current_x)

    return summation / gamma(p) * res

