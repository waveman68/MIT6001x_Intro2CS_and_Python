import string

__author__ = 'Sam Broderick'


def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    :param base:
    :param exp:
    """
    # Your code here
    if exp == 0:
        return 1
    elif exp > 0:
        answer = base
        for n in range(1, exp):
            answer *= base
        return answer
    else:
        print('Error, exponent is not 0 or positive integer.')
        return


print('iterPower')
print(iterPower(2, 10))
print(iterPower(3, 3))
print(iterPower(4, 4))


def recurPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    :param exp:
    :param base:
    """
    # Your code here

    if exp == 0:
        return 1
    elif exp > 0:
        return base * recurPower(base, exp - 1)
    else:
        print('error')
        return


print('recurPower')
print(recurPower(2, 10))
print(recurPower(3, 3))
print(recurPower(4, 4))


def recurPowerNew(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    :param exp:
    :param base:
    """
    # Your code here
    if exp == 0:
        return 1
    elif exp > 1 and exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    elif exp > 0 and exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)
    else:
        print('error')
        return


print('recurPowerNew')
print(recurPowerNew(2, 10))
print(recurPowerNew(3, 3))
print(recurPowerNew(4, 4))


def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    :param b:
    :param a:
    """
    # Your code here
    if a > b:
        gcd = b
    elif b >= a:
        gcd = a
    else:
        print('Error')
    while (a % gcd != 0 or b % gcd != 0) and gcd > 1:
        gcd -= 1
    return gcd


print('gcdIter')
print(gcdIter(2, 3))
print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))


def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    :param b:
    :param a:
    """
    # Your code here

    if b == 0:
        return a
    elif b != 0:
        return gcdRecur(b, a % b)
    else:
        print('Error')
        return


print('gcdRecur')
print(gcdRecur(2, 3))
print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))


def lenIter(aStr):
    """
    aStr: a string

    returns: int, the length of aStr
    :param aStr:
    """
    # Your code here
    n = 0
    for char in aStr:
        n += 1
    return n


print('lenIter')
print(lenIter('Hello, world!'))


def lenRecur(aStr):
    """
    aStr: a string

    returns: int, the length of aStr
    :param aStr:
    """
    # Your code here
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])


print('lenRecur')
print(lenRecur('Hello, world!'))

'''My submission'''
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     # Your code here
#
#     if char == '' or aStr == '':
#         return False
#     else:
#         bisection = int(len(aStr)/2)
#         char_bisection = aStr[bisection]
#         if len(aStr) == 1 and char != char_bisection:
#             return False
#         elif char == char_bisection:
#             return True
#         elif char > char_bisection:
#             return isIn(char, aStr[bisection:len(aStr)])
#         elif char < char_bisection:
#             return isIn(char, aStr[0:bisection])
#         else:
#             return None

''' Instructor Solution - more elegant'''


def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    :param aStr:
    :param char:
    """
    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: See if the character in the middle of aStr equals the
    #   test character
    midIndex = len(aStr) / 2
    midChar = aStr[midIndex]
    if char == midChar:
        # We found the character!
        return True

    # Recursive case: If the test character is smaller than the middle
    #  character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Otherwise the test character is larger than the middle character,
    #  so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[midIndex + 1:])

my_ascii = string.ascii_letters[::-1]
print('isIn')
print(isIn('H', my_ascii))
print(isIn('Z', my_ascii[:51]))
print(isIn('a', ''))


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    """
    Compares 2 strings if they are palindromes
    :type str1: string - 1st input string
    :type str2: string - 2nd input string
    """
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    """
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
             :rtype: Boolean - is palindrome?
             :param str1:
             :param str2:
    """
    # Your code here

    # Why isn't this in the wrapper function?
    # Maybe because it doesn't interfere, but I imagine that it
    # costs cycles to open another function, so why not wrap it?

    # Reject strings of unequal length
    if len(str1) != len(str2):
        return False

    # One character left means str1 and str2 are palindromes since they the
    # original single-character case was excluded.
    if len(str1) == 1 and len(str2) == 1:
        return True

    Test = (str1[0] == str2[len(str2)-1])
    if Test and semordnilap(str1[1:], str2[:-1]):
        return True
    else:
        return False

print('semordnilap')
print(semordnilapWrapper('nametag', 'gateman'))
print(semordnilapWrapper('blues', 'hockey'))
print(semordnilapWrapper('desserts', 'stressed'))


def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)
