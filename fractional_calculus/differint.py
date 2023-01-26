from scipy.special import gamma

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

    current_x = a
    while current_x <= b:
        summation += res * func(current_x)

        # Move up one
        current_x += res

    return summation

def fractional_integral(p, t, func, res=0.01):
    """
    Returns the integral from a to b that is used in the differintegral calculation
    :param p: order of fractional integral to compute
    :param a: left bound
    :param t: right bound
    :param func: function to apply to
    :param res: resolution (data step increment)
    :return: numerical result
    """
    summation = 0

    current_x = 0
    while current_x <= t:
        summation += (t - current_x)**(p-1)*func(current_x)

        # Move up one
        current_x += res

    return summation*1/gamma(p)

