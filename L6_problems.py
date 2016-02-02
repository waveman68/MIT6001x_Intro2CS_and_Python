__author__ = 'Sam Broderick'


def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    :param aTup: tuple
    """
    # Your Code Here
    if aTup == ():
        return aTup
    return_tuple = (aTup[0], )
    for n in range(2, len(aTup), 2):
        return_tuple = return_tuple + (aTup[n], )

    return return_tuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
print(oddTuples(()))

listA = [1, 4, 3, 0]
listA.insert(0, 100)
listA.remove(3)
listA.index(1)


def absolute(a):
    return abs(a)

def plus_one(a):
    return a + 1

def square(a):
    return a**2

testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

applyToEach(testList, absolute)
print(testList)

testList = [1, -4, 8, -9]
applyToEach(testList, plus_one)
print(testList)

testList = [1, -4, 8, -9]
applyToEach(testList, square)
print(testList)

print('=============')


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a


def halve(a):
    return a/2


def inc(a):
    return a+1

print(applyToEach([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))
