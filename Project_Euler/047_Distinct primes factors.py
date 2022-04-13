# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import time
start = time.time()

def len_facto_4(x):
    i = 2
    factori = set()
    while i <= x:
        if x % i == 0:
            x = x / i
            factori.add(i)
        else:
            i += 1
    return len(factori) == 4

n = 1
sieve = [False]
cnt = 0
while True:
    sieve.append(len_facto_4(n))
    if sieve[n]:
        cnt += 1
    else:
        cnt = 0
    if cnt == 4:
        print(n-3)
        break

    n += 1



end = time.time()
print(end - start)
