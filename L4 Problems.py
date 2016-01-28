def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    bitLo = min(lo, x, hi) == x
    bitX = min(lo, x, hi) == lo and max(lo, x, hi) == hi
    bitHi = max(lo, x, hi) == x
    result = lo * int(bitLo) + x * int(bitX) + hi * int(bitHi)

    return result

print(clip(10, 15, 20))
print(clip(10, 25, 20))
print(clip(10, 5, 20))


def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    test_str = char.lower()
    if (test_str == 'a' or test_str == 'e' or test_str == 'i' or
        test_str == 'o' or test_str == 'u'):
        return True
    else:
        return False


def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    test_str = char.lower()
    if test_str in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


print(isVowel2('A'))
