from string import ascii_lowercase

__author__ = 'Sam Broderick'

# Problem 1.1 True
x = 'pi'
y = 'pie'
x, y = y, x
print x, y


# Problem 1.2 False (terminates for all x <= 3)
def f(x):
    while x > 3:
        f(x + 1)


# Problem 1.3 False (not every line always, e.g. conditional)
# Problem 1.4 False (depends if x is local or global in both functions)



def ff(x):
    return x ** 2


print(f(-3))

# Problem 1.5 False (only if i >= 0 and j defined)

# i = 1
# j = 1
# while i >= 0:
#     while j >= 0:
#         print i, j

# Problem 1.6 False (testing is rarely complete)
# Problem 1.7 False (statement a = f(x) undefined, a=f  gives a pointer, a(2) returns None)
a = f
print(a)
print(a(2))

# Problem 1.8 False (keeps running is infinite loop, not syntax error)
# Problem 1.9 False (keeps running is infinite loop, not syntax error)
# Problem 1.10 False (keeps running is infinite loop, not syntax error)

L = [1, 2, 3]
d = {'a': 'b'}


def f(x):
    return 3


# print(L[3])
# print(d['b'])
# for i in range(1000001, -1, -2):
#     print f
# print int('abc')

def Square(x):
    return SquareHelper(abs(x), abs(x))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n - 1, x) + x


test = range(0, 11)
# for x in test:
#     print(Square(x))


# Problem 4
# ============


def isPalindrome(aString):
    """
    aString: a string
    """

    # Your code here
    def alpha_lower(string_in):
        """
        Zap any non-letters (e.g., spaces)
        :return: str
        :type string_in: str
        :param string_in:
        :rtype: str
        """
        string_in = string_in.lower()
        return_string = ''
        alphabet = ascii_lowercase
        for letter in string_in:
            if letter in alphabet:
                return_string += letter
        return return_string

    def is_pal_with_for(string_in):
        palindrome = True
        last = len(string_in) - 1
        for index in range(0, int(len(string_in) / 2)):
            palindrome = palindrome and string_in[index] == string_in[last - index]
        return palindrome

    return is_pal_with_for(alpha_lower(aString))


my_string = 'Able was I ere I saw Elba'
print('Is palindrome?')
print(isPalindrome(my_string))


# Problem 5
# ============


def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    :type listA: list
    :rtype: int
    """
    # Your code here
    assert len(listA) == len(listB)
    dot_product = 0
    try:
        for i in range(0, len(listA)):
            dot_product += listA[i] * listB[i]
    except AssertionError:
        print('Lists are not equal length!')

    return dot_product


print(dotProduct([1, 2, 3], [4, 5, 6]))
print(dotProduct([1, 2, 3], [1, 2, 3]))


# Problem 6
# ============


def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    :rtype: list
    :type aList: list
    """
    return_list = list()
    for element in aList:
        if type(element) == list:
            return_list = return_list + flatten(element)
        else:
            return_list.append(element)
    return return_list


print('Test flatten')
print('===========')
test_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(test_list))
print

# Problem 7
# ============


def f(a, b):
    return a > b
    # return a + b


def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    :type d1: dict
    :type d2: dict
    :rtype: object
    :param d1: integer dict
    """
    intersect = dict()
    difference = dict()

    for key1 in d1.iterkeys():
        if key1 in d2.keys():
            intersect.update({key1: f(d1[key1], d2[key1])})

    for key1 in d1.iterkeys():
        if key1 not in d2.keys():
            difference.update({key1: d1[key1]})
    for key2 in d2.iterkeys():
        if key2 not in d1.keys():
            difference.update({key2: d2[key2]})
    return_tuple = (intersect, difference)
    return return_tuple


print('dict_interdiff')
print('===========')
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# print(dict_interdiff(d1, d2))
print
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))

# Problem 8
# ============


# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     :rtype: int
#     """
#     # Your function implementation here
#     L_copy = L[:]
#     for element in L_copy:
#         if f(element):
#             pass
#         else:
#             L.remove(element)
#     return len(L)

# run_satisfiesF(L, satisfiesF)


# def f(s):
#     return len(s) > 6

print('I can''t get no satisfaction')
L = ['ali', 'baba', 'has', 'a', 'ghost']
# print satisfiesF(L)
print L

L2 = []
# print satisfiesF(L2)
print L2
