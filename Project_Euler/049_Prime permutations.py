# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

import time
import itertools
import math

start = time.time()

lim = 10000
is_prime = bytearray([1])*(lim+1)
is_prime[0] = is_prime[1] = 0
prime_list = []

for p, is_p in enumerate(is_prime):
    if is_p:
        m = lim//p-p+1
        is_prime[p**2::p] = bytearray([0])*m
        if int(math.log10(p)) == 3:
            prime_list.append(p)

answer = ''

while prime_list:
    p = prime_list[0]
    # Find permutation
    p_permu = map(lambda x: int(''.join(x)), itertools.permutations(str(p), 4))
    p_permu = list(set(filter(lambda x: x in prime_list, p_permu)))
    p_permu.sort()
    if not p_permu or len(p_permu) <= 2:
        prime_list.pop(0)
        continue
    prime_list = list(filter(lambda x: x not in p_permu, prime_list))
    # Check if the permutation fits the condition
    for numbers in list(itertools.combinations(p_permu, 3)):
        if numbers[2]-numbers[1] == numbers[1]-numbers[0]:
            print(time.time()-start)
            print(numbers)
            answer = ''.join(map(str, numbers))
            print('ANSWER: {a}'.format(a=answer))
