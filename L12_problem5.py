__author__ = 'Sam Broderick'


# my solution

# def genPrimes():
#     global n
#     n = 0               # iterator of list of primes
#     l_primes = [2]      # initialize list of primes
#     prime_not_found = True      # initialize boolean
#     is_prime = True
#     while True:
#         next = l_primes[n]
#         prime_not_found = True
#         yield next
#         n += 1
#
#         while prime_not_found:
#             next += 1
#             is_prime = True
#             for p in l_primes:
#                 is_prime = is_prime and (next % p) != 0
#             if is_prime:
#                 l_primes.append(next)
#                 prime_not_found = False
#
#
# for p in genPrimes():
#     print p
#     raw_input('Press return')

# of course the course solution is more elegant using for/else


# Note that our solution makes use of the for/else clause, which
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

primeGenerator = genPrimes()
primeGenerator.next()

for p in genPrimes():
    print p
    raw_input('Press return')
