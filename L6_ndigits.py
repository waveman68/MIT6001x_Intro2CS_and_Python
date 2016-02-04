__author__ = 'Sam Broderick'

# Note to grader: the """DocString""" adheres to Python style guide.

def ndigits(x):

    """
    This function takes an integer and returns its number of digits
    :param x: int - input
    :rtype: int - number of digits in x
    """
    if type(x) != int:                      # basic error handling of non-int
        print('The value of x is not an integer')
        return None
    if abs(x) < 10:
        return 1                            # single digit case
    x_recursive = int((x - x % 10)/10)      # remove last digit using modulo
    return 1 + ndigits(x_recursive)


# ================================
# Unit tests
# ================================
# print(ndigits(-1234))
# print(ndigits(-12345678))
# print(ndigits(42.12))
