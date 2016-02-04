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
    return a*a

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


def halve(a):
    return a/2


def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))


def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    animal_count = 0
    for dict_key in aDict:
        animal_count += len(aDict[dict_key])
    return animal_count

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print('howMany:')
print('=============')
print(howMany(animals))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    return_str = ''                 # initialize biggest dict_key for return

    if len(aDict) == 0:
        return None

    for dict_key in aDict:
        if aDict.has_key(return_str):     # compare entry lengths
            if len(aDict[dict_key]) >= len(aDict[return_str]):
                return_str = dict_key
        elif return_str == '':              # set first item for comparison
            return_str = dict_key

    return return_str

print('biggest:')
print('=============')

print(biggest(animals))
print(biggest({}))
print(biggest({'S': []}))
