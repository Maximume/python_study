# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

# 1. there is no prime number in permutations 1-9 (sum of all digits is 45, devided by 3)

# 2. by same method, there is no prime number in permutations 1-8

import time
import itertools

start = time.time()

def is_prime(x):
    if x<2: return False
    for i in range(2, int(x**0.5) +1):
        if x%i == 0: return False
    return True

arr = []
for i in range(7, 0, -1):
    arr += str(i)

permutations = []
for a, b, c, e, f, g, h in itertools.permutations(arr, 7):
    permutations.append(a+b+c+e+f+g+h)

for p in permutations:
    if is_prime(int(p)):
        print(p)
        break