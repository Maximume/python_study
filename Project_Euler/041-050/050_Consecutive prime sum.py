# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


from itertools import combinations
import time
start = time.time()

def call_prime_list(n:int) -> list:
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

# 1. make prime list under 1000000
primes = call_prime_list(1000000)

# 2. make set of primes for fast calculation
set_primes = set(primes)


max_len = 1
max_val = 1

for i in range(len(primes)):
    sm, sml = 0, []
    for j in range(i, len(primes)):
        sm += primes[j]
        sml.append(sm)

        if sm > 1000000:
            if sm - primes[j] in set_primes and len(sml) >= max_len:
                print(sm - primes[j])
                print(time.time() - start)
                break
    
    for idx, k in enumerate(sml[::-1]):
        if k in set_primes:
            if len(sml) - idx > max_len:
                max_len, max_val = len(sml) - idx, k
                break
print(max_val)


print(time.time() - start)