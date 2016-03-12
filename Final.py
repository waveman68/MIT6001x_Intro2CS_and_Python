__author__ = 'Sam Broderick'


def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary according to the instructions above
    :param d: dictionary to be inverted
    """
    # Your code here
    assert type(d) == dict
    d_inverted = {}
    for k, v in d.iteritems():
        if v not in d_inverted:
            d_inverted[v] = [k]
        else:
            d_inverted[v].append(k)
            d_inverted[v].sort()
    return d_inverted


d1 = {1: 10, 2: 20, 3: 30}
# print(dict_invert(d1))

d2 = {1: 10, 2: 20, 3: 30, 4: 30}
# print(dict_invert(d2))

d3 = {4: True, 2: True, 0: True}
# print(dict_invert(d3))

d4 = {8: 6, 2: 6, 4: 6, 6: 6}


# print(dict_invert(d4))


def getSublists(L, n):
    """

    :rtype: list
    :param L: List
    :param n: length of substring
    """
    return_list = []
    for ind in range(0, len(L) - n + 1):
        return_list.append(L[ind:ind + n])
    return return_list


L1 = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print(getSublists(L1, 4))
print(getSublists(L1, len(L1)))

L2 = [1, 1, 1, 1, 4]
print(getSublists(L2, 2))

print(getSublists([], 4))
print(getSublists([1, 2, 3], 4))
print('======')


def longestRun(L):
    """

    :param L: list
    """
    for n in range(len(L), 0, -1):
        sub_L = getSublists(L, n)
        ordered_run = False
        for idx in range(len(sub_L)):
            test = (sub_L[idx] == sorted(sub_L[idx]))
            ordered_run = ordered_run or test
        if ordered_run:
            return n

print(longestRun(L1))
