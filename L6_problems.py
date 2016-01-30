__author__ = 'Sam Broderick'

def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    :param aTup: tuple
    """
    # Your Code Here
    return_tuple = (aTup[0], )
    for n in range(2, len(aTup), 2):
        return_tuple = return_tuple + (aTup[n], )

    return return_tuple


