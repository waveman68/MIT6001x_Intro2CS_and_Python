s = 'ohjelewfhricdfwiukkmauoi'

n = 0   # number of vowels
for letter in s:
    letter = letter.lower()
    if letter in ['a', 'e', 'i', 'o', 'u']:
        n += 1
result = 'Number of vowels: %u' % n
print(result)

print('=======')

s = 'azcbobobegghakl'

n = 0   # number of times bob occurs
i = 0   # last location bob was found
found = True    # was bob found?

while found:
    i = s.find('bob', i)
    if i >= 0:
        n += 1
    else:
        found = False
    i += 1

print('Number of times bob occurs is: %u' % n)

print('=======')


def item_order(order):
    """
    Counts the number of each menu item based on a space separated string of
    customer orders

    :rtype: None
    :param: Str - a space separated list of customer orders
    """
    salad = 0
    hamburger = 0
    water = 0

    salad = countSubString(order, 'salad')
    hamburger = countSubString(order, 'hamburger')
    water = countSubString(order, 'water')

    print('salad:%u hamburger:%u water:%u' % (salad, hamburger, water))
    return

def countSubString(s, ss):
    """
    Counts the
    :rtype: int
    :param s: str - a string that may contain the substring
    :param ss: str - a substring to look for
    """
    n = 0   # number of times bob occurs
    i = 0   # last location bob was found
    found = True    # was bob found?

    while found:
        i = s.find(ss, i)
        if i >= 0:
            n += 1
        else:
            found = False
        i += 1
    return n

order = "salad water hamburger salad hamburger"
item_order(order)
order = "hamburger water hamburger"
item_order(order)
