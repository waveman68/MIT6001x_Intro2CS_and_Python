__author__ = 'Sam Broderick'





# def f(x):
#     import math
#     return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
      :param step: float
      :param stop: int
      :param start: int
    """
    if type(start) != int or type(stop) != int:         # Error handling
        print('Error. Start and stop must be integers')
        return None

    integral = 0                                        # initializing
    number_steps = int((stop - start)/step)             # range requires int

    for n in range(0, number_steps, 1):
        integral += step * f(start + n * step)
    return integral

print(radiationExposure(0, 5, 1))
print(radiationExposure(5, 11, 1))
print(radiationExposure(0, 11, 1))
print(radiationExposure(40, 100, 1.5))
