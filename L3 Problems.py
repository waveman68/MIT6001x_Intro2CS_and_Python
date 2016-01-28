import math

num = 0
while num <= 5:
    print num
    num += 1

print "Outside of loop"
print num

print('=======')

print('Hello!')
n = 10
while n >= 2:
    print n
    n -= 2

print('=======')

end = 6
n = 1
my_sum = 0
while n <= end:
    my_sum += n
    n += 1
print(my_sum)

print('=======')

myStr = '6.00x'

for char in myStr:
    print char

print 'done' ''

print('=======')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
            or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)

print('=======')

num = 10
for num in range(5):
    print num
print num

divisor = 2
for num in range(0, 10, 2):
    print num / divisor

print('=======')

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'

for letter in 'hola':
    print letter

print('=======')

count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count

print('=======')

for n in range(5):
    n += 1
    print(2 * n)
print "Goodbye!"

print('=======')

print "Hello!"
for n in range(5):
    print(10 - 2 * n)

print('=======')

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print('=======')

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess ** 2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess ** 2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

print('=======')

print('Please think of a number between 0 and 100!')
wrong = True
computer_guess = 50
max_guess = 100
min_guess = 0
counter = 0
while wrong:
    print('Is your secret number ' + str(computer_guess) + '?')
    s = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\''
                  ' to indicate the guess is too low. Enter \'c\' to indicate'
                  ' I guessed correctly. ',)
    if s == 'c':
        wrong = False
        print('Game over. Your secret number was: %u', computer_guess)
    elif s == 'h':
        max_guess = computer_guess
        computer_guess = int((computer_guess + min_guess)/2)
    elif s == 'l':
        min_guess = computer_guess
        computer_guess = int((computer_guess + max_guess)/2)
    else:
        print('You typed something else besides h, l, or c')
        counter += 1
        if counter > 99:
            wrong = False

print('=======')


def polysum(n, s):
    """
    Sum of the area and the square of the perimeter
    :rtype: float
    :param n: int - number of sides
    :param s: float - length of one side
    """
    perimeterSquared = (n * s)**2
    area = n * s**2 / (4 * math.tan(math.pi / n))
    result = round(perimeterSquared + area, 4)
    return result

print polysum(7, 4)
